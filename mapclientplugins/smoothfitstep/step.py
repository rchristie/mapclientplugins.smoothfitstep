'''
MAP Client Plugin Step
'''
import os
import json

from PySide import QtGui

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.smoothfitstep.configuredialog import ConfigureDialog
from mapclientplugins.smoothfitstep.model.smoothfitmodel import SmoothfitModel
from mapclientplugins.smoothfitstep.view.smoothfitwidget import SmoothfitWidget


class smoothfitStep(WorkflowStepMountPoint):
    '''
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    '''

    def __init__(self, location):
        super(smoothfitStep, self).__init__('smoothfit', location)
        self._configured = False # A step cannot be executed until it has been configured.
        self._category = 'Fitting'
        # Add any other initialisation code here:
        self._icon =  QtGui.QImage(':/smoothfitstep/images/fitting.png')
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#zincmodel'))
        # Port data:
        self._inputZincModelFile = None # http://physiomeproject.org/workflow/1.0/rdf-schema#zincmodel
        self._inputZincPointCloudFile = None # http://physiomeproject.org/workflow/1.0/rdf-schema#pointcloud
        self._outputZincModel = None # http://physiomeproject.org/workflow/1.0/rdf-schema#zincmodel
        # Config:
        self._config = {}
        self._config['identifier'] = ''
        self._config['enable_settings_save'] = True
        self._view = None

    def execute(self):
        '''
        Kick off the execution of the step, in this case an interactive dialog.
        User invokes the _doneExecution() method when finished, via pushbutton.
        '''
        smoothfitModel = None
        if self._view is None:
            smoothfitModel = SmoothfitModel()
            smoothfitModel.setLocation(os.path.join(self._location, self._config['identifier']))
            self._view = SmoothfitWidget(smoothfitModel)
            self._view.registerDoneExecution(self._doneExecution)
        else:
            smoothfitModel = self._view.getModel()
            self._view.clear()
            smoothfitModel.clear()
        if self._inputZincModelFile is not None:
            smoothfitModel.setZincModelFile(self._inputZincModelFile)
        if self._inputZincPointCloudFile is not None:
            smoothfitModel.setZincPointCloudFile(self._inputZincPointCloudFile)
        self._view.initialise()
        self._view.setEnableSettingsSave(self._config['enable_settings_save'])
        self._setCurrentWidget(self._view)

    def setPortData(self, index, dataIn):
        '''
        Set inputs, called by mapclient framework.
        '''
        if index == 0:
            self._inputZincModelFile = dataIn # http://physiomeproject.org/workflow/1.0/rdf-schema#zincmodel
        elif index == 1:
            self._inputZincPointCloudFile = dataIn # http://physiomeproject.org/workflow/1.0/rdf-schema#zincpointcloud

    def getPortData(self, index):
        '''
        Get outputs, called by mapclient framework.
        '''
        return self._outputZincModel # http://physiomeproject.org/workflow/1.0/rdf-schema#zincmodel

    def configure(self):
        '''
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        '''
        dlg = ConfigureDialog()
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        '''
        The identifier is a string that must be unique within a workflow.
        '''
        return self._config['identifier']

    def setIdentifier(self, identifier):
        '''
        The framework will set the identifier for this step when it is loaded.
        '''
        self._config['identifier'] = identifier

    def serialize(self):
        '''
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        '''
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        '''
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.
        '''
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()


