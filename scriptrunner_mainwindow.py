"""
/***************************************************************************
 ScriptRunnerDialog
                                 A QGIS plugin
 Run scripts to automate QGIS tasks
                             -------------------
        begin                : 2012-01-27
        copyright            : (C) 2012 by GeoApt LLC
        email                : gsherman@geoapt.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from mainwindow import Ui_MainWindow
# create the dialog for zoom to point
class ScriptRunnerMainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
