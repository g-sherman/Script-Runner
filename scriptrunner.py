"""
ScriptRunner - A QGIS plugin that runs scripts to automate QGIS tasks.

Date: 2012-01-27
Copyright: (C) 2012 by GeoApt LLC
Email: gsherman@geoapt.com


This program is free software; you can redistribute it and/or modify  
it under the terms of the GNU General Public License as published by  
the Free Software Foundation; either version 2 of the License, or     
(at your option) any later version.                                   
                                                                          
"""

import sys
import os
import re
import inspect

# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from scriptrunner_mainwindow import ScriptRunnerMainWindow
# Import the help module
from scriptrunner_help import *
#from highlighter import *
from syntax import *

class ScriptRunner:

    """
    ScriptRunner is the main plugin class that initializes the QGIS
    plugin, initializes the GUI, and performs the work.
    """

    def __init__(self, iface):
        """
        Save reference to the QGIS interface
        """
        self.iface = iface


    def initGui(self):
        """
        Initialize the GUI elements and menu/tool 
        on the QGIS Plugins toolbar.
        """
        # create the mainwindow
        self.mw = ScriptRunnerMainWindow()
        # fetch the list of stored scripts from user setting
        settings = QSettings()
        stored_scripts = settings.value("ScriptRunner/scripts")
        self.list_of_scripts = stored_scripts.toList()

        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/scriptrunner/icon.png"), \
            "ScriptRunner", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

