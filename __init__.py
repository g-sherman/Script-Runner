"""
This script initializes the plugin, making it known to QGIS.

ScriptRunner - A QGIS plugin that runs scripts to automate QGIS tasks.

Date: 2012-01-27
Copyright: (C) 2012-2013 by GeoApt LLC
Email: gsherman@geoapt.com


This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

"""


def classFactory(iface):
    """
    Load ScriptRunner class from file ScriptRunner, passing
    it the qgis.utils.iface object.
    """
    from .scriptrunner import ScriptRunner
    return ScriptRunner(iface)
