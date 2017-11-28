"""
Import the Traceback UI and intialize it.

ScriptRunner - A QGIS plugin that runs scripts to automate QGIS tasks.

Date: 2013-03-14
Copyright: (C) 2013 by GeoApt LLC
Email: gsherman@geoapt.com


This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

"""

from PyQt5.QtWidgets import QDialog
from .ui_traceback import Ui_TracebackDialog


class TracebackDialog(QDialog):
    """
    This class initializes the traceback dialog for Script Runner
    """

    def __init__(self):
        """
        Set up the user interface from Designer.
        """
        QDialog.__init__(self)
        self.ui = Ui_TracebackDialog()
        self.ui.setupUi(self)
