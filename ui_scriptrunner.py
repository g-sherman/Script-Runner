# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_scriptrunner.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ScriptRunner(object):
    def setupUi(self, ScriptRunner):
        ScriptRunner.setObjectName("ScriptRunner")
        ScriptRunner.resize(616, 411)
        self.gridLayout = QtWidgets.QGridLayout(ScriptRunner)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(ScriptRunner)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 32))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 32))
        self.frame.setBaseSize(QtCore.QSize(0, 32))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 2)
        self.listScripts = QtWidgets.QListWidget(ScriptRunner)
        self.listScripts.setMaximumSize(QtCore.QSize(250, 16777215))
        self.listScripts.setObjectName("listScripts")
        self.gridLayout.addWidget(self.listScripts, 1, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(ScriptRunner)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushAdd = QtWidgets.QPushButton(ScriptRunner)
        self.pushAdd.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushAdd.setObjectName("pushAdd")
        self.horizontalLayout_2.addWidget(self.pushAdd)
        self.pushRemove = QtWidgets.QPushButton(ScriptRunner)
        self.pushRemove.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushRemove.setObjectName("pushRemove")
        self.horizontalLayout_2.addWidget(self.pushRemove)
        spacerItem = QtWidgets.QSpacerItem(268, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushBtnRun = QtWidgets.QPushButton(ScriptRunner)
        self.pushBtnRun.setObjectName("pushBtnRun")
        self.horizontalLayout_2.addWidget(self.pushBtnRun)
        self.pushBtnClose = QtWidgets.QPushButton(ScriptRunner)
        self.pushBtnClose.setObjectName("pushBtnClose")
        self.horizontalLayout_2.addWidget(self.pushBtnClose)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)
        self.lblStatus = QtWidgets.QLabel(ScriptRunner)
        self.lblStatus.setMinimumSize(QtCore.QSize(31, 22))
        self.lblStatus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblStatus.setText("")
        self.lblStatus.setObjectName("lblStatus")
        self.gridLayout.addWidget(self.lblStatus, 3, 0, 1, 2)
        self.listScripts.raise_()
        self.textBrowser.raise_()
        self.pushAdd.raise_()
        self.pushRemove.raise_()
        self.pushBtnRun.raise_()
        self.pushBtnClose.raise_()
        self.lblStatus.raise_()
        self.frame.raise_()

        self.retranslateUi(ScriptRunner)
        self.pushBtnClose.clicked.connect(ScriptRunner.reject)
        QtCore.QMetaObject.connectSlotsByName(ScriptRunner)

    def retranslateUi(self, ScriptRunner):
        _translate = QtCore.QCoreApplication.translate
        ScriptRunner.setWindowTitle(_translate("ScriptRunner", "ScriptRunner"))
        self.pushAdd.setText(_translate("ScriptRunner", "+"))
        self.pushRemove.setText(_translate("ScriptRunner", "-"))
        self.pushBtnRun.setText(_translate("ScriptRunner", "Run"))
        self.pushBtnClose.setText(_translate("ScriptRunner", "Close"))

