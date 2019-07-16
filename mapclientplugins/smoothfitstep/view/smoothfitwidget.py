'''
Created on July 15, 2015

@author: Richard Christie
'''
from PySide import QtGui, QtCore

from mapclientplugins.smoothfitstep.view.ui_smoothfitwidget import Ui_SmoothfitWidget
from opencmiss.zinc.scene import Scene

class SmoothfitWidget(QtGui.QWidget):
    '''
    classdocs
    '''


    def __init__(self, model, parent=None):
        '''
        Constructor
        '''
        super(SmoothfitWidget, self).__init__(parent)
        self._ui = Ui_SmoothfitWidget()
        self._ui.setupUi(self)
        self._ui.sceneviewerWidget.setContext(model.getContext())
        self._ui.sceneviewerWidget.setModel(model)
        self._model = model
        self._model.setAlignSettingsChangeCallback(self._alignSettingsDisplay)
        self._model.setFitSettingsChangeCallback(self._fitSettingsDisplay)
        self._ui.sceneviewerWidget.graphicsInitialized.connect(self._graphicsInitialized)
        self._scene = None
        self._callback = None
        self._makeConnections()

    def _graphicsInitialized(self):
        '''
        Callback for when SceneviewerWidget is initialised
        Set custom scene from model
        '''
        sceneviewer = self._ui.sceneviewerWidget.getSceneviewer()
        if sceneviewer is not None:
            scene = self._model.getRegion().getScene()
            sceneviewer.setScene(scene)
            sceneviewer.viewAll()

    def _makeConnections(self):
        self._ui.doneButton.clicked.connect(self._doneButtonClicked)
        self._ui.viewAllButton.clicked.connect(self._viewAllButtonClicked)
        self._ui.toolBox.currentChanged.connect(self._toolBoxPageChange)
        self._ui.alignLoadButton.clicked.connect(self._alignLoadButtonClicked)
        self._ui.alignSaveButton.clicked.connect(self._alignSaveButtonClicked)
        self._ui.alignScaleLineEdit.editingFinished.connect(self._alignScaleEntered)
        self._ui.alignRotationLineEdit.editingFinished.connect(self._alignRotationEntered)
        self._ui.alignOffsetLineEdit.editingFinished.connect(self._alignOffsetEntered)
        self._ui.alignMirrorCheckBox.clicked.connect(self._alignMirrorClicked)
        self._ui.alignResetButton.clicked.connect(self._alignResetButtonClicked)
        self._ui.alignAutoCentreButton.clicked.connect(self._alignAutoCentreButtonClicked)
        self._ui.projectClearButton.clicked.connect(self._projectClearButtonClicked)
        self._ui.projectPointsButton.clicked.connect(self._projectPointsButtonClicked)
        self._ui.filterTopErrorPushButton.clicked.connect(self._filterTopErrorClicked)
        self._ui.filterTopErrorProportionLineEdit.editingFinished.connect(self._filterTopErrorProportionEntered)
        self._ui.filterNonNormalPushButton.clicked.connect(self._filterNonNormalClicked)
        self._ui.filterNonNormalProjectionLimitLineEdit.editingFinished.connect(self._filterNonNormalProjectionLimitEntered)
        self._ui.fitLoadButton.clicked.connect(self._fitLoadButtonClicked)
        self._ui.fitSaveButton.clicked.connect(self._fitSaveButtonClicked)
        self._ui.fitStrainPenaltyLineEdit.editingFinished.connect(self._fitStrainPenaltyEntered)
        self._ui.fitCurvaturePenaltyLineEdit.editingFinished.connect(self._fitCurvaturePenaltyEntered)
        self._ui.fitEdgeDiscontinuityPenaltyLineEdit.editingFinished.connect(self._fitEdgeDiscontinuityPenaltyEntered)
        self._ui.fitMaxIterationsSpinBox.valueChanged.connect(self._fitMaxIterationsValueChanged)
        self._ui.fitPerformButton.clicked.connect(self._fitPerformButtonClicked)

    def clear(self):
        self._scene = None
        self._model.clear()

    def initialise(self):
        self._model.initialise()
        self._scene = self._model.getRegion().getScene()
        self._setupUi()
        if self._model.isStateAlign:
            self._ui.toolBox.setCurrentIndex(0)
        else:
            self._ui.toolBox.setCurrentIndex(1)
        self._graphicsInitialized()

    def setEnableSettingsSave(self, isEnabled):
        self._ui.alignSaveButton.setEnabled(isEnabled)
        self._ui.fitSaveButton.setEnabled(isEnabled)

    def setEnableLoadPreviousSolution(self, isEnabled):
        self._model._enableloadPreviousSolution = isEnabled

    def getModel(self):
        return self._model

    def _displayReal(self, widget, value):
        newText = '{:.4g}'.format(value)
        widget.setText(newText)

    def _parseRealNonNegative(self, widget, currentValue):
        newValue = currentValue
        try:
            value = float(widget.text())
            if value < 0.0:
                raise ValueError("Value must be >= 0")
            newValue = value
        except:
            print("Value must be >= 0")
        self._displayReal(widget, newValue)
        return newValue

    def _parseRealZeroToOne(self, widget, currentValue):
        newValue = currentValue
        try:
            value = float(widget.text())
            if (value < 0.0) or (value > 1.0):
                raise ValueError("Value must be from 0 to 1")
            newValue = value
        except:
            print("Value must be from 0 to 1")
        self._displayReal(widget, newValue)
        return newValue

    def _displayVector(self, widget, values, numberFormat = '{:.4g}'):
        '''
        Display real vector values in a widget
        '''
        newText = ", ".join(numberFormat.format(value) for value in values)
        widget.setText(newText)

    def _parseVector3(self, widget):
        '''
        Return real vector from comma separated text in line edit widget
        '''
        text = widget.text()
        values = [float(value) for value in text.split(',')]
        if len(values) != 3:
            raise ValueError('Not 3 values')
        return values

    def _setupUi(self):
        self._ui.toolBox.setCurrentIndex(0)
        self._alignSettingsDisplay()
        self._fitSettingsDisplay()

    def _alignSettingsDisplay(self):
        self._displayReal(self._ui.alignScaleLineEdit, self._model.getAlignScale())
        self._displayVector(self._ui.alignRotationLineEdit, self._model.getAlignEulerAngles())
        self._displayVector(self._ui.alignOffsetLineEdit, self._model.getAlignOffset())
        self._ui.alignMirrorCheckBox.setCheckState(
            QtCore.Qt.Checked if self._model.isAlignMirror() else QtCore.Qt.Unchecked)

    def _fitSettingsDisplay(self):
        self._displayReal(self._ui.filterTopErrorProportionLineEdit, self._model.getFilterTopErrorProportion())
        self._displayReal(self._ui.filterNonNormalProjectionLimitLineEdit, self._model.getFilterNonNormalProjectionLimit())
        self._displayReal(self._ui.fitStrainPenaltyLineEdit, self._model.getFitStrainPenalty())
        self._displayReal(self._ui.fitCurvaturePenaltyLineEdit, self._model.getFitCurvaturePenalty())
        self._displayReal(self._ui.fitEdgeDiscontinuityPenaltyLineEdit, self._model.getFitEdgeDiscontinuityPenalty())
        self._ui.fitMaxIterationsSpinBox.setValue(self._model.getFitMaxIterations())

    def registerDoneExecution(self, callback):
        self._callback = callback

    def _doneButtonClicked(self):
        self._model.setStatePostAlign() # ensure model is transformed; does nothing if not in align tab
        self._model.writeOutputModel()
        #sceneviewer = self._ui.sceneviewerWidget.getSceneviewer()
        #sceneviewer.setScene(Scene())
        self._ui.dockWidget.setFloating(False)
        self._callback()

    def _viewAllButtonClicked(self):
        self._ui.sceneviewerWidget.viewAll()

    def _toolBoxPageChange(self, page):
        if page == 0:
            self._model.load()
            self._model.setStateAlign()
        else:
            self._model.setStatePostAlign()

    def _alignLoadButtonClicked(self):
        self._model.loadAlignSettings()

    def _alignSaveButtonClicked(self):
        self._model.saveAlignSettings()

    def _alignScaleEntered(self):
        self._model.setAlignScale(self._parseRealNonNegative(self._ui.alignScaleLineEdit, self._model.getAlignScale()))

    def _alignRotationEntered(self):
        try:
            eulerAngles = self._parseVector3(self._ui.alignRotationLineEdit)
            self._model.setAlignEulerAngles(eulerAngles)
        except:
            print("Invalid model rotation Euler angles entered")
            self._alignSettingsDisplay()

    def _alignOffsetEntered(self):
        try:
            offset = self._parseVector3(self._ui.alignOffsetLineEdit)
            self._model.setAlignOffset(offset)
        except:
            print("Invalid model offset entered")
            self._alignSettingsDisplay()

    def _alignMirrorClicked(self):
        state = self._ui.alignMirrorCheckBox.checkState()
        self._model.setAlignMirror(state == QtCore.Qt.Checked)

    def _alignResetButtonClicked(self):
        self._model.resetAlignment()

    def _alignAutoCentreButtonClicked(self):
        self._model.autoCentreModelOnData()

    def _projectClearButtonClicked(self):
        self._model.clearDataProjections()

    def _projectPointsButtonClicked(self):
        self._model.calculateDataProjections()

    def _filterTopErrorClicked(self):
        self._model.filterTopError()

    def _filterTopErrorProportionEntered(self):
        self._model.setFilterTopErrorProportion(self._parseRealZeroToOne(self._ui.filterTopErrorProportionLineEdit, self._model.getFilterTopErrorProportion()))

    def _filterNonNormalClicked(self):
        self._model.filterNonNormal()

    def _filterNonNormalProjectionLimitEntered(self):
        self._model.setFilterNonNormalProjectionLimit(self._parseRealZeroToOne(self._ui.filterNonNormalProjectionLimitLineEdit, self._model.getFilterNonNormalProjectionLimit()))

    def _fitLoadButtonClicked(self):
        self._model.loadFitSettings()

    def _fitSaveButtonClicked(self):
        self._model.saveFitSettings()

    def _fitStrainPenaltyEntered(self):
        self._model.setFitStrainPenalty(self._parseRealNonNegative(self._ui.fitStrainPenaltyLineEdit, self._model.getFitStrainPenalty()))

    def _fitCurvaturePenaltyEntered(self):
        self._model.setFitCurvaturePenalty(self._parseRealNonNegative(self._ui.fitCurvaturePenaltyLineEdit, self._model.getFitCurvaturePenalty()))

    def _fitEdgeDiscontinuityPenaltyEntered(self):
        self._model.setFitEdgeDiscontinuityPenalty(self._parseRealNonNegative(self._ui.fitEdgeDiscontinuityPenaltyLineEdit, self._model.getFitEdgeDiscontinuityPenalty()))

    def _fitMaxIterationsValueChanged(self, value):
        self._model.setFitMaxIterations(value)

    def _fitPerformButtonClicked(self):
        self._model.fit()
