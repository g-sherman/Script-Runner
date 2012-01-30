"""
/***************************************************************************
 ScriptRunner
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
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "ScriptRunner"
def description():
    return "Run scripts to automate QGIS tasks"
def version():
    return "Version 0.3"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.7"
def classFactory(iface):
    # load ScriptRunner class from file ScriptRunner
    from scriptrunner import ScriptRunner
    return ScriptRunner(iface)
