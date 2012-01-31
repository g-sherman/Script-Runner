# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_scriptrunner.ui'
#
# Created: Mon Jan 30 05:56:35 2012
#      by: PyQt4 UI code generator 4.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ScriptRunner(object):
    def setupUi(self, ScriptRunner):
        ScriptRunner.setObjectName(_fromUtf8("ScriptRunner"))
        ScriptRunner.resize(616, 411)
        self.gridLayout = QtGui.QGridLayout(ScriptRunner)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(ScriptRunner)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 32))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 32))
        self.frame.setBaseSize(QtCore.QSize(0, 32))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 2)
        self.listScripts = QtGui.QListWidget(ScriptRunner)
        self.listScripts.setMaximumSize(QtCore.QSize(250, 16777215))
        self.listScripts.setObjectName(_fromUtf8("listScripts"))
        self.gridLayout.addWidget(self.listScripts, 1, 0, 1, 1)
        self.textBrowser = QtGui.QTextBrowser(ScriptRunner)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout.addWidget(self.textBrowser, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushAdd = QtGui.QPushButton(ScriptRunner)
        self.pushAdd.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushAdd.setObjectName(_fromUtf8("pushAdd"))
        self.horizontalLayout_2.addWidget(self.pushAdd)
        self.pushRemove = QtGui.QPushButton(ScriptRunner)
        self.pushRemove.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushRemove.setObjectName(_fromUtf8("pushRemove"))
        self.horizontalLayout_2.addWidget(self.pushRemove)
        spacerItem = QtGui.QSpacerItem(268, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushBtnRun = QtGui.QPushButton(ScriptRunner)
        self.pushBtnRun.setObjectName(_fromUtf8("pushBtnRun"))
        self.horizontalLayout_2.addWidget(self.pushBtnRun)
        self.pushBtnClose = QtGui.QPushButton(ScriptRunner)
        self.pushBtnClose.setObjectName(_fromUtf8("pushBtnClose"))
        self.horizontalLayout_2.addWidget(self.pushBtnClose)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)
        self.lblStatus = QtGui.QLabel(ScriptRunner)
        self.lblStatus.setMinimumSize(QtCore.QSize(31, 22))
        self.lblStatus.setFrameShape(QtGui.QFrame.NoFrame)
        self.lblStatus.setText(_fromUtf8(""))
        self.lblStatus.setObjectName(_fromUtf8("lblStatus"))
        self.gridLayout.addWidget(self.lblStatus, 3, 0, 1, 2)

        self.retranslateUi(ScriptRunner)
        QtCore.QObject.connect(self.pushBtnClose, QtCore.SIGNAL(_fromUtf8("clicked()")), ScriptRunner.reject)
        QtCore.QMetaObject.connectSlotsByName(ScriptRunner)

    def retranslateUi(self, ScriptRunner):
        ScriptRunner.setWindowTitle(QtGui.QApplication.translate("ScriptRunner", "ScriptRunner", None, QtGui.QApplication.UnicodeUTF8))
        self.pushAdd.setText(QtGui.QApplication.translate("ScriptRunner", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.pushRemove.setText(QtGui.QApplication.translate("ScriptRunner", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.pushBtnRun.setText(QtGui.QApplication.translate("ScriptRunner", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.pushBtnClose.setText(QtGui.QApplication.translate("ScriptRunner", "Close", None, QtGui.QApplication.UnicodeUTF8))

