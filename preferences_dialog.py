"""
Import the Preferences UI and intialize it.

ScriptRunner - A QGIS plugin that runs scripts to automate QGIS tasks.

Date: 2013-03-14
Copyright: (C) 2013 by GeoApt LLC
Email: gsherman@geoapt.com


This program is free software; you can redistribute it and/or modify  
it under the terms of the GNU General Public License as published by  
the Free Software Foundation; either version 2 of the License, or     
(at your option) any later version.                                   
                                                                          
"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
from ui_preferences import Ui_PrefsDialog

class PreferencesDialog(QtGui.QDialog):
    """
    This class initializes the preferences dialog for Script Runner
    """

    def __init__(self):
        """
        Set up the user interface from Designer.
        """
        QtGui.QDialog.__init__(self)
        self.ui = Ui_PrefsDialog()
        self.ui.setupUi(self)

        # connect the OK button
        self.ui.buttonBox.accepted.connect(self.save_settings)
        # connect the set log directory button
        self.ui.tbSetLogDirectory.clicked.connect(self.set_log_dir)

        # connect the checkbox state change
        self.ui.cbShowOutput.stateChanged.connect(self.changed_show_output)
        self.ui.cbLogToDisk.stateChanged.connect(self.changed_log_to_disk)

        self.settings = QtCore.QSettings()
        self.restore_settings()

    def restore_settings(self):
        auto_display = self.settings.value("ScriptRunner/auto_display", True)
        self.ui.cbAutoDisplay.setChecked(auto_display.toBool())
        clear_console = self.settings.value("ScriptRunner/clear_console", True)
        self.ui.cbClearConsole.setChecked(clear_console.toBool())
        display_in_console = self.settings.value("ScriptRunner/display_in_console", True)
        self.ui.cbShowOutput.setChecked(display_in_console.toBool())
        log_output = self.settings.value("ScriptRunner/log_output_to_disk", False)
        self.ui.cbLogToDisk.setChecked(log_output.toBool())

        log_dir = self.settings.value("ScriptRunner/log_directory", "/tmp")
        self.ui.leLogDirectory.setText(log_dir.toString())

        log_overwite = self.settings.value("ScriptRunner/log_overwite", False)
        self.ui.cbOverwriteLogFile.setChecked(log_overwite.toBool())

        # disable controls based on parent settings
        self.changed_show_output(self.ui.cbShowOutput.checkState())
        self.changed_log_to_disk(self.ui.cbLogToDisk.checkState())

 

    def set_log_dir(self):
        self.log_dir = QtGui.QFileDialog.getExistingDirectory(None, "Select the Directory for your Script Runner Logs", ".")
        if self.log_dir != '':
            # store the log_dir in settings
            self.ui.leLogDirectory.setText(self.log_dir)

    def changed_show_output(self, state):
         self.ui.cbClearConsole.setEnabled(state == Qt.Checked)

    def changed_log_to_disk(self, state):
         self.ui.leLogDirectory.setEnabled(state == Qt.Checked)
         self.ui.tbSetLogDirectory.setEnabled(state == Qt.Checked)
         self.ui.cbOverwriteLogFile.setEnabled(state == Qt.Checked)

    def save_settings(self):
        #QtGui.QMessageBox.information(None, "Save", "Saving Settings")
        self.settings.setValue("ScriptRunner/auto_display", self.ui.cbAutoDisplay.checkState() == Qt.Checked)
        self.settings.setValue("ScriptRunner/clear_console", self.ui.cbClearConsole.checkState() == Qt.Checked)
        self.settings.setValue("ScriptRunner/display_in_console", self.ui.cbShowOutput.checkState() == Qt.Checked)
        self.settings.setValue("ScriptRunner/log_output_to_disk", self.ui.cbLogToDisk.checkState() == Qt.Checked)
        self.settings.setValue("ScriptRunner/log_directory", self.ui.leLogDirectory.text())
        self.settings.setValue("ScriptRunner/log_overwrite", self.ui.cbOverwriteLogFile.checkState() == Qt.Checked)
