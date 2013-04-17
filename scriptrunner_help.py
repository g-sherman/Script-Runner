"""

Help strings used in the plugin:
    htmlhelp: HTML for the Help tab - deprecated; help now displayed in browser
    htmlabout: HTML for the About tab

"""


def htmlhelp():
    """
    Return the html used to populate the Help tab.
    """
    return """<html>
    <body>
    <h2>Script Runner Help</h2>
    <br>
    <i>Run it like you own it</i>

    <p>
    <a href="#design">Design Options</a><br>
    <a href="#requirements">Requirements for Your Script</a><br>
    <a href="#working_with_scripts">Working with Scripts</a><br>
    <a href="#editing_a_script">Editing a Script</a><br>
    <a href="#passing_arguments">Passing Arguments</a></br>
    </p>
    <a name="design"/>
    <p>
    The Script Runner allows you to execute a script in QGIS to automate
    a task. The script can use two approaches to access the QGIS API:
    </p>
    <ol>
    <li>Use the qgis.utils.iface object</li>
    <li>Import qgis.core and qgis.gui</li>
    </ol>
    <p>
    In the first method, you are limited to to only those methods supported
    by the QgisInterface class. In the second you have full access to the
    PyQGIS API.
    </p>
    <a name="requirements"/>
    <h4>Requirements</h4>
    <p>
    In order for Script Runner to execute your script you must define a
    <em>run_script</em> function that accepts a single argument.
    This is the standard entry point used by Script Runner. A reference to
    the qgis.utils.iface object will be passed to your
    <em>run_script</em> function.
    You don't have to use the iface object in your script but your
    <em>run_script</em> function must accept it as an argument.
    </p>
   <p>
   Here is an example of a simple <em>run_script</em> function:
   </p>
   <pre>
    def run_script(iface):
        ldr = Loader(iface)
        ldr.load_shapefiles('/vmap0_shapefiles')
    </pre>

   <p>
   In this example, the <em>run_script</em> creates an instance (ldr) of a
   class named Loader that is defined in the same source file. It then calls a
   method in the Loader class named load_shapefiles to do something useful---in
   this case, load all the shapefiles in a specified directory.
   </p>
   <p>
   Alternatively, you could choose not to use classes and just do everything
   within the <em>run_script</em> function, including having it call functions
   in the same script or others you might import. The important thing is to be
   sure you have defined a <em>run_script</em> function. If not, Script Runner
   won't load your script.
   </p>
   <a name="working_with_scripts"/>
   <h4>Working with Scripts</h4>
   <p>
   To run a script, you must add it to Script Runner using the <em>Add
   Script</em> tool on the toolbar. This will add it to a list in the left
   panel. This list of scripts is persisted between uses of QGIS. You can
   remove a script using the <em>Remove Script</em> tool. This just removes it
   from the list; it does nothing to the script file on disk.
   </p>
   <p>
   Once you have a script loaded, you can click the <em>Script Info</em> tool
   to populate the Info and Source tabs in the panel on the right. The Info tab
   contains the docstring from your module and then a list of the classes,
   methods, and functions found in the script. Having a proper docstring at the
   head of your script will help you determine the puprose of script.  </p>
   <p>
   You can view the source of the script on the Source tab. This allows you
   to quickly confirm that you are using the right script and it does what you
   think it will.
   </p>

   <a name="editing_a_script"/>
   <h4>Editing a Script</h4>
   <p>
   The context menu (right-click on a script) has an <em>Edit script in external
   editor</em> option---this will open the script in the default system
   editor used for Python source files. If you wish to use a different editor,
   you can enter the full path to the editor on the Preferences dialog.
   </p>
   <p>
   This feature allows you to quickly make edits to your script during
   development. Once edited, be sure to click the *Reload* button to pull in
   the new version. You can leave the script open in your editor during the
   edit->reload->run cycle.
   </p>

   <a name="passing_arguments"/>
   <h4>Passing Arguments</h4>
   <p>
   You can pass one or more arguments to your script. Your <em>run_script</em>
   function must include an argument preceded by <tt>**</tt>:
   </p>
   <pre>
    def run_script(iface, **args):
    </pre>
   <p>
   To run the script, click the <em>Run script with arguments</em> button  and
   enter the arguments in the form: key=value.
   </p>
   <p>
   For example, if your script needs the path to a raster, you would enter the
   argument as:
   <pre>
   path='/data/myraster.tif'
   </pre>
   <p>
   In your <em>run_script</em> function you then access the path using:
   </p>
   <pre>
   args['path']
   </pre>
   <p>
   Arguments can be either numeric or string. Arguments are separated by commas
   and all strings must be quoted. For example:
   <pre>
   buffer_size=100, path='/data/myvectors.shp'
   </pre>


    </body>
    </html>"""


def htmlabout():
    """
    Return the html used to populate the About tab.
    """
    return """<html>
    <body>
    <h3>Script Runner - Version 0.71</h3>
    <p>
    Script Runner lets you run Python scripts in QGIS to automate and perform
    repetitive tasks.
    </p>
    <p>
    Author: Gary Sherman, Copyright &copy; 2012-2013 GeoApt LLC</p>
    <p>
    Email:
    <a href="mailto:gsherman@geoapt.com?Subject=Script Runner">
    gsherman@geoapt.com</>
    </p>
    <p>
    Repository: <a href="https://github.com/g-sherman/Script-Runner">
    https://github.com/g-sherman/Script-Runner</a>
    </p>
    <p>
    Bug Tracker: <a href="http://hub.qgis.org/projects/scriptrunner">
    http://hub.qgis.org/projects/scriptrunner</a>
    </p>

    <p>
    Please report issues and feature requests using the Bug Tracker.
    </p>
    <h4>Credits</h4>
    <ul>
    <li>Syntax highlighting taken from:
    <a href="http://diotavelli.net/PyQtWiki/Python%20syntax%20highlighting">
    http://diotavelli.net/PyQtWiki/Python%20syntax%20highlighting</a>
    "Based on existing work by Carson Farmer and Christophe Kibleur, and an
    example on the SciPres wiki."</li>
   </ul>
       <h4>Changelog</h4>
       <ul>
       <li>0.71</li>
       <ul>
       <li>For mandatory arguments, prompt by name</li>
       <li>A single run button is now used to run scripts with or without arguments</li>
       <li>Fixed bug that prevented syntax highlighting from working when
       reloading a script</li>
       <li>Updated documentation</li>
       <li>Moved help from tab to button that opens Sphinx doc in browser</li>
       </ul>
       </ul>
       <ul>
       <li>0.6</li>
       <ul>
       <li>Script output is logged to the Script Runner window<li>
       <li>Script output can be logged to disk</li>
       <li>Preferences dialog allows control of output and logging options</li>
       <li>Exceptions in scripts are displayed without interfering with
       console/logging output</li>
       <li>Context menu (right-click) to access script functions</li>
       <li>Edit script function uses system default editor or one you specify
       in preferences</li>
       <li>
       <li>Arguments can be passed to a script using keyword arguments</li>
       </ul>
       <li>0.5</li>
       <ul>
       <li>Double-click on script to show info/source</li>
       <li>Fix problem with info under master (issue #5034)</li>
       </ul>
    </body>
    </html>"""
