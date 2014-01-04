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
        # connect the set custom editor path button
        self.ui.tbSetEditorPath.clicked.connect(self.editor_path)

        # connect the checkbox state change
        self.ui.cbLogToDisk.stateChanged.connect(self.changed_log_to_disk)

        self.settings = QtCore.QSettings()
        self.restore_settings()

    def restore_settings(self):
        auto_display = self.settings.value(
            "ScriptRunner/auto_display", True, type=bool)
        self.ui.cbAutoDisplay.setChecked(auto_display)
        show_console = self.settings.value(
            "ScriptRunner/show_console", True, type=bool)
        self.ui.cbShowConsole.setChecked(show_console)
        clear_console = self.settings.value(
            "ScriptRunner/clear_console", False, type=bool)
        self.ui.cbClearConsole.setChecked(clear_console)
        log_output = self.settings.value(
            "ScriptRunner/log_output_to_disk", False, type=bool)
        self.ui.cbLogToDisk.setChecked(log_output)

        log_dir = self.settings.value(
            "ScriptRunner/log_directory", "", type=unicode)
        self.ui.leLogDirectory.setText(log_dir)

        log_overwite = self.settings.value(
            "ScriptRunner/log_overwrite", False, type=bool)
        self.ui.cbOverwriteLogFile.setChecked(log_overwite)

        use_custom_editor = self.settings.value(
            "ScriptRunner/use_custom_editor", False, type=bool)
        self.ui.cbCustomEditor.setChecked(use_custom_editor)

        custom_editor = self.settings.value(
            "ScriptRunner/custom_editor", "", type=unicode)
        self.ui.leCustomEditorPath.setText(custom_editor)

        # disable controls based on parent settings
        self.changed_log_to_disk(self.ui.cbLogToDisk.checkState())

    def set_log_dir(self):
        self.log_dir = QtGui.QFileDialog.getExistingDirectory(
            None, "Select the Directory for your Script Runner Logs", ".")
        if self.log_dir != '':
            # store the log_dir in settings
            self.ui.leLogDirectory.setText(self.log_dir)

    def editor_path(self):
        self.editor_path = QtGui.QFileDialog.getOpenFileName(
            None, "Select the Application for Editing Scripts", ".")
        if self.editor_path != '':
            # store the log_dir in settings
            self.ui.leCustomEditorPath.setText(self.editor_path)

    def changed_log_to_disk(self, state):
        self.ui.leLogDirectory.setEnabled(state == Qt.Checked)
        self.ui.tbSetLogDirectory.setEnabled(state == Qt.Checked)
        self.ui.cbOverwriteLogFile.setEnabled(state == Qt.Checked)

    def save_settings(self):
        self.settings.setValue(
            "ScriptRunner/auto_display",
            self.ui.cbAutoDisplay.checkState() == Qt.Checked)
        self.settings.setValue(
            "ScriptRunner/clear_console",
            self.ui.cbClearConsole.checkState() == Qt.Checked)
        self.settings.setValue(
            "ScriptRunner/show_console",
            self.ui.cbShowConsole.checkState() == Qt.Checked)
        self.settings.setValue(
            "ScriptRunner/log_output_to_disk",
            self.ui.cbLogToDisk.checkState() == Qt.Checked)
        self.settings.setValue(
            "ScriptRunner/log_directory",
            self.ui.leLogDirectory.text())
        self.settings.setValue(
            "ScriptRunner/log_overwrite",
            self.ui.cbOverwriteLogFile.checkState() == Qt.Checked)
        self.settings.setValue(
            "ScriptRunner/use_custom_editor",
            self.ui.cbCustomEditor.checkState() == Qt.Checked)
        self.settings.setValue(
            "ScriptRunner/custom_editor",
            self.ui.leCustomEditorPath.text())
