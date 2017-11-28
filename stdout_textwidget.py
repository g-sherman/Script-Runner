"""
A custom QTextWidget to support writing stdout

ScriptRunner - A QGIS plugin that runs scripts to automate QGIS tasks.

Date: 2013-03-14
Copyright: (C) 2013 by GeoApt LLC
Email: gsherman@geoapt.com


This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

"""
import sys

from PyQt5.QtCore import Qt, pyqtSignal, QCoreApplication
from PyQt5.QtGui import QColor, QTextCursor
from PyQt5.QtWidgets import QTextEdit


class StdoutTextEdit(QTextEdit):
    """
    This class is the stdout widget for Script Runner
    """
    new_output = pyqtSignal(str)

    def __init__(self):
        """
        Set up the user interface from Designer.
        """
        QTextEdit.__init__(self)
        self.setPlainText("Script Runner %s\n" % "3.0.1")
        # cursor for the StdoutTextEdit
        self.cursor = QTextCursor(self.textCursor())
        self.setTextCursor(self.cursor)

    def write(self, text, warning=False):
        """ Write to the stdout widget"""
        cursor = QTextCursor(self.textCursor())
        cursor.movePosition(QTextCursor.End)
        self.setTextCursor(cursor)
        if warning:
            self.setTextColor(QColor(Qt.red))
            self.insertPlainText(text)
        else:
            self.insertPlainText(text)
        self.ensureCursorVisible()
        QCoreApplication.processEvents()
        sys.__stdout__.flush()
        self.new_output.emit(str(text))
