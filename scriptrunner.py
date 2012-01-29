"""
 ScriptRunner
 A QGIS plugin
 Run scripts to automate QGIS tasks
                              -------------------
        begin                : 2012-01-27
        copyright            : (C) 2012 by GeoApt LLC
        email                : gsherman@geoapt.com


    This program is free software; you can redistribute it and/or modify  
    it under the terms of the GNU General Public License as published by  
    the Free Software Foundation; either version 2 of the License, or     
    (at your option) any later version.                                   
                                                                          
"""

import sys
import os
import inspect

# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from scriptrunner_mainwindow import ScriptRunnerMainWindow

class ScriptRunner:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # create the mainwindow
        self.mw = ScriptRunnerMainWindow()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/scriptrunner/icon.png"), \
            "ScriptRunner", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # connect the run button to the run_script method
#        QObject.connect(self.dlg.ui.pushBtnRun, SIGNAL("clicked()"), self.run_script)
#
#        # connect the add button to the add method
#        QObject.connect(self.dlg.ui.pushAdd, SIGNAL("clicked()"), self.add_script)
#        # connect the remove button to the remove method
#        QObject.connect(self.dlg.ui.pushRemove, SIGNAL("clicked()"), self.remove_script)
#
#        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&ScriptRunner", self.action)
#
#        #grid_layout = QGridLayout(self.dlg.ui.frame)
#        # create the main toolbar
#        self.toolbar = QToolBar('Toolbar', self.dlg) #.ui.frame)
#
#        self.action_group = QActionGroup(self.dlg)

        self.main_window = self.mw.ui

        self.toolbar = self.main_window.toolBar
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        ## Action setup 
        # action for adding a script
        self.add_action = QAction(QIcon(":plugins/scriptrunner/icon.png"),
                "Add Script", self.mw)
        #self.add_action.setIconText('Add script')
        self.toolbar.addAction(self.add_action)
        QObject.connect(self.add_action, SIGNAL("triggered()"), self.add_script)

        # action for running a script
        self.run_action = QAction(QIcon(":plugins/scriptrunner/icon.png"),
                "Run Script", self.mw)
        #self.run_action.setIconText('Run script')
        self.toolbar.addAction(self.run_action)
        QObject.connect(self.run_action, SIGNAL("triggered()"), self.run_script)

        # action for getting info about a script
        self.info_action = QAction(QIcon(":plugins/scriptrunner/icon.png"),
                "Script Info", self.mw)
        #self.info_action.setIconText('Script Info')
        self.toolbar.addAction(self.info_action)
        QObject.connect(self.info_action, SIGNAL("triggered()"), self.info)

        #jself.action_group.addAction(self.add_action)
        #jself.action_group.addAction(self.info_action)
#
#
#        self.toolbar.addWidget(self.action_group)
#        #self.toolbar.addAction(self.add_action)
#        #self.toolbar.addAction(self.info_action)
#        #grid_layout.addWidget(self.toolbar)
#

        # setup the splitter and list/text browser
        self.layout = QHBoxLayout(self.main_window.frame)

        self.splitter = QSplitter(self.main_window.frame)


        self.layout.addWidget(self.splitter)
        self.scriptList = QListWidget()
        self.splitter.addWidget(self.scriptList)
        self.tabWidget = QTabWidget()
        self.textBrowser = QTextBrowser()
        self.textBrowserSource = QTextBrowser()
        self.tabWidget.addTab(self.textBrowser, "Info")
        self.tabWidget.addTab(self.textBrowserSource, "Source")
        self.splitter.addWidget(self.tabWidget)
        # set the sizes for the splitter
        split_size = [150, 350]
        self.splitter.setSizes(split_size)
        
#
#        # add test data
#
        item = QListWidgetItem('loader.py', self.scriptList)
        item.setToolTip('/Users/gsherman/qgis_scripts/loader.py')
#
    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&ScriptRunner",self.action)
        self.iface.removeToolBarIcon(self.action)

    def add_script(self):
        script = QFileDialog.getOpenFileName(None, "Add a Python Script", "", "Python scripts (*.py)")
        (script_dir, script_name) = os.path.split(str(script))
        item = QListWidgetItem(script_name, self.scriptList)
        item.setToolTip(script)
        QMessageBox.information(None, "Add", script)
        self.main_window.statusbar.showMessage("Added script: %s" % script)

    def remove_script(self):
        QMessageBox.information(None, "Remove", "Remove script was clicked")

    def info(self):
        item = self.scriptList.currentItem()
        if item != None:
            script = item.toolTip()
            (script_dir, script_name) = os.path.split(str(script))
            (user_module, ext) = os.path.splitext(script_name)
            if script_dir not in sys.path:
                sys.path.append(script_dir)
            if not sys.modules.has_key(user_module):
                __import__(user_module)

            # add the doc string to the info page
            doc_string = inspect.getdoc(sys.modules[user_module])
            doc_string = doc_string.replace('\n', '<br>')
            html = "<h4>Doc String:</h4>%s" % doc_string

            # populate the source tab
            source_code = "<pre>%s</pre>" % inspect.getsource(sys.modules[user_module])
            self.textBrowserSource.setHtml(source_code)

            classes = inspect.getmembers(sys.modules[user_module], inspect.isclass)

            # populate classes and methdods

            html += "<h4>Classes and Methods for %s</h4><ul>" % script_name

            for cls in classes:
              modinfo = inspect.getmodule(cls[1])
              if modinfo.__name__ == user_module:
                  html += "<li>%s</li>" % cls[0]
                  #print "  ", cls[0] #, modinfo.__name__, inspect.getmodule(c[1])
                  #html += "&nbsp;&nbsp;&nbsp;<b>Methods:</b><br/><ul>"
                  html += "<ul>"
                  for meth in inspect.getmembers(cls[1], inspect.ismethod):
                    html+= "<li>%s</li>" % meth[0]
                  html += "</ul></ul>"
            functions = inspect.getmembers(sys.modules[user_module], inspect.isfunction)
            html += "<h4>Functions and Methods in %s</h4><ul>" % script_name
            for func in functions:
                modinfo = inspect.getmodule(func[1])
                if modinfo.__name__ == user_module:
                    html += "<li>%s</li>" % func[0]
            html += "</ul>"

            self.textBrowser.setHtml(html)



    def run_script(self):
        # get the selected item from the list
        item = self.scriptList.currentItem()
        if item != None:
            script = item.toolTip()
            self.main_window.statusbar.showMessage("Running script: %s" % script)
            #QMessageBox.information(None, "Run", "This would run " + script)
            # get the path and add it to sys.path
            (script_dir, script_name) = os.path.split(str(script))
            #QMessageBox.information(None, "Run", "Script dir / name " + script_dir + " / " + script_name)
            if script_dir not in sys.path:
                sys.path.append(script_dir)
            (user_module, ext) = os.path.splitext(script_name)
            #QMessageBox.information(None, "Run", "Imported Module " + user_module)
            user_script = __import__(user_module)
            #QMessageBox.information(None, "Run", str(dir(user_script)))
            user_script.run(self.iface)
            self.main_window.statusbar.showMessage("Completed script: %s" % script)




    # run method that performs all the real work
    def run(self):

        # show the dialog
        self.mw.show()
        #result = self.dlg.exec_()
        ## See if OK was pressed
        #if result == 1:
        #    # do something useful (delete the line containing pass and
        #    # substitute with your code
        #    sys.path.append('/Users/gsherman/qgis_scripts')
        #    import loader
        #    loader.run(self.iface)
        #    self.dlg.reject()
