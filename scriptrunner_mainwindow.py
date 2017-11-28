"""
Import the UI and intialize it.

ScriptRunner - A QGIS plugin that runs scripts to automate QGIS tasks.

Date: 2012-01-27
Copyright: (C) 2012-2013 by GeoApt LLC
Email: gsherman@geoapt.com


This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

"""

from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QMainWindow

from .mainwindow import Ui_MainWindow


class ScriptRunnerMainWindow(QMainWindow):
    """
    This class initializes the main window for Script Runner
    """

    def __init__(self):
        """
        Set up the user interface from Designer.
        """
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.settings = QSettings()

    def closeEvent(self, event):
        self.settings.setValue("ScriptRunner/geometry", self.saveGeometry())

    def moveEvent(self, event):
        self.settings.setValue("ScriptRunner/geometry", self.saveGeometry())
