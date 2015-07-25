'''
Created on July 15, 2015

@author: rchristie
'''
from PySide import QtCore
from math import sqrt
from mapclientplugins.smoothfitstep.maths import vectorops
from opencmiss.zincwidgets.sceneviewerwidget import SceneviewerWidget

class AlignmentSceneviewerWidget(SceneviewerWidget):
    '''
    classdocs
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(AlignmentSceneviewerWidget, self).__init__(parent)
        self._model = None
        self._active_button = QtCore.Qt.NoButton
        self._lastMousePos = None

    def setModel(self, model):
        self._model = model

    def mousePressEvent(self, event):
        if self._active_button != QtCore.Qt.NoButton:
            return
        if event.modifiers() & QtCore.Qt.CTRL:
            if self._model.isStateAlign():
                self._active_button = event.button()
                self._lastMousePos = [ event.x(), event.y() ]
        else:
            super(AlignmentSceneviewerWidget, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._lastMousePos is not None:
            pos = [ event.x(), event.y() ]
            delta = [ pos[0] - self._lastMousePos[0], pos[1] - self._lastMousePos[1] ]
            result, eye = self._sceneviewer.getEyePosition()
            result, lookat = self._sceneviewer.getLookatPosition()
            result, up = self._sceneviewer.getUpVector()
            lookatToEye = vectorops.sub(eye, lookat)
            eyeDistance = vectorops.magnitude(lookatToEye)
            front = vectorops.div(lookatToEye, eyeDistance)
            right = vectorops.cross(up, front)
            if self._active_button == QtCore.Qt.LeftButton:
                mag = vectorops.magnitude(delta)
                prop = vectorops.div(delta, mag)
                axis = vectorops.add(vectorops.mult(up, prop[0]), vectorops.mult(right, prop[1]))
                angle = mag*0.002
                self._model.rotateModel(axis, angle)
            elif self._active_button == QtCore.Qt.MiddleButton:
                result, l, r, b, t, near, far = self._sceneviewer.getViewingVolume()
                viewportWidth = self.width()
                viewportHeight = self.height()
                if viewportWidth > viewportHeight:
                    eyeScale = (t - b) / viewportHeight
                else:
                    eyeScale = (r - l) / viewportWidth
                offset = vectorops.add(vectorops.mult(right, eyeScale*delta[0]), vectorops.mult(up, -eyeScale*delta[1]))
                self._model.offsetModel(offset)
            elif self._active_button == QtCore.Qt.RightButton:
                factor = 1.0 + delta[1]*0.0005
                if factor < 0.9:
                    factor = 0.9
                self._model.scaleModel(factor)
            self._lastMousePos = pos
        else:
            super(AlignmentSceneviewerWidget, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self._lastMousePos is not None:
            pass
        else:
            super(AlignmentSceneviewerWidget, self).mouseReleaseEvent(event)
        self._active_button = QtCore.Qt.NoButton
        self._lastMousePos = None
