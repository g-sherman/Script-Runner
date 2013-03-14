# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_preferences.ui'
#
# Created: Thu Mar 14 13:31:09 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PrefsDialog(object):
    def setupUi(self, PrefsDialog):
        PrefsDialog.setObjectName(_fromUtf8("PrefsDialog"))
        PrefsDialog.resize(554, 298)
        self.gridLayout_3 = QtGui.QGridLayout(PrefsDialog)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox = QtGui.QGroupBox(PrefsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.cbAutoDisplay = QtGui.QCheckBox(self.groupBox)
        self.cbAutoDisplay.setObjectName(_fromUtf8("cbAutoDisplay"))
        self.gridLayout_2.addWidget(self.cbAutoDisplay, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBoxOutput = QtGui.QGroupBox(PrefsDialog)
        self.groupBoxOutput.setObjectName(_fromUtf8("groupBoxOutput"))
        self.cbShowOutput = QtGui.QCheckBox(self.groupBoxOutput)
        self.cbShowOutput.setGeometry(QtCore.QRect(10, 30, 212, 20))
        self.cbShowOutput.setObjectName(_fromUtf8("cbShowOutput"))
        self.cbClearConsole = QtGui.QCheckBox(self.groupBoxOutput)
        self.cbClearConsole.setGeometry(QtCore.QRect(10, 51, 259, 20))
        self.cbClearConsole.setObjectName(_fromUtf8("cbClearConsole"))
        self.cbLogToDisk = QtGui.QCheckBox(self.groupBoxOutput)
        self.cbLogToDisk.setGeometry(QtCore.QRect(10, 72, 181, 20))
        self.cbLogToDisk.setObjectName(_fromUtf8("cbLogToDisk"))
        self.widget = QtGui.QWidget(self.groupBoxOutput)
        self.widget.setGeometry(QtCore.QRect(12, 98, 433, 58))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.leLogDirectory = QtGui.QLineEdit(self.widget)
        self.leLogDirectory.setMinimumSize(QtCore.QSize(250, 0))
        self.leLogDirectory.setObjectName(_fromUtf8("leLogDirectory"))
        self.gridLayout.addWidget(self.leLogDirectory, 0, 2, 1, 1)
        self.tbSetLogDirectory = QtGui.QToolButton(self.widget)
        self.tbSetLogDirectory.setObjectName(_fromUtf8("tbSetLogDirectory"))
        self.gridLayout.addWidget(self.tbSetLogDirectory, 0, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.cbOverwriteLogFile = QtGui.QCheckBox(self.widget)
        self.cbOverwriteLogFile.setObjectName(_fromUtf8("cbOverwriteLogFile"))
        self.gridLayout.addWidget(self.cbOverwriteLogFile, 1, 1, 1, 2)
        self.gridLayout_3.addWidget(self.groupBoxOutput, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(PrefsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_3.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(PrefsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PrefsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PrefsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PrefsDialog)
        PrefsDialog.setTabOrder(self.cbShowOutput, self.cbClearConsole)
        PrefsDialog.setTabOrder(self.cbClearConsole, self.cbLogToDisk)
        PrefsDialog.setTabOrder(self.cbLogToDisk, self.leLogDirectory)
        PrefsDialog.setTabOrder(self.leLogDirectory, self.tbSetLogDirectory)
        PrefsDialog.setTabOrder(self.tbSetLogDirectory, self.buttonBox)

    def retranslateUi(self, PrefsDialog):
        PrefsDialog.setWindowTitle(QtGui.QApplication.translate("PrefsDialog", "Script Runner Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("PrefsDialog", "General Options", None, QtGui.QApplication.UnicodeUTF8))
        self.cbAutoDisplay.setText(QtGui.QApplication.translate("PrefsDialog", "Automatically display info/source when a script is selected from the list", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxOutput.setTitle(QtGui.QApplication.translate("PrefsDialog", "Output and Logging", None, QtGui.QApplication.UnicodeUTF8))
        self.cbShowOutput.setText(QtGui.QApplication.translate("PrefsDialog", "Show script output in console", None, QtGui.QApplication.UnicodeUTF8))
        self.cbClearConsole.setText(QtGui.QApplication.translate("PrefsDialog", "Clear console before running a script", None, QtGui.QApplication.UnicodeUTF8))
        self.cbLogToDisk.setText(QtGui.QApplication.translate("PrefsDialog", "Log script output to disk", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PrefsDialog", "Log directory", None, QtGui.QApplication.UnicodeUTF8))
        self.tbSetLogDirectory.setText(QtGui.QApplication.translate("PrefsDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.cbOverwriteLogFile.setText(QtGui.QApplication.translate("PrefsDialog", "Overwrite log file each time the script is run", None, QtGui.QApplication.UnicodeUTF8))

