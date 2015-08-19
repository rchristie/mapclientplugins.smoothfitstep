'''
Created on Jul 16, 2015

@author: Richard Christie
'''
import json
from opencmiss.zinc.context import Context
from opencmiss.zinc.field import Field, FieldFindMeshLocation
from opencmiss.zinc.glyph import Glyph
from opencmiss.zinc.graphics import Graphics
from opencmiss.zinc.material import Material
from opencmiss.zinc.optimisation import Optimisation
from opencmiss.zinc.scenefilter import Scenefilter
from opencmiss.zinc.scenecoordinatesystem import SCENECOORDINATESYSTEM_NORMALISED_WINDOW_FIT_LEFT
from opencmiss.zinc.status import OK as ZINC_OK
from mapclientplugins.smoothfitstep.maths import vectorops
from mapclientplugins.smoothfitstep.utils import zinc as zincutils

class SmoothfitModel(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._context = Context('surfacefit')
        materialmodule = self._context.getMaterialmodule()
        materialmodule.beginChange()
        materialmodule.defineStandardMaterials()
        self._surfaceMaterial = materialmodule.createMaterial()
        self._surfaceMaterial.setName('fit-surface')
        self._surfaceMaterial.setAttributeReal3(Material.ATTRIBUTE_AMBIENT, [0.7, 0.7, 1.0])
        self._surfaceMaterial.setAttributeReal3(Material.ATTRIBUTE_DIFFUSE, [0.7, 0.7, 1.0])
        self._surfaceMaterial.setAttributeReal3(Material.ATTRIBUTE_SPECULAR, [0.5, 0.5, 0.5])
        self._surfaceMaterial.setAttributeReal(Material.ATTRIBUTE_ALPHA, 0.5)
        self._surfaceMaterial.setAttributeReal(Material.ATTRIBUTE_SHININESS, 0.3)
        materialmodule.endChange()
        glyphmodule = self._context.getGlyphmodule()
        glyphmodule.defineStandardGlyphs()
        tessellationmodule = self._context.getTessellationmodule()
        defaultTessellation = tessellationmodule.getDefaultTessellation()
        defaultTessellation.setRefinementFactors([12])
        self._location = None
        self._zincModelFile = None
        self._zincPointCloudFile = None
        self.clear()

    def clear(self):
        '''
        Ensure scene for this region is not in use before calling!
        '''
        self._region = None
        self._mesh = None
        self._modelCoordinateField = None
        self._modelReferenceCoordinateField = None
        self._modelOffsetField = None # 3 vector
        self._modelRotationScaleField = None # 3x3 matrix
        self._modelTransformedCoordinateField = None
        self._dataCoordinateField = None
        self._findMeshLocationField = None
        self._storedMeshLocationField = None
        self._dataProjectionCoordinateField = None
        self._dataProjectionDeltaCoordinateField = None
        self._dataProjectionErrorField = None
        self._dataProjectionMeanErrorField = None
        self._dataProjectionMaximumErrorField = None
        self._projectSurfaceElementGroup = None
        self._resetAlignSettings()
        self._resetFitSettings()
        self._isStateAlign = True

    def getContext(self):
        return self._context

    def setLocation(self, location):
        self._location = location

    def getRegion(self):
        return self._region

    def setZincModelFile(self, zincModelFile):
        self._zincModelFile = zincModelFile.encode('ASCII')

    def setZincPointCloudFile(self, zincPointCloudFile):
        self._zincPointCloudFile = zincPointCloudFile.encode('ASCII')

    def initialise(self):
        self._region = self._context.createRegion()
        self.setStateAlign()

# ----- Align Settings -----

    def _resetAlignSettings(self):
        self._alignSettings = dict(euler_angles = [0.0, 0.0, 0.0], scale = 1.0, offset = [0.0, 0.0, 0.0])

    def setAlignSettingsChangeCallback(self, alignSettingsChangeCallback):
        self._alignSettingsChangeCallback = alignSettingsChangeCallback

    def getAlignScale(self):
        return self._alignSettings['scale']

    def setAlignScale(self, scale):
        self._alignSettings['scale'] = scale
        self._applyAlignSettings()

    def getAlignEulerAngles(self):
        return self._alignSettings['euler_angles']

    def setAlignEulerAngles(self, eulerAngles):
        if len(eulerAngles) == 3:
            self._alignSettings['euler_angles'] = eulerAngles
            self._applyAlignSettings()

    def getAlignOffset(self):
        return self._alignSettings['offset']

    def setAlignOffset(self, offset):
        if len(offset) == 3:
            self._alignSettings['offset'] = offset
            self._applyAlignSettings()

    def _applyAlignSettings(self):
        rot = vectorops.eulerToRotationMatrix3(self._alignSettings['euler_angles'])
        scale = self._alignSettings['scale']
        rotationScale = [
            rot[0][0]*scale, rot[0][1]*scale, rot[0][2]*scale,
            rot[1][0]*scale, rot[1][1]*scale, rot[1][2]*scale,
            rot[2][0]*scale, rot[2][1]*scale, rot[2][2]*scale]
        fm = self._region.getFieldmodule()
        fm.beginChange()
        if self._modelTransformedCoordinateField is None:
            self._modelRotationScaleField = fm.createFieldConstant(rotationScale)
            # following works in 3-D only
            temp1 = fm.createFieldMatrixMultiply(3, self._modelRotationScaleField, self._modelCoordinateField)
            self._modelOffsetField = fm.createFieldConstant(self._alignSettings['offset'])
            self._modelTransformedCoordinateField = fm.createFieldAdd(temp1, self._modelOffsetField)
        else:
            cache = fm.createFieldcache()
            self._modelRotationScaleField.assignReal(cache, rotationScale);
            self._modelOffsetField.assignReal(cache, self._alignSettings['offset'])
        fm.endChange()
        if not self._modelTransformedCoordinateField.isValid():
            print "Can't create transformed model coordinate field. Is problem 2-D?"
        self._alignSettingsChangeCallback()

    def loadAlignSettings(self):
        with open(self._location + '-align-settings.json', 'r') as f:
            self._alignSettings.update(json.loads(f.read()))
        self._applyAlignSettings()

    def saveAlignSettings(self):
        with open(self._location + '-align-settings.json', 'w') as f:
            f.write(json.dumps(self._alignSettings, default=lambda o: o.__dict__, sort_keys=True, indent=4))

    def resetAlignment(self):
        self._resetAlignSettings()
        self._applyAlignSettings()

    def scaleModel(self, factor):
        self._alignSettings['scale'] *= factor
        self._applyAlignSettings()

    def rotateModel(self, axis, angle):
        quat = vectorops.axisAngleToQuaternion(axis, angle)
        mat1 = vectorops.rotmx(quat)
        mat2 = vectorops.eulerToRotationMatrix3(self._alignSettings['euler_angles'])
        newmat = vectorops.matrixmult(mat1, mat2)
        self._alignSettings['euler_angles'] = vectorops.rotationMatrix3ToEuler(newmat)
        self._applyAlignSettings()

    def offsetModel(self, relativeOffset):
        self._alignSettings['offset'] = vectorops.add(self._alignSettings['offset'], relativeOffset)
        self._applyAlignSettings()

    def autoCentreModelOnData(self):
        minimums, maximums = self._getDataRange()
        dataCentre = vectorops.mult(vectorops.add(minimums, maximums), 0.5)
        self.setAlignOffset(vectorops.sub(dataCentre, self._modelCentre))

    def isStateAlign(self):
        return self._isStateAlign

    def setStateAlign(self):
        self._isStateAlign = True
        self.clearDataProjections()
        self._load()

    def setStatePostAlign(self):
        if not self._isStateAlign:
            return
        self._isStateAlign = False
        rotationScale = vectorops.matrixconstantmult(vectorops.eulerToRotationMatrix3(self._alignSettings['euler_angles']), self._alignSettings['scale'])
        zincutils.transformCoordinates(self._modelCoordinateField, rotationScale, self._alignSettings['offset'])
        self._setModelGraphicsCoordinateField(self._modelCoordinateField)

# ----- Fit Settings -----

    def _resetFitSettings(self):
        self._fitSettings = dict(strain_penalty = 0.0, edge_discontinuity_penalty = 0.0)

    def setFitSettingsChangeCallback(self, fitSettingsChangeCallback):
        self._fitSettingsChangeCallback = fitSettingsChangeCallback

    def getFitStrainPenalty(self):
        return self._fitSettings['strain_penalty']

    def setFitStrainPenalty(self, penalty):
        self._fitSettings['strain_penalty'] = penalty

    def getFitEdgeDiscontinuityPenalty(self):
        return self._fitSettings['edge_discontinuity_penalty']

    def setFitEdgeDiscontinuityPenalty(self, penalty):
        self._fitSettings['edge_discontinuity_penalty'] = penalty

    def loadFitSettings(self):
        with open(self._location + '-fit-settings.json', 'r') as f:
            self._fitSettings.update(json.loads(f.read()))
        self._fitSettingsChangeCallback()

    def saveFitSettings(self):
        with open(self._location + '-fit-settings.json', 'w') as f:
            f.write(json.dumps(self._fitSettings, default=lambda o: o.__dict__, sort_keys=True, indent=4))

# -----

    def _getMesh(self):
        '''
        Return highest dimension mesh
        '''
        fm = self._region.getFieldmodule()
        for dimension in range(3,1,-1):
            mesh = fm.findMeshByDimension(dimension)
            if mesh.getSize() > 0:
                return mesh
        raise ValueError('Model contains no mesh');

    def _getModelCoordinateField(self):
        """
        Return first coordinate field defined on first element of highest dimension mesh
        """
        mesh = self._getMesh()
        element = mesh.createElementiterator().next()
        if not element.isValid():
            raise ValueError('Model contains no elements');
        fm = self._region.getFieldmodule()
        cache = fm.createFieldcache()
        cache.setElement(element)
        fieldIter = fm.createFielditerator()
        field = fieldIter.next()
        while field.isValid():
            if field.isTypeCoordinate() and (field.getNumberOfComponents() <= 3) and ((self._modelReferenceCoordinateField is None) or (field != self._modelReferenceCoordinateField)):
                if field.isDefinedAtLocation(cache):
                    return field
            field = fieldIter.next()
        raise ValueError('Could not determine model coordinate field')

    def _getDataCoordinateField(self):
        """
        Return first coordinate field defined on first datapoint
        """
        fm = self._region.getFieldmodule()
        datapoints = fm.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)
        datapoint = datapoints.createNodeiterator().next()
        if not datapoint.isValid():
            raise ValueError('Point cloud is empty')
        cache = fm.createFieldcache()
        cache.setNode(datapoint)
        fieldIter = fm.createFielditerator()
        field = fieldIter.next()
        while field.isValid():
            if field.isTypeCoordinate() and (field.getNumberOfComponents() <= 3) and ((self._modelReferenceCoordinateField is None) or (field != self._modelReferenceCoordinateField)):
                if field.isDefinedAtLocation(cache):
                    return field
            field = fieldIter.next()
        raise ValueError('Could not determine data coordinate field')

    def _getProjectSurfaceGroup(self):
        fm = self._region.getFieldmodule()
        projectSurfaceGroup = fm.findFieldByName('projectsurface').castGroup()
        if projectSurfaceGroup.isValid():
            mesh2d = fm.findMeshByDimension(2)
            projectSurfaceElementGroup = projectSurfaceGroup.getFieldElementGroup(mesh2d)
            if projectSurfaceElementGroup.isValid() and (projectSurfaceElementGroup.getMeshGroup().getSize() > 0):
                return projectSurfaceGroup, projectSurfaceElementGroup
        return None, None

    def _load(self):
        if self._modelReferenceCoordinateField is None:
            # read and rename coordinates to reference_coordinates, for calculating strains
            result = self._region.readFile(self._zincModelFile)
            if result != ZINC_OK:
                raise ValueError('Failed to read reference model')
            self._modelReferenceCoordinateField = self._getModelCoordinateField()
            name = self._modelReferenceCoordinateField.getName()
            number = 0
            numberString = ''
            while True:
                result = self._modelReferenceCoordinateField.setName('reference_' + name + numberString)
                if result == ZINC_OK:
                    #print 'Renamed field', name, ' to', 'reference_' + name + numberString
                    break
                number = number + 1
                numberString = str(number)
            # read data cloud
            sir = self._region.createStreaminformationRegion()
            pointCloudResource = sir.createStreamresourceFile(self._zincPointCloudFile)
            sir.setResourceDomainTypes(pointCloudResource, Field.DOMAIN_TYPE_DATAPOINTS)
            result = self._region.read(sir)
            if result != ZINC_OK:
                raise ValueError('Failed to read point cloud')
            self._dataCoordinateField = self._getDataCoordinateField()
        result = self._region.readFile(self._zincModelFile)
        if result != ZINC_OK:
            raise ValueError('Failed to read model')
        self._mesh = self._getMesh()
        self._modelCoordinateField = self._getModelCoordinateField()
        minimums, maximums = self._getModelRange()
        self._modelCentre = vectorops.mult(vectorops.add(minimums, maximums), 0.5)
        self._projectSurfaceGroup, self._projectSurfaceElementGroup = self._getProjectSurfaceGroup()
        self._applyAlignSettings()
        self._showModelGraphics()

    def _getNodesetMinimumMaximum(self, nodeset, field):
        fm = field.getFieldmodule()
        count = field.getNumberOfComponents()
        minimumsField = fm.createFieldNodesetMinimum(field, nodeset)
        maximumsField = fm.createFieldNodesetMaximum(field, nodeset)
        cache = fm.createFieldcache()
        result, minimums = minimumsField.evaluateReal(cache, count)
        if result != ZINC_OK:
            minimums = None
        result, maximums = maximumsField.evaluateReal(cache, count)
        if result != ZINC_OK:
            maximums = None
        del minimumsField
        del maximumsField
        return minimums, maximums

    def _getDataRange(self):
        fm = self._region.getFieldmodule()
        datapoints = fm.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)
        minimums, maximums = self._getNodesetMinimumMaximum(datapoints, self._dataCoordinateField)
        return minimums, maximums

    def _getModelRange(self):
        fm = self._region.getFieldmodule()
        nodes = fm.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_NODES)
        minimums, maximums = self._getNodesetMinimumMaximum(nodes, self._modelCoordinateField)
        return minimums, maximums

    def _getAutoPointSize(self):
        minimums, maximums = self._getDataRange()
        dataSize = vectorops.magnitude(vectorops.sub(maximums, minimums))
        return 0.005*dataSize

    def _showModelGraphics(self):
        scene = self._region.getScene()
        scene.beginChange()
        scene.removeAllGraphics()
        materialmodule = scene.getMaterialmodule()
        axes = scene.createGraphicsPoints()
        pointAttr = axes.getGraphicspointattributes()
        pointAttr.setGlyphShapeType(Glyph.SHAPE_TYPE_AXES_XYZ)
        pointAttr.setBaseSize(1.0)
        axes.setMaterial(materialmodule.findMaterialByName('brown'))
        points = scene.createGraphicsPoints()
        points.setFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)
        points.setCoordinateField(self._dataCoordinateField)
        pointAttr = points.getGraphicspointattributes()
        pointAttr.setGlyphShapeType(Glyph.SHAPE_TYPE_CROSS)
        pointSize = self._getAutoPointSize()
        pointAttr.setBaseSize(pointSize)
        points.setMaterial(materialmodule.findMaterialByName('silver'))
        lines = scene.createGraphicsLines()
        if self._mesh.getDimension() == 3:
            lines.setExterior(True)
        lines.setName('fit-lines')
        lines.setCoordinateField(self._modelTransformedCoordinateField)
        surfaces = scene.createGraphicsSurfaces()
        if self._projectSurfaceElementGroup is not None:
            surfaces.setSubgroupField(self._projectSurfaceElementGroup)
        surfaces.setName('fit-surfaces')
        surfaces.setCoordinateField(self._modelTransformedCoordinateField)
        surfaces.setMaterial(self._surfaceMaterial)
        scene.endChange()

    def _setModelGraphicsCoordinateField(self, coordinateField):
        scene = self._region.getScene()
        scene.beginChange()
        for name in ['fit-lines', 'fit-surfaces']:
            graphics = scene.findGraphicsByName(name)
            graphics.setCoordinateField(coordinateField)
        scene.endChange()

    def clearDataProjections(self):
        if self._storedMeshLocationField is None:
            return
        fm = self._region.getFieldmodule()
        fm.beginChange()
        datapoints =  fm.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)
        nodetemplate = datapoints.createNodetemplate()
        nodetemplate.undefineField(self._storedMeshLocationField)
        dataIter = datapoints.createNodeiterator()
        datapoint = dataIter.next()
        while datapoint.isValid():
           datapoint.merge(nodetemplate)
           datapoint = dataIter.next()
        self._storedMeshLocationField = None
        self._findMeshLocationField = None
        fm.endChange()
        self._hideDataProjections()

    def calculateDataProjections(self):
        fm = self._region.getFieldmodule()
        mesh = self._mesh
        if self._projectSurfaceElementGroup is not None:
            mesh = self._projectSurfaceElementGroup.getMeshGroup()
        if self._findMeshLocationField is None:
            self._findMeshLocationField = fm.createFieldFindMeshLocation(self._dataCoordinateField, self._modelCoordinateField, mesh)
            if self._findMeshLocationField.isValid():
                self._findMeshLocationField.setSearchMode(FieldFindMeshLocation.SEARCH_MODE_NEAREST)
            else:
                self._findMeshLocationField = None
                raise ValueError('Failed to create find mesh location field. Possibly because no coordinate field or mesh?')
        if self._storedMeshLocationField is None:
            self._storedMeshLocationField = fm.createFieldStoredMeshLocation(mesh)
            if not self._storedMeshLocationField.isValid():
                self._storedMeshLocationField = None
                raise ValueError('Failed to create stored mesh location field. Possibly because no mesh?')
        datapoints =  fm.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)
        dimension = mesh.getDimension()
        fm.beginChange()
        self._dataProjectionCoordinateField = fm.createFieldEmbedded(self._modelCoordinateField, self._storedMeshLocationField)
        self._dataProjectionDeltaCoordinateField = fm.createFieldSubtract(self._dataProjectionCoordinateField, self._dataCoordinateField)
        self._dataProjectionErrorField = fm.createFieldMagnitude(self._dataProjectionDeltaCoordinateField)
        self._dataProjectionMeanErrorField = fm.createFieldNodesetMean(self._dataProjectionErrorField, datapoints)
        self._dataProjectionMaximumErrorField = fm.createFieldNodesetMaximum(self._dataProjectionErrorField, datapoints)
        datapoints =  fm.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)
        nodetemplate = datapoints.createNodetemplate()
        nodetemplate.defineField(self._storedMeshLocationField)
        cache = fm.createFieldcache()
        dataIter = datapoints.createNodeiterator()
        datapoint = dataIter.next()
        while datapoint.isValid():
            cache.setNode(datapoint)
            element, xi = self._findMeshLocationField.evaluateMeshLocation(cache, dimension)
            if element.isValid():
                datapoint.merge(nodetemplate)
                self._storedMeshLocationField.assignMeshLocation(cache, element, xi)
            datapoint = dataIter.next()
        fm.endChange()
        self._showDataProjections()

    def _hideDataProjections(self):
        scene = self._region.getScene()
        scene.beginChange()
        graphics = scene.findGraphicsByName('data-projections')
        scene.removeGraphics(graphics)
        graphics = scene.findGraphicsByName('data-mean-error')
        scene.removeGraphics(graphics)
        graphics = scene.findGraphicsByName('data-maximum-error')
        scene.removeGraphics(graphics)
        scene.endChange()

    def _autorangeSpectrum(self):
        scene = self._region.getScene()
        spectrummodule = scene.getSpectrummodule()
        defaultSpectrum = spectrummodule.getDefaultSpectrum()
        spectrummodule.beginChange()
        result, minimum, maximum = scene.getSpectrumDataRange(Scenefilter(), defaultSpectrum, 1)
        spectrumComponent = defaultSpectrum.getFirstSpectrumcomponent()
        spectrumComponent.setRangeMinimum(minimum)
        spectrumComponent.setRangeMaximum(maximum)
        spectrummodule.endChange()

    def _showDataProjections(self):
        scene = self._region.getScene()
        scene.beginChange()
        materialmodule = scene.getMaterialmodule()
        spectrummodule = scene.getSpectrummodule()
        defaultSpectrum = spectrummodule.getDefaultSpectrum()

        errorBars = scene.createGraphicsPoints()
        errorBars.setName('data-projections')
        errorBars.setFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)
        errorBars.setCoordinateField(self._dataCoordinateField)
        pointAttr = errorBars.getGraphicspointattributes()
        pointAttr.setGlyphShapeType(Glyph.SHAPE_TYPE_LINE)
        pointAttr.setBaseSize([0.0,1.0,1.0])
        pointAttr.setScaleFactors([1.0,0.0,0.0])
        pointAttr.setOrientationScaleField(self._dataProjectionDeltaCoordinateField)
        errorBars.setDataField(self._dataProjectionErrorField)
        errorBars.setSpectrum(defaultSpectrum)

        meanError = scene.createGraphicsPoints()
        meanError.setName('data-mean-error')
        meanError.setScenecoordinatesystem(SCENECOORDINATESYSTEM_NORMALISED_WINDOW_FIT_LEFT)
        pointAttr = meanError.getGraphicspointattributes()
        pointAttr.setBaseSize([1.0,1.0,1.0])
        pointAttr.setGlyphOffset([-0.9,0.9,0.0])
        pointAttr.setGlyphShapeType(Glyph.SHAPE_TYPE_NONE)
        pointAttr.setLabelText(1, 'Mean error:  ')
        pointAttr.setLabelField(self._dataProjectionMeanErrorField)

        maximumError = scene.createGraphicsPoints()
        maximumError.setName('data-maximum-error')
        maximumError.setScenecoordinatesystem(SCENECOORDINATESYSTEM_NORMALISED_WINDOW_FIT_LEFT)
        pointAttr = maximumError.getGraphicspointattributes()
        pointAttr.setBaseSize([1.0,1.0,1.0])
        pointAttr.setGlyphOffset([-0.9,0.8,0.0])
        pointAttr.setGlyphShapeType(Glyph.SHAPE_TYPE_NONE)
        pointAttr.setLabelText(1, 'Max. error:  ')
        pointAttr.setLabelField(self._dataProjectionMaximumErrorField)
        maximumError.setMaterial(materialmodule.findMaterialByName('red'))

        # ensure semi-transparent surfaces drawn last for best transparency
        surfaces = scene.findGraphicsByName('fit-surfaces')
        scene.moveGraphicsBefore(surfaces, Graphics())

        self._autorangeSpectrum()
        scene.endChange()

    def _getStrainField(self, mesh):
        fm = self._region.getFieldmodule()
        dimension = mesh.getDimension()
        if dimension == 2:
            # assume nu ~ xi; effect is to penalise elements where this is not so, which is also desired
            dX_dxi1 = fm.createFieldDerivative(self._modelReferenceCoordinateField, 1)
            dX_dxi2 = fm.createFieldDerivative(self._modelReferenceCoordinateField, 2)
            FXT = fm.createFieldConcatenate([dX_dxi1, dX_dxi2])
            FX = fm.createFieldTranspose(2, FXT)
            FXT_FX = fm.createFieldMatrixMultiply(2, FXT, FX)
            dx_dxi1 = fm.createFieldDerivative(self._modelCoordinateField, 1)
            dx_dxi2 = fm.createFieldDerivative(self._modelCoordinateField, 2)
            FxT = fm.createFieldConcatenate([dx_dxi1, dx_dxi2])
            Fx = fm.createFieldTranspose(2, FxT)
            FxT_Fx = fm.createFieldMatrixMultiply(2, FxT, Fx)
            # should multiply following by 0.5, but not needed due to arbitrary weighting
            strainField = fm.createFieldSubtract(FxT_Fx, FXT_FX)
            return strainField
        return None

    def _showStrains(self, strainField):
        scene = self._region.getScene()
        scene.beginChange()
        materialmodule = scene.getMaterialmodule()
        points = scene.createGraphicsPoints()
        points.setFieldDomainType(Field.DOMAIN_TYPE_MESH2D)
        points.setCoordinateField(self._modelCoordinateField)
        pointAttr = points.getGraphicspointattributes()
        pointAttr.setGlyphShapeType(Glyph.SHAPE_TYPE_NONE)
        pointAttr.setLabelField(strainField)
        points.setMaterial(materialmodule.findMaterialByName('silver'))
        scene.endChange()

    def fit(self):
        if self._storedMeshLocationField is None:
            raise ValueError('Cannot fit before data point projections are found')
        fm = self._region.getFieldmodule()
        datapoints =  fm.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)
        optimisation = fm.createOptimisation()
        optimisation.setMethod(Optimisation.METHOD_LEAST_SQUARES_QUASI_NEWTON)
        surfaceFitObjectiveField = fm.createFieldNodesetSumSquares(self._dataProjectionDeltaCoordinateField, datapoints)
        result = optimisation.addObjectiveField(surfaceFitObjectiveField)
        if result != ZINC_OK:
            raise ValueError('Could not set optimisation surface fit objective field')
        numberOfGaussPoints = 4
        mesh = self._mesh
        lineMesh = fm.findMeshByDimension(1)
        if self._projectSurfaceElementGroup is not None:
            mesh = self._projectSurfaceElementGroup.getMeshGroup()
            lineMeshGroup = self._projectSurfaceGroup.getFieldElementGroup(lineMesh).getMeshGroup()
            if lineMeshGroup.isValid():
                lineMesh = lineMeshGroup
        if self.getFitStrainPenalty() > 0.0:
            strainField = self._getStrainField(mesh)
            if strainField is None:
                print 'Not supported: Apply Strain Penalty', self.getFitStrainPenalty()
            else:
                #print 'Apply Strain Penalty', self.getFitStrainPenalty()
                weightField = fm.createFieldConstant(self.getFitStrainPenalty())
                weightedStrainField = strainField*weightField
                weightedStrainFieldIntegralField = fm.createFieldMeshIntegralSquares(weightedStrainField, self._modelReferenceCoordinateField, mesh)
                weightedStrainFieldIntegralField.setNumbersOfPoints(numberOfGaussPoints)
                result = optimisation.addObjectiveField(weightedStrainFieldIntegralField)
                if result != ZINC_OK:
                    raise ValueError('Could not add optimisation strain penalty objective field')
        if self.getFitEdgeDiscontinuityPenalty() > 0.0:
            #print 'Apply Edge Discontinuity Penalty', self.getFitEdgeDiscontinuityPenalty()
            edgeDiscontinuityField = fm.createFieldEdgeDiscontinuity(self._modelCoordinateField)
            weightField = fm.createFieldConstant(self.getFitEdgeDiscontinuityPenalty())
            weightedEdgeDiscontinuityField = edgeDiscontinuityField*weightField
            weightedEdgeDiscontinuityIntegralField = fm.createFieldMeshIntegralSquares(weightedEdgeDiscontinuityField, self._modelReferenceCoordinateField, lineMesh)
            weightedEdgeDiscontinuityIntegralField.setNumbersOfPoints(numberOfGaussPoints)
            result = optimisation.addObjectiveField(weightedEdgeDiscontinuityIntegralField)
            if result != ZINC_OK:
                raise ValueError('Could not add optimisation edge discontinuity penalty objective field')
        result = optimisation.addIndependentField(self._modelCoordinateField)
        if result != ZINC_OK:
            raise ValueError('Could not set optimisation dependent field')
        if self._projectSurfaceGroup is not None:
            optimisation.setConditionalField(self._modelCoordinateField, self._projectSurfaceGroup)
        result = optimisation.setAttributeInteger(Optimisation.ATTRIBUTE_MAXIMUM_ITERATIONS, 1)
        if result != ZINC_OK:
            raise ValueError('Could not set optimisation maximum iterations')
        #optimisation.setAttributeInteger(Optimisation.ATTRIBUTE_MAXIMUM_FUNCTION_EVALUATIONS, 100000)
        result = optimisation.optimise()
        if result != ZINC_OK:
            raise ValueError('Optimisation failed with result ' + str(result))
        self._autorangeSpectrum()
        #self._showStrains()