# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'smoothfitwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from opencmiss.zincwidgets.alignmentsceneviewerwidget import AlignmentSceneviewerWidget


class Ui_SmoothfitWidget(object):
    def setupUi(self, SmoothfitWidget):
        if not SmoothfitWidget.objectName():
            SmoothfitWidget.setObjectName(u"SmoothfitWidget")
        SmoothfitWidget.resize(1112, 1046)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SmoothfitWidget.sizePolicy().hasHeightForWidth())
        SmoothfitWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(SmoothfitWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.dockWidget = QDockWidget(SmoothfitWidget)
        self.dockWidget.setObjectName(u"dockWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy1)
        self.dockWidget.setMinimumSize(QSize(574, 183))
        self.dockWidget.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        sizePolicy1.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.dockWidgetContents)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy2)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 572, 1018))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.toolBox = QToolBox(self.scrollAreaWidgetContents)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy1.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy1)
        self.toolBox.setStyleSheet(u"QToolBox::tab {\n"
"         background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                     stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"         border-radius: 5px;\n"
"         color: black;\n"
"     }\n"
"\n"
"     QToolBox::tab:selected { /* italicize selected tabs */\n"
"         font: bold;\n"
"         color: black;\n"
"     }\n"
"QToolBox {\n"
"    padding : 0\n"
"}")
        self.alignPage = QWidget()
        self.alignPage.setObjectName(u"alignPage")
        self.alignPage.setGeometry(QRect(0, 0, 568, 924))
        sizePolicy1.setHeightForWidth(self.alignPage.sizePolicy().hasHeightForWidth())
        self.alignPage.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.alignPage)
        self.verticalLayout_5.setSpacing(7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 3, 0, 3)
        self.alignSettingsGroupBox = QGroupBox(self.alignPage)
        self.alignSettingsGroupBox.setObjectName(u"alignSettingsGroupBox")
        self.verticalLayout_7 = QVBoxLayout(self.alignSettingsGroupBox)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.alignLoadSaveWidgets = QWidget(self.alignSettingsGroupBox)
        self.alignLoadSaveWidgets.setObjectName(u"alignLoadSaveWidgets")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.alignLoadSaveWidgets.sizePolicy().hasHeightForWidth())
        self.alignLoadSaveWidgets.setSizePolicy(sizePolicy3)
        self.gridLayout = QGridLayout(self.alignLoadSaveWidgets)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.alignSaveButton = QPushButton(self.alignLoadSaveWidgets)
        self.alignSaveButton.setObjectName(u"alignSaveButton")
        self.alignSaveButton.setEnabled(True)

        self.gridLayout.addWidget(self.alignSaveButton, 0, 1, 1, 1)

        self.alignLoadButton = QPushButton(self.alignLoadSaveWidgets)
        self.alignLoadButton.setObjectName(u"alignLoadButton")
        self.alignLoadButton.setEnabled(True)

        self.gridLayout.addWidget(self.alignLoadButton, 0, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 2)

        self.verticalLayout_7.addWidget(self.alignLoadSaveWidgets)

        self.alignScaleWidgets = QWidget(self.alignSettingsGroupBox)
        self.alignScaleWidgets.setObjectName(u"alignScaleWidgets")
        sizePolicy3.setHeightForWidth(self.alignScaleWidgets.sizePolicy().hasHeightForWidth())
        self.alignScaleWidgets.setSizePolicy(sizePolicy3)
        self.formLayout = QFormLayout(self.alignScaleWidgets)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(3)
        self.formLayout.setVerticalSpacing(3)
        self.formLayout.setContentsMargins(3, 3, 3, 3)
        self.alignScaleLabel = QLabel(self.alignScaleWidgets)
        self.alignScaleLabel.setObjectName(u"alignScaleLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.alignScaleLabel)

        self.alignScaleLineEdit = QLineEdit(self.alignScaleWidgets)
        self.alignScaleLineEdit.setObjectName(u"alignScaleLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.alignScaleLineEdit)

        self.alignRotationLabel = QLabel(self.alignScaleWidgets)
        self.alignRotationLabel.setObjectName(u"alignRotationLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.alignRotationLabel)

        self.alignRotationLineEdit = QLineEdit(self.alignScaleWidgets)
        self.alignRotationLineEdit.setObjectName(u"alignRotationLineEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.alignRotationLineEdit)

        self.alignOffsetLabel = QLabel(self.alignScaleWidgets)
        self.alignOffsetLabel.setObjectName(u"alignOffsetLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.alignOffsetLabel)

        self.alignOffsetLineEdit = QLineEdit(self.alignScaleWidgets)
        self.alignOffsetLineEdit.setObjectName(u"alignOffsetLineEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.alignOffsetLineEdit)

        self.alignMirrorCheckBox = QCheckBox(self.alignScaleWidgets)
        self.alignMirrorCheckBox.setObjectName(u"alignMirrorCheckBox")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.alignMirrorCheckBox)


        self.verticalLayout_7.addWidget(self.alignScaleWidgets)


        self.verticalLayout_5.addWidget(self.alignSettingsGroupBox)

        self.alignResetButton = QPushButton(self.alignPage)
        self.alignResetButton.setObjectName(u"alignResetButton")

        self.verticalLayout_5.addWidget(self.alignResetButton)

        self.alignAutoCentreButton = QPushButton(self.alignPage)
        self.alignAutoCentreButton.setObjectName(u"alignAutoCentreButton")

        self.verticalLayout_5.addWidget(self.alignAutoCentreButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.toolBox.addItem(self.alignPage, u"Align")
        self.fitPage = QWidget()
        self.fitPage.setObjectName(u"fitPage")
        self.fitPage.setGeometry(QRect(0, 0, 568, 924))
        sizePolicy1.setHeightForWidth(self.fitPage.sizePolicy().hasHeightForWidth())
        self.fitPage.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.fitPage)
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 3, 0, 3)
        self.groupBoxProjectData = QGroupBox(self.fitPage)
        self.groupBoxProjectData.setObjectName(u"groupBoxProjectData")
        self.gridLayout_4 = QGridLayout(self.groupBoxProjectData)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(3, 3, 3, 3)
        self.projectPointsButton = QPushButton(self.groupBoxProjectData)
        self.projectPointsButton.setObjectName(u"projectPointsButton")

        self.gridLayout_4.addWidget(self.projectPointsButton, 0, 0, 1, 1)

        self.projectClearButton = QPushButton(self.groupBoxProjectData)
        self.projectClearButton.setObjectName(u"projectClearButton")

        self.gridLayout_4.addWidget(self.projectClearButton, 0, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBoxProjectData)

        self.filterDataGroupBox = QGroupBox(self.fitPage)
        self.filterDataGroupBox.setObjectName(u"filterDataGroupBox")
        self.gridLayout_3 = QGridLayout(self.filterDataGroupBox)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(3, 3, 3, 3)
        self.filterTopErrorProportionLineEdit = QLineEdit(self.filterDataGroupBox)
        self.filterTopErrorProportionLineEdit.setObjectName(u"filterTopErrorProportionLineEdit")

        self.gridLayout_3.addWidget(self.filterTopErrorProportionLineEdit, 0, 2, 1, 1)

        self.filterNonNormalPushButton = QPushButton(self.filterDataGroupBox)
        self.filterNonNormalPushButton.setObjectName(u"filterNonNormalPushButton")

        self.gridLayout_3.addWidget(self.filterNonNormalPushButton, 2, 0, 1, 1)

        self.filterNonNormalProjectionLimitLabel = QLabel(self.filterDataGroupBox)
        self.filterNonNormalProjectionLimitLabel.setObjectName(u"filterNonNormalProjectionLimitLabel")

        self.gridLayout_3.addWidget(self.filterNonNormalProjectionLimitLabel, 2, 1, 1, 1)

        self.filterNonNormalProjectionLimitLineEdit = QLineEdit(self.filterDataGroupBox)
        self.filterNonNormalProjectionLimitLineEdit.setObjectName(u"filterNonNormalProjectionLimitLineEdit")

        self.gridLayout_3.addWidget(self.filterNonNormalProjectionLimitLineEdit, 2, 2, 1, 1)

        self.filterTopErrorPushButton = QPushButton(self.filterDataGroupBox)
        self.filterTopErrorPushButton.setObjectName(u"filterTopErrorPushButton")

        self.gridLayout_3.addWidget(self.filterTopErrorPushButton, 0, 0, 1, 1)

        self.filterTopErrorProportionLabel = QLabel(self.filterDataGroupBox)
        self.filterTopErrorProportionLabel.setObjectName(u"filterTopErrorProportionLabel")

        self.gridLayout_3.addWidget(self.filterTopErrorProportionLabel, 0, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.filterDataGroupBox)

        self.fitSettingsGroupBox = QGroupBox(self.fitPage)
        self.fitSettingsGroupBox.setObjectName(u"fitSettingsGroupBox")
        sizePolicy.setHeightForWidth(self.fitSettingsGroupBox.sizePolicy().hasHeightForWidth())
        self.fitSettingsGroupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.fitSettingsGroupBox)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.fitSettingsLoadSaveWidgets = QWidget(self.fitSettingsGroupBox)
        self.fitSettingsLoadSaveWidgets.setObjectName(u"fitSettingsLoadSaveWidgets")
        sizePolicy3.setHeightForWidth(self.fitSettingsLoadSaveWidgets.sizePolicy().hasHeightForWidth())
        self.fitSettingsLoadSaveWidgets.setSizePolicy(sizePolicy3)
        self.gridLayout_2 = QGridLayout(self.fitSettingsLoadSaveWidgets)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fitLoadButton = QPushButton(self.fitSettingsLoadSaveWidgets)
        self.fitLoadButton.setObjectName(u"fitLoadButton")
        self.fitLoadButton.setEnabled(True)

        self.gridLayout_2.addWidget(self.fitLoadButton, 0, 0, 1, 1)

        self.fitSaveButton = QPushButton(self.fitSettingsLoadSaveWidgets)
        self.fitSaveButton.setObjectName(u"fitSaveButton")
        self.fitSaveButton.setEnabled(True)

        self.gridLayout_2.addWidget(self.fitSaveButton, 0, 1, 1, 1)

        self.gridLayout_2.setRowStretch(0, 2)

        self.verticalLayout_6.addWidget(self.fitSettingsLoadSaveWidgets)

        self.fitSettingsWidget = QWidget(self.fitSettingsGroupBox)
        self.fitSettingsWidget.setObjectName(u"fitSettingsWidget")
        self.formLayout_2 = QFormLayout(self.fitSettingsWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setVerticalSpacing(3)
        self.formLayout_2.setContentsMargins(0, 3, 0, 3)
        self.fitStrainPenaltyLabel = QLabel(self.fitSettingsWidget)
        self.fitStrainPenaltyLabel.setObjectName(u"fitStrainPenaltyLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.fitStrainPenaltyLabel)

        self.fitStrainPenaltyLineEdit = QLineEdit(self.fitSettingsWidget)
        self.fitStrainPenaltyLineEdit.setObjectName(u"fitStrainPenaltyLineEdit")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.fitStrainPenaltyLineEdit)

        self.fitPerformButton = QPushButton(self.fitSettingsWidget)
        self.fitPerformButton.setObjectName(u"fitPerformButton")

        self.formLayout_2.setWidget(6, QFormLayout.SpanningRole, self.fitPerformButton)

        self.fitMaxIterationsLabel = QLabel(self.fitSettingsWidget)
        self.fitMaxIterationsLabel.setObjectName(u"fitMaxIterationsLabel")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.fitMaxIterationsLabel)

        self.fitEdgeDiscontinuityPenaltyLabel = QLabel(self.fitSettingsWidget)
        self.fitEdgeDiscontinuityPenaltyLabel.setObjectName(u"fitEdgeDiscontinuityPenaltyLabel")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.fitEdgeDiscontinuityPenaltyLabel)

        self.fitEdgeDiscontinuityPenaltyLineEdit = QLineEdit(self.fitSettingsWidget)
        self.fitEdgeDiscontinuityPenaltyLineEdit.setObjectName(u"fitEdgeDiscontinuityPenaltyLineEdit")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.fitEdgeDiscontinuityPenaltyLineEdit)

        self.fitMaxIterationsSpinBox = QSpinBox(self.fitSettingsWidget)
        self.fitMaxIterationsSpinBox.setObjectName(u"fitMaxIterationsSpinBox")
        self.fitMaxIterationsSpinBox.setMinimum(1)
        self.fitMaxIterationsSpinBox.setMaximum(100)
        self.fitMaxIterationsSpinBox.setValue(1)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.fitMaxIterationsSpinBox)

        self.fitCurvaturePenaltyLineEdit = QLineEdit(self.fitSettingsWidget)
        self.fitCurvaturePenaltyLineEdit.setObjectName(u"fitCurvaturePenaltyLineEdit")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.fitCurvaturePenaltyLineEdit)

        self.fitCurvaturePenaltyLabel = QLabel(self.fitSettingsWidget)
        self.fitCurvaturePenaltyLabel.setObjectName(u"fitCurvaturePenaltyLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.fitCurvaturePenaltyLabel)


        self.verticalLayout_6.addWidget(self.fitSettingsWidget)


        self.verticalLayout_4.addWidget(self.fitSettingsGroupBox)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.toolBox.addItem(self.fitPage, u"Fit")

        self.verticalLayout_3.addWidget(self.toolBox)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.viewAllButton = QPushButton(self.frame)
        self.viewAllButton.setObjectName(u"viewAllButton")

        self.horizontalLayout_2.addWidget(self.viewAllButton)

        self.doneButton = QPushButton(self.frame)
        self.doneButton.setObjectName(u"doneButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.doneButton.sizePolicy().hasHeightForWidth())
        self.doneButton.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.doneButton)


        self.verticalLayout_3.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.horizontalLayout.addWidget(self.dockWidget)

        self.sceneviewerWidget = AlignmentSceneviewerWidget(SmoothfitWidget)
        self.sceneviewerWidget.setObjectName(u"sceneviewerWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.sceneviewerWidget.sizePolicy().hasHeightForWidth())
        self.sceneviewerWidget.setSizePolicy(sizePolicy5)

        self.horizontalLayout.addWidget(self.sceneviewerWidget)


        self.retranslateUi(SmoothfitWidget)

        self.toolBox.setCurrentIndex(1)
        self.toolBox.layout().setSpacing(2)


        QMetaObject.connectSlotsByName(SmoothfitWidget)
    # setupUi

    def retranslateUi(self, SmoothfitWidget):
        SmoothfitWidget.setWindowTitle(QCoreApplication.translate("SmoothfitWidget", u"Form", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("SmoothfitWidget", u"Fitting Steps", None))
        self.alignSettingsGroupBox.setTitle(QCoreApplication.translate("SmoothfitWidget", u"Alignment Settings", None))
#if QT_CONFIG(tooltip)
        self.alignSaveButton.setToolTip(QCoreApplication.translate("SmoothfitWidget", u"Save alignment settings for recall later or when next run", None))
#endif // QT_CONFIG(tooltip)
        self.alignSaveButton.setText(QCoreApplication.translate("SmoothfitWidget", u"Save Settings", None))
#if QT_CONFIG(tooltip)
        self.alignLoadButton.setToolTip(QCoreApplication.translate("SmoothfitWidget", u"Load pre-saved alignment settings", None))
#endif // QT_CONFIG(tooltip)
        self.alignLoadButton.setText(QCoreApplication.translate("SmoothfitWidget", u"Load Settings", None))
        self.alignScaleLabel.setText(QCoreApplication.translate("SmoothfitWidget", u"Scale:", None))
#if QT_CONFIG(tooltip)
        self.alignScaleLineEdit.setToolTip(QCoreApplication.translate("SmoothfitWidget", u"Scaling of model, where 1.0 is original size", None))
#endif // QT_CONFIG(tooltip)
        self.alignRotationLabel.setText(QCoreApplication.translate("SmoothfitWidget", u"Rotation:", None))
#if QT_CONFIG(tooltip)
        self.alignRotationLineEdit.setToolTip(QCoreApplication.translate("SmoothfitWidget", u"Rotation of the model as 3 Euler angles", None))
#endif // QT_CONFIG(tooltip)
        self.alignOffsetLabel.setText(QCoreApplication.translate("SmoothfitWidget", u"Offset:", None))
#if QT_CONFIG(tooltip)
        self.alignOffsetLineEdit.setToolTip(QCoreApplication.translate("SmoothfitWidget", u"Offset of the model in x, y ,z", None))
#endif // QT_CONFIG(tooltip)
        self.alignMirrorCheckBox.setText(QCoreApplication.translate("SmoothfitWidget", u"Mirror", None))
#if QT_CONFIG(tooltip)
        self.alignResetButton.setToolTip(QCoreApplication.translate("SmoothfitWidget", u"Reset the alignment settings", None))
#endif // QT_CONFIG(tooltip)
        self.alignResetButton.setText(QCoreApplication.translate("SmoothfitWidget", u"Reset", None))
#if QT_CONFIG(tooltip)
        self.alignAutoCentreButton.setToolTip(QCoreApplication.translate("SmoothfitWidget", u"Offset the model to the centre of the data points. May need to click View All afterwards.", None))
#endif // QT_CONFIG(tooltip)
        self.alignAutoCentreButton.setText(QCoreApplication.translate("SmoothfitWidget", u"Auto Centre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.alignPage), QCoreApplication.translate("SmoothfitWidget", u"Align", None))
        self.groupBoxProjectData.setTitle(QCoreApplication.translate("SmoothfitWidget", u"1. Projections", None))
#if QT_CONFIG(tooltip)
        self.projectPointsButton.setToolTip(QCoreApplication.translate("SmoothfitWidget", u"Project or re-project all active points to the nearest locations on the model surfaces", None))
#endif // QT_CONFIG(tooltip)
        self.projectPointsButton.setText(QCoreApplication.translate("SmoothfitWidget", u"Project Points", None))
#if QT_CONFIG(tooltip)
        self.projectClearButton.setToolTip(QCoreApplication.translate("SmoothfitWidget", u"Clear all projections and reset the active data points to include all", None))
#endif // QT_CONFIG(tooltip)
        self.projectClearButton.setText(QCoreApplication.translate("SmoothfitWidget", u"Reset", None))
        self.filterDataGroupBox.setTitle(QCoreApplication.translate("SmoothfitWidget", u"2. Filter data", None))
#if QT_CONFIG(tooltip)
        self.filterTopErrorProportionLineEdit.setToolTip(QCoreApplication.translate("SmoothfitWidget", u"Proportion of maximum error (0.0 to 1.0) used to filter data points", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.filterNonNormalPushButton.setToolTip(QCoreApplication.translate("SmoothfitWidget", u"Remove data points with projections whose dot product with the surface normal is less than the given limit (1.0 is perface alignment, 0.0 is orthogonal)", None))
#endif // QT_CONFIG(tooltip)
        self.filterNonNormalPushButton.setText(QCoreApplication.translate("SmoothfitWidget", u"Remove non-normal", None))
        self.filterNonNormalProjectionLimitLabel.setText(QCoreApplication.translate("SmoothfitWidget", u"Proj. Limit:", None))
#if QT_CONFIG(tooltip)
        self.filterNonNormalProjectionLimitLineEdit.setToolTip(QCoreApplication.translate("SmoothfitWidget", u"Minimum dot product for removing non-normal projections (<=1.0 where 1.0 is perfecly normal)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.filterTopErrorPushButton.setToolTip(QCoreApplication.translate("SmoothfitWidget", u"Remove data points with errors greater than the given proportion of the maximum error", None))
#endif // QT_CONFIG(tooltip)
        self.filterTopErrorPushButton.setText(QCoreApplication.translate("SmoothfitWidget", u"Remove top error", None))
        self.filterTopErrorProportionLabel.setText(QCoreApplication.translate("SmoothfitWidget", u"Proportion:", None))
        self.fitSettingsGroupBox.setTitle(QCoreApplication.translate("SmoothfitWidget", u"3. Fit", None))
#if QT_CONFIG(tooltip)
        self.fitLoadButton.setToolTip(QCoreApplication.translate("SmoothfitWidget", u"Load pre-saved fitting settings", None))
#endif // QT_CONFIG(tooltip)
        self.fitLoadButton.setText(QCoreApplication.translate("SmoothfitWidget", u"Load Settings", None))
#if QT_CONFIG(tooltip)
        self.fitSaveButton.setToolTip(QCoreApplication.translate("SmoothfitWidget", u"Save fit settings for recall later or when next run", None))
#endif // QT_CONFIG(tooltip)
        self.fitSaveButton.setText(QCoreApplication.translate("SmoothfitWidget", u"Save Settings", None))
        self.fitStrainPenaltyLabel.setText(QCoreApplication.translate("SmoothfitWidget", u"Strain Penalty:", None))
#if QT_CONFIG(tooltip)
        self.fitStrainPenaltyLineEdit.setToolTip(QCoreApplication.translate("SmoothfitWidget", u"Penalty factor for strains, typically << 1.0 e.g. 0.001", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.fitPerformButton.setToolTip(QCoreApplication.translate("SmoothfitWidget", u"Perform fitting up to at most the set number of iteratations", None))
#endif // QT_CONFIG(tooltip)
        self.fitPerformButton.setText(QCoreApplication.translate("SmoothfitWidget", u"Perform Fit", None))
        self.fitMaxIterationsLabel.setText(QCoreApplication.translate("SmoothfitWidget", u"Max. Iterations:", None))
        self.fitEdgeDiscontinuityPenaltyLabel.setText(QCoreApplication.translate("SmoothfitWidget", u"Edge Discontinuity Pen.:", None))
#if QT_CONFIG(tooltip)
        self.fitEdgeDiscontinuityPenaltyLineEdit.setToolTip(QCoreApplication.translate("SmoothfitWidget", u"Penalty factor for discontinuity between adjacent elements. Used only with non-C1 continuous coordinate fields", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.fitMaxIterationsSpinBox.setToolTip(QCoreApplication.translate("SmoothfitWidget", u"Maximum number of iterations to limit fit time if convergence is slow", None))
#endif // QT_CONFIG(tooltip)
        self.fitCurvaturePenaltyLabel.setText(QCoreApplication.translate("SmoothfitWidget", u"Curvature Penalty:", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.fitPage), QCoreApplication.translate("SmoothfitWidget", u"Fit", None))
#if QT_CONFIG(tooltip)
        self.viewAllButton.setToolTip(QCoreApplication.translate("SmoothfitWidget", u"Adjust the view to see the whole model", None))
#endif // QT_CONFIG(tooltip)
        self.viewAllButton.setText(QCoreApplication.translate("SmoothfitWidget", u"View All", None))
#if QT_CONFIG(tooltip)
        self.doneButton.setToolTip(QCoreApplication.translate("SmoothfitWidget", u"Finish this step", None))
#endif // QT_CONFIG(tooltip)
        self.doneButton.setText(QCoreApplication.translate("SmoothfitWidget", u"Done", None))
    # retranslateUi

