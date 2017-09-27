# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_traceback.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TracebackDialog(object):
    def setupUi(self, TracebackDialog):
        TracebackDialog.setObjectName("TracebackDialog")
        TracebackDialog.resize(516, 323)
        self.gridLayout = QtWidgets.QGridLayout(TracebackDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.teTraceback = QtWidgets.QTextEdit(TracebackDialog)
        self.teTraceback.setReadOnly(True)
        self.teTraceback.setObjectName("teTraceback")
        self.gridLayout.addWidget(self.teTraceback, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(TracebackDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(TracebackDialog)
        self.buttonBox.accepted.connect(TracebackDialog.accept)
        self.buttonBox.rejected.connect(TracebackDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TracebackDialog)

    def retranslateUi(self, TracebackDialog):
        _translate = QtCore.QCoreApplication.translate
        TracebackDialog.setWindowTitle(_translate("TracebackDialog", "Script Runner Traceback"))

