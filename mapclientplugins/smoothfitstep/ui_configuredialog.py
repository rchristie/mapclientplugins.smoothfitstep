# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapclientplugins\smoothfitstep\qt\configuredialog.ui'
#
# Created: Tue Jul 16 11:41:45 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        ConfigureDialog.setObjectName("ConfigureDialog")
        ConfigureDialog.resize(444, 303)
        self.gridLayout = QtGui.QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.configGroupBox = QtGui.QGroupBox(ConfigureDialog)
        self.configGroupBox.setTitle("")
        self.configGroupBox.setObjectName("configGroupBox")
        self.formLayout = QtGui.QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName("formLayout")
        self.label0 = QtGui.QLabel(self.configGroupBox)
        self.label0.setObjectName("label0")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label0)
        self.lineEdit0 = QtGui.QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName("lineEdit0")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit0)
        self.enableSettingsSaveCheckBox = QtGui.QCheckBox(self.configGroupBox)
        self.enableSettingsSaveCheckBox.setObjectName("enableSettingsSaveCheckBox")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.enableSettingsSaveCheckBox)
        self.loadPreviousSolutionCheckBox = QtGui.QCheckBox(self.configGroupBox)
        self.loadPreviousSolutionCheckBox.setEnabled(False)
        self.loadPreviousSolutionCheckBox.setObjectName("loadPreviousSolutionCheckBox")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.loadPreviousSolutionCheckBox)
        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(ConfigureDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ConfigureDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ConfigureDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigureDialog)

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QtGui.QApplication.translate("ConfigureDialog", "ConfigureDialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label0.setText(QtGui.QApplication.translate("ConfigureDialog", "identifier:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.enableSettingsSaveCheckBox.setText(QtGui.QApplication.translate("ConfigureDialog", "Enable Settings Save", None, QtGui.QApplication.UnicodeUTF8))
        self.loadPreviousSolutionCheckBox.setText(QtGui.QApplication.translate("ConfigureDialog", "Load previous solution", None, QtGui.QApplication.UnicodeUTF8))

