# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_traceback.ui'
#
# Created: Thu Mar 14 11:14:12 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TracebackDialog(object):
    def setupUi(self, TracebackDialog):
        TracebackDialog.setObjectName(_fromUtf8("TracebackDialog"))
        TracebackDialog.resize(516, 323)
        self.gridLayout = QtGui.QGridLayout(TracebackDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.teTraceback = QtGui.QTextEdit(TracebackDialog)
        self.teTraceback.setReadOnly(True)
        self.teTraceback.setObjectName(_fromUtf8("teTraceback"))
        self.gridLayout.addWidget(self.teTraceback, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(TracebackDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(TracebackDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TracebackDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TracebackDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TracebackDialog)

    def retranslateUi(self, TracebackDialog):
        TracebackDialog.setWindowTitle(QtGui.QApplication.translate("TracebackDialog", "Script Runner Traceback", None, QtGui.QApplication.UnicodeUTF8))