#        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&ScriptRunner", self.action)

        self.main_window = self.mw.ui

        self.toolbar = self.main_window.toolBar
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        ## Action setup 
        # action for adding a script
        self.add_action = QAction(QIcon(":plugins/scriptrunner/add_icon"),
                "Add Script", self.mw)
        self.toolbar.addAction(self.add_action)
        QObject.connect(self.add_action, SIGNAL("triggered()"), self.add_script)

        # action for running a script
        self.run_action = QAction(QIcon(":plugins/scriptrunner/run_icon"),
                "Run Script", self.mw)
        self.toolbar.addAction(self.run_action)
        QObject.connect(self.run_action, SIGNAL("triggered()"), self.run_script)

        # action for getting info about a script
        self.info_action = QAction(QIcon(":plugins/scriptrunner/info_icon"),
                "Script Info", self.mw)
        self.toolbar.addAction(self.info_action)
        QObject.connect(self.info_action, SIGNAL("triggered()"), self.info)


        # action for reloading a script
        self.reload_action = QAction(QIcon(":plugins/scriptrunner/reload_icon"),
                "Reload Script", self.mw)
        self.toolbar.addAction(self.reload_action)
        QObject.connect(self.reload_action, SIGNAL("triggered()"), self.reload_script)

        # action for removing a script
        self.remove_action = QAction(QIcon(":plugins/scriptrunner/cancel_icon"),
                "Remove Script", self.mw)
        self.toolbar.addAction(self.remove_action)
        QObject.connect(self.remove_action, SIGNAL("triggered()"), self.remove_script)

        # setup the splitter and list/text browser and mainwindow layout
        self.layout = QHBoxLayout(self.main_window.frame)
        self.splitter = QSplitter(self.main_window.frame)
        self.layout.addWidget(self.splitter)

        self.scriptList = QListWidget()
        # connect double click to info slot
        QObject.connect(self.scriptList, SIGNAL("itemDoubleClicked(QListWidgetItem *)"), self.item_info)

        self.splitter.addWidget(self.scriptList)

        self.tabWidget = QTabWidget()

        self.textBrowser = QTextBrowser()
        self.tabWidget.addTab(self.textBrowser, "Info")

        self.textBrowserSource = QTextBrowser()
        self.tabWidget.addTab(self.textBrowserSource, "Source")
        highlighter = PythonHighlighter(self.textBrowserSource.document())
        
        self.textBrowserHelp = QTextBrowser()
        self.textBrowserHelp.setHtml(htmlhelp())
        self.tabWidget.addTab(self.textBrowserHelp, "Help")

        self.textBrowserAbout = QTextBrowser()
        self.textBrowserAbout.setHtml(htmlabout())
        self.textBrowserAbout.setOpenExternalLinks(True)
        self.tabWidget.addTab(self.textBrowserAbout, "About")

        self.splitter.addWidget(self.tabWidget)
        # set the sizes for the splitter
        split_size = [150, 350]
        self.splitter.setSizes(split_size)
        
        if len(self.list_of_scripts) == 0:
            # make the help tab visible if no scripts are loaded
            self.tabWidget.setCurrentIndex(2)
        else:
            # add the list of scripts fetched from settings
            for script in self.list_of_scripts:
                (script_dir, script_name) = os.path.split(str(script.toString()))
                item = QListWidgetItem(script_name, self.scriptList)
                item.setToolTip(script.toString())

    def unload(self):
        """
        Cleanup the QGIS GUI by removing the plugin menu item and icon.
        """
        self.iface.removePluginMenu("&ScriptRunner",self.action)
        self.iface.removeToolBarIcon(self.action)

    def add_script(self):
        """
        Add a script to the list of scripts that can be executed.
        """
        script = QFileDialog.getOpenFileName(None, "Add a Python Script", 
                "", "Python scripts (*.py)")
        if script:
            # check to see if we have a run method without importing the script
            if self.have_run_method(script):
                (script_dir, script_name) = os.path.split(str(script))
                item = QListWidgetItem(script_name, self.scriptList)
                item.setToolTip(script)
                self.main_window.statusbar.showMessage("Added script: %s" % script)
                self.list_of_scripts.append(script)
                self.update_settings()
                
            else:
                QMessageBox.information(None, "Error", "Your script must have a run_script() function defined. Adding the script failed.")
                self.main_window.statusbar.showMessage("Failed to add: %s - no run_script function" % script)



    def remove_script(self):
        """
        Remove a script from the list of scripts that can be executed.
        """
        item = self.scriptList.currentItem()
        if item != None:
            result = QMessageBox.question(None, "Remove Script", 
                    "Are you sure you want to remove %s?" % item.text(),
                    QMessageBox.Yes, QMessageBox.No)
            if result == QMessageBox.Yes:
                self.list_of_scripts.pop(self.list_of_scripts.index(item.toolTip()))
                self.update_settings()
                self.scriptList.takeItem(self.scriptList.currentRow())

    def reload_script(self):
        """
        Reload the currently selected script.
        """
        item = self.scriptList.currentItem()
        if item != None:
            script = item.toolTip()
            (script_dir, script_name) = os.path.split(str(script))
            (user_module, ext) = os.path.splitext(script_name)
            if sys.modules.has_key(user_module):
                reload(sys.modules[user_module])
                self.main_window.statusbar.showMessage("Reloaded script: %s" % script)
                self.info()
            else:
                QMessageBox.information(None, "Reload", 
                        "The %s script was not reloaded since it hasn't been imported yet" % user_module)

                
    def item_info(self, item):
        self.info(item)

    def info(self, item=None):
        """
        Display information about the script, including the docstring,
        classes, methods, and functions.
        """
        if item == None:
            item = self.scriptList.currentItem()
        if item != None: # just in case there is no currentitem and none was passed
            script = item.toolTip()
            (script_dir, script_name) = os.path.split(str(script))
            (user_module, ext) = os.path.splitext(script_name)
            if script_dir not in sys.path:
                sys.path.append(script_dir)
            if not sys.modules.has_key(user_module):
                __import__(user_module)

            # add the doc string to the info page
            doc_string = inspect.getdoc(sys.modules[user_module])
            if doc_string == None:
                doc_string = "You Have no Docstring. You really should add one..."
            else:
                doc_string = doc_string.replace('\n', '<br>')
            html = "<h3>%s</h3><h4>Doc String:</h4>%s" % (script, doc_string)

            # populate the source tab
            source_code = "<pre>%s</pre>" % self.get_source(script) #inspect.getsource(sys.modules[user_module])
            self.textBrowserSource.setHtml(source_code)

            classes = inspect.getmembers(sys.modules[user_module], inspect.isclass)

            # populate classes and methdods

            html += "<h4>Classes and Methods for %s</h4><ul>" % script_name

            for cls in classes:
              modinfo = inspect.getmodule(cls[1])
              if modinfo:
                  if modinfo.__name__ == user_module:
                      html += "<li>%s</li>" % cls[0]
                      html += "<ul>"
                      for meth in inspect.getmembers(cls[1], inspect.ismethod):
                        html+= "<li>%s</li>" % meth[0]
                      html += "</ul></ul>"
            functions = inspect.getmembers(sys.modules[user_module], inspect.isfunction)
            html += "<h4>Functions in %s</h4><ul>" % script_name
            for func in functions:
                modinfo = inspect.getmodule(func[1])
                if modinfo.__name__ == user_module:
                    html += "<li>%s</li>" % func[0]
            html += "</ul>"

            self.textBrowser.setHtml(html)
            self.tabWidget.setCurrentIndex(0)



    def get_source(self, script):
        src = open(script, 'r')
        source = src.read()#.replace("\n", '<br>')
        source 
        src.close()
        return source

    def run_script(self):
        """
        Run the currently selected script.
        """
        # get the selected item from the list
        item = self.scriptList.currentItem()
        if item != None:
            script = item.toolTip()
            self.main_window.statusbar.showMessage("Running script: %s" % script)
    
            # get the path and add it to sys.path
            (script_dir, script_name) = os.path.split(str(script))
   
            if script_dir not in sys.path:
                sys.path.append(script_dir)
            (user_module, ext) = os.path.splitext(script_name)
  
            user_script = __import__(user_module)
 
            user_script.run_script(self.iface)
            self.main_window.statusbar.showMessage("Completed script: %s" % script)

    def run(self):
        """
        Bring up the main window.
        """
        self.mw.show()

    def have_run_method(self, script_path):
        """
        Parse the script to make sure it has a run_script function
        before allowing it to be added to the list of scripts.
        """
        script = open(script_path, 'r')
        pattern = re.compile('\s*def run_script\(*')
        run_method = False
        for line in script:
            if pattern.search(line):
                run_method = True
                break
        script.close()
        return run_method

    def update_settings(self):
        """
        Update the setting for the plugin---at present just
        the list of scripts.
        """
        settings = QSettings()
        settings.setValue("ScriptRunner/scripts", QVariant(self.list_of_scripts))

      

