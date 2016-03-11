'''
Created on Jul 23, 2015

@author: Richard Christie
'''
from opencmiss.zinc.node import Node
from opencmiss.zinc.field import Field
from opencmiss.zinc.status import OK as ZINC_OK
from mapclientplugins.smoothfitstep.maths import vectorops

def transformCoordinates(field, rotationScale, offset, time = 0.0):
    '''
    Transform finite element field coordinates by matrix and offset, handling nodal derivatives and versions.
    Limited to nodal parameters, rectangular cartesian coordinates
    :param field: the coordinate field to transform
    :param rotationScale: square transformation matrix 2-D array with as many rows and columns as field components.
    :param offset: coordinates offset
    :return: True on success, otherwise false
    '''
    ncomp = field.getNumberOfComponents()
    if ((ncomp != 2) and (ncomp != 3)):
        print('zinc.transformCoordinates: field has invalid number of components')
        return False
    if (len(rotationScale) != ncomp) or (len(offset) != ncomp):
        print('zinc.transformCoordinates: invalid matrix number of columns or offset size')
        return False
    for matRow in rotationScale:
        if len(matRow) != ncomp:
            print('zinc.transformCoordinates: invalid matrix number of columns')
            return False
    if (field.getCoordinateSystemType() != Field.COORDINATE_SYSTEM_TYPE_RECTANGULAR_CARTESIAN):
        print('zinc.transformCoordinates: field is not rectangular cartesian')
        return False
    feField = field.castFiniteElement()
    if not feField.isValid():
        print('zinc.transformCoordinates: field is not finite element field type')
        return False
    success = True
    fm = field.getFieldmodule()
    fm.beginChange()
    cache = fm.createFieldcache()
    cache.setTime(time)
    nodes = fm.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_NODES)
    nodetemplate = nodes.createNodetemplate()
    nodeIter = nodes.createNodeiterator()
    node = nodeIter.next()
    while node.isValid():
        nodetemplate.defineFieldFromNode(feField, node)
        cache.setNode(node)
        for derivative in [Node.VALUE_LABEL_VALUE, Node.VALUE_LABEL_D_DS1, Node.VALUE_LABEL_D_DS2, Node.VALUE_LABEL_D2_DS1DS2,
                           Node.VALUE_LABEL_D_DS3, Node.VALUE_LABEL_D2_DS1DS3, Node.VALUE_LABEL_D2_DS2DS3, Node.VALUE_LABEL_D3_DS1DS2DS3]:
            versions = nodetemplate.getValueNumberOfVersions(feField, -1, derivative)
            for v in range(versions):
                result, values = feField.getNodeParameters(cache, -1, derivative, v + 1, ncomp)
                if result != ZINC_OK:
                    success = False
                else:
                    newValues = vectorops.matrixvectormult(rotationScale, values)
                    if derivative == Node.VALUE_LABEL_VALUE:
                        newValues = vectorops.add(newValues, offset)
                    result = feField.setNodeParameters(cache, -1, derivative, v + 1, newValues)
                    if result != ZINC_OK:
                        success = False
        node = nodeIter.next()
    fm.endChange()
    if not success:
        print('zinc.transformCoordinates: failed to get/set some values')
    return success
