""" Load a layer and change the fill color to red. """
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from qgis.gui import *


def run_script(iface):
    project = QgsProject.instance()
    #project.removeAllMapLayers()
    wb = QgsVectorLayer('/Users/gsherman/Downloads/pyqgis_data/world_borders.shp', 'world_borders', 'ogr')
    project.instance().addMapLayer(wb)
    renderer = wb.renderer()
    symb = renderer.symbol()
    symb.setColor(QColor(Qt.yellow))
    wb.triggerRepaint()
    iface.layerTreeView().refreshLayerSymbology(wb.id())
