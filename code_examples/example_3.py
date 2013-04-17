"""Load all shapefiles in a given directory."""
from glob import glob
from os import path
from qgis.core import *
from qgis.gui import *
import qgis.utils


class Loader:
    def __init__(self, iface):
        """Initialize using the qgis.utils.iface
        object passed from the console.

        """
        self.iface = qgis.utils.iface

    def load_shapefiles(self, shp_path):
        """Load all shapefiles found in shp_path"""
        print "Loading shapes from %s" % path.join(shp_path, "*.shp")
        shps = glob(path.join(shp_path, "*.shp"))
        for shp in shps:
            (shpdir, shpfile) = path.split(shp)
            print "Loading %s" % shpfile
            lyr = QgsVectorLayer(shp, shpfile, 'ogr')
            QgsMapLayerRegistry.instance().addMapLayer(lyr)


def run_script(iface, data_path, buffer_size, **myargs):
    ldr = Loader(iface)
    print "Loading all shapefiles in %s" % myargs['shape_path']
    ldr.load_shapefiles(myargs['shape_path'])
    # Do something with data_path and buffer_size...
    print "data_path = %s" % data_path
    print "buffer_size = %s" % buffer_size
