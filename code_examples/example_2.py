"""Load all shapefiles in a given directory.  """
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


def run_script(iface):
    ldr = Loader(iface)
    print "Loading all shapefiles in /dev1/gis_data/qgis_sample_data/shapefiles"
    ldr.load_shapefiles('/dev1/gis_data/qgis_sample_data/shapefiles')
