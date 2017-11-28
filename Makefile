#/***************************************************************************
# ScriptRunner
# 
# Run scripts to automate QGIS tasks
#                             -------------------
#        begin                : 2012-01-27
#        copyright            : (C) 2012 by GeoApt LLC
#        email                : gsherman@geoapt.com
# ***************************************************************************/
# 
#/***************************************************************************
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 2 of the License, or     *
# *   (at your option) any later version.                                   *
# *                                                                         *
# ***************************************************************************/

# Makefile for a PyQGIS plugin 

#DOTQGIS = .qgis3
DOTQGIS = Library/Application\ Support/QGIS/QGIS3/profiles/default/
WORKDIR = work_dir
PLUGINNAME = scriptrunner3

PY_FILES = scriptrunner.py scriptrunner_mainwindow.py __init__.py preferences_dialog.py traceback_dialog.py scriptrunner_help.py stdout_textwidget.py syntax.py argsdialog.py scripteditor.py edit_buffer.py

EXTRAS = icon.png metadata.txt new_file.tmpl

UI_FILES = ui_scriptrunner.py mainwindow.py ui_preferences.py ui_traceback.py 

RESOURCE_FILES = resources.py

HELP_FILES = doc/_build/html/

default: compile

compile: $(UI_FILES) $(RESOURCE_FILES)

%.py : %.qrc
	pyrcc5 -o $@  $<

%.py : %.ui
	pyuic5 -o $@ $<

.PHONY: sphinx_doc

sphinx_doc:
	make -C doc html

# The deploy  target only works on unix like operating system where
# the Python plugin directory is located at:
# $HOME/$(DOTQGIS)/python/plugins
deploy: compile sphinx_doc
#deploy: compile 
	mkdir -p $(HOME)/$(DOTQGIS)/python/plugins/$(PLUGINNAME)
	cp -vf $(PY_FILES) $(HOME)/$(DOTQGIS)/python/plugins/$(PLUGINNAME)
	cp -vf $(UI_FILES) $(HOME)/$(DOTQGIS)/python/plugins/$(PLUGINNAME)
	cp -vf $(RESOURCE_FILES) $(HOME)/$(DOTQGIS)/python/plugins/$(PLUGINNAME)
	cp -vf $(EXTRAS) $(HOME)/$(DOTQGIS)/python/plugins/$(PLUGINNAME)
	mkdir -p $(HOME)/$(DOTQGIS)/python/plugins/$(PLUGINNAME)/help
	cp -rvf $(HELP_FILES)/* $(HOME)/$(DOTQGIS)/python/plugins/$(PLUGINNAME)/help

zipfile: compile sphinx_doc
	rm -rvf ./$(WORKDIR)
	mkdir -p $(WORKDIR)/$(PLUGINNAME)
	cp -vf $(PY_FILES) $(WORKDIR)/$(PLUGINNAME)
	cp -vf $(UI_FILES) $(WORKDIR)/$(PLUGINNAME)
	cp -vf $(RESOURCE_FILES) $(WORKDIR)/$(PLUGINNAME)
	cp -vf $(EXTRAS) $(WORKDIR)/$(PLUGINNAME)
	cp -rvf $(HELP_FILES) $(WORKDIR)/$(PLUGINNAME)/help
	cd $(WORKDIR);zip -9vr $(PLUGINNAME).zip $(PLUGINNAME)

dist: zipfile
	scp $(WORKDIR)/$(PLUGINNAME).zip geoapt.net:/var/vhosts/geoapt/qgis_plugins
# Create a zip package of the plugin named $(PLUGINNAME).zip. 
# This requires use of git (your plugin development directory must be a 
# git repository).
# 
# Get the last commit hash
COMMITHASH=$(shell git rev-parse HEAD)
package: compile
		rm -f $(PLUGINNAME).zip
		git archive --prefix=$(PLUGINNAME)/ -o $(PLUGINNAME).zip $(COMMITHASH)
		echo "Created package: $(PLUGINNAME).zip"
