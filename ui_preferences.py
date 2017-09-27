# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_preferences.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PrefsDialog(object):
    def setupUi(self, PrefsDialog):
        PrefsDialog.setObjectName("PrefsDialog")
        PrefsDialog.resize(547, 354)
        self.gridLayout_4 = QtWidgets.QGridLayout(PrefsDialog)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(PrefsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cbAutoDisplay = QtWidgets.QCheckBox(self.groupBox)
        self.cbAutoDisplay.setObjectName("cbAutoDisplay")
        self.gridLayout_2.addWidget(self.cbAutoDisplay, 0, 0, 1, 1)
        self.cbCustomEditor = QtWidgets.QCheckBox(self.groupBox)
        self.cbCustomEditor.setObjectName("cbCustomEditor")
        self.gridLayout_2.addWidget(self.cbCustomEditor, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.leCustomEditorPath = QtWidgets.QLineEdit(self.groupBox)
        self.leCustomEditorPath.setMinimumSize(QtCore.QSize(400, 0))
        self.leCustomEditorPath.setObjectName("leCustomEditorPath")
        self.horizontalLayout.addWidget(self.leCustomEditorPath)
        self.tbSetEditorPath = QtWidgets.QToolButton(self.groupBox)
        self.tbSetEditorPath.setObjectName("tbSetEditorPath")
        self.horizontalLayout.addWidget(self.tbSetEditorPath)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBoxOutput = QtWidgets.QGroupBox(PrefsDialog)
        self.groupBoxOutput.setObjectName("groupBoxOutput")
        self.layoutWidget = QtWidgets.QWidget(self.groupBoxOutput)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 120, 433, 58))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.leLogDirectory = QtWidgets.QLineEdit(self.layoutWidget)
        self.leLogDirectory.setMinimumSize(QtCore.QSize(250, 0))
        self.leLogDirectory.setObjectName("leLogDirectory")
        self.gridLayout.addWidget(self.leLogDirectory, 0, 2, 1, 1)
        self.tbSetLogDirectory = QtWidgets.QToolButton(self.layoutWidget)
        self.tbSetLogDirectory.setObjectName("tbSetLogDirectory")
        self.gridLayout.addWidget(self.tbSetLogDirectory, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.cbOverwriteLogFile = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbOverwriteLogFile.setObjectName("cbOverwriteLogFile")
        self.gridLayout.addWidget(self.cbOverwriteLogFile, 1, 1, 1, 2)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBoxOutput)
        self.layoutWidget1.setGeometry(QtCore.QRect(8, 40, 352, 80))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cbShowConsole = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbShowConsole.setObjectName("cbShowConsole")
        self.gridLayout_3.addWidget(self.cbShowConsole, 0, 0, 1, 1)
        self.cbClearConsole = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbClearConsole.setMinimumSize(QtCore.QSize(350, 0))
        self.cbClearConsole.setObjectName("cbClearConsole")
        self.gridLayout_3.addWidget(self.cbClearConsole, 1, 0, 1, 1)
        self.cbLogToDisk = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cbLogToDisk.setObjectName("cbLogToDisk")
        self.gridLayout_3.addWidget(self.cbLogToDisk, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBoxOutput, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(PrefsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_4.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(PrefsDialog)
        self.buttonBox.accepted.connect(PrefsDialog.accept)
        self.buttonBox.rejected.connect(PrefsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PrefsDialog)
        PrefsDialog.setTabOrder(self.cbClearConsole, self.cbLogToDisk)
        PrefsDialog.setTabOrder(self.cbLogToDisk, self.leLogDirectory)
        PrefsDialog.setTabOrder(self.leLogDirectory, self.tbSetLogDirectory)
        PrefsDialog.setTabOrder(self.tbSetLogDirectory, self.buttonBox)

    def retranslateUi(self, PrefsDialog):
        _translate = QtCore.QCoreApplication.translate
        PrefsDialog.setWindowTitle(_translate("PrefsDialog", "Script Runner Preferences"))
        self.groupBox.setTitle(_translate("PrefsDialog", "General Options"))
        self.cbAutoDisplay.setText(_translate("PrefsDialog", "Automatically display info/source when a script is selected from the list"))
        self.cbCustomEditor.setToolTip(_translate("PrefsDialog", "Application to use for editing scripts. If not specified, the system default will be used."))
        self.cbCustomEditor.setText(_translate("PrefsDialog", "Edit scripts using:"))
        self.leCustomEditorPath.setToolTip(_translate("PrefsDialog", "Full path to your editor application"))
        self.leCustomEditorPath.setPlaceholderText(_translate("PrefsDialog", "Full path to your edtior"))
        self.tbSetEditorPath.setText(_translate("PrefsDialog", "..."))
        self.groupBoxOutput.setTitle(_translate("PrefsDialog", "Output and Logging"))
        self.label.setText(_translate("PrefsDialog", "Log directory"))
        self.tbSetLogDirectory.setText(_translate("PrefsDialog", "..."))
        self.cbOverwriteLogFile.setText(_translate("PrefsDialog", "Overwrite log file each time the script is run"))
        self.cbShowConsole.setText(_translate("PrefsDialog", "Show console at startup"))
        self.cbClearConsole.setText(_translate("PrefsDialog", "Clear console before running a script"))
        self.cbLogToDisk.setText(_translate("PrefsDialog", "Log script output to disk"))

