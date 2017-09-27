""" Load a layer and change the fill color to red. """
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from qgis.gui import *


def run_script(iface):
    mapreg = QgsMapLayerRegistry.instance()
    mapreg.removeAllMapLayers()
    wb = QgsVectorLayer('/dev1/gis_data/qgis_sample_data/shapefiles/alaska.shp', 'world_borders', 'ogr')
    mapreg.instance().addMapLayer(wb)
    renderer = wb.rendererV2()
    symb = renderer.symbol()
    symb.setColor(QColor(Qt.red))
    iface.mapCanvas().refresh()
    if QGis.QGIS_VERSION_INT < 10900:
        iface.refreshLegend(wb)
    else:
        iface.legendInterface().refreshLayerSymbology(wb)
