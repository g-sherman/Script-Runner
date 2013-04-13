from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *

class ArgsDialog(QDialog):

    def __init__(self, argspec, script_name):
        QDialog.__init__(self)
        self.setWindowTitle("Enter Arguments for %s" % script_name)
        self.setMinimumWidth(400)
        self.grid = QGridLayout(self)
        self.build_dialog(argspec)
        

    def build_dialog(self, argspec):
        # args is an ArgSpec object
        self.arg_map = list()
        row = 0
        col = 0
        arg_count = 0
        if len(argspec.args) > 1:
            self.grid.addWidget(QLabel(
                "Enter arguments below. Strings must be quoted."), row, 0,
                1, 2)
            row += 1
        for arg in argspec.args:
            if arg != 'iface':
                # create a label and line edit
                self.grid.addWidget(QLabel(arg), row, col)
                col += 1
                le = QLineEdit()
                self.grid.addWidget(le, row, col)
                self.arg_map.append(le)
                row += 1
                col =0
                arg_count += 1

        # check to see if the method accepts keyword args
        if argspec.keywords:
            self.grid.addWidget(QLabel(
                "Enter comma separated keyword arguments as key=value pairs."),
                 row, 0, 1, 2)
            row += 1
            self.grid.addWidget(QLabel(
                "String values must be quoted. Example: path='/data', buffer=100"),
                row, 0, 1, 2)
            row += 1
            self.keywords = QLineEdit()
            self.grid.addWidget(self.keywords, row, 0, 1, 2)
            row += 1
            arg_count += 1
        else:
            self.keywords = None

        # add the button group
        h_layout = QHBoxLayout()
        btn_run = QPushButton("Run")
        btn_run.setMaximumWidth(80)
        btn_run.clicked.connect(self.accept)
        h_layout.addWidget(btn_run)
        btn_cancel = QPushButton("Cancel")
        btn_cancel.setMaximumWidth(80)
        btn_cancel.clicked.connect(self.reject)
        h_layout.addWidget(btn_cancel)
        self.grid.addLayout(h_layout, row, 0, 1, 2)


    def show_dialog(self):
        result = self.exec_()
        if result == 1:
            #print "fetching results"
            arg_values = list()
            arg_map = dict()
            # fetch the args values
            for line_edit in self.arg_map:
                arg_values.append(str(line_edit.text()))
            arg_map['args'] = arg_values

            if self.keywords:
                arg_map['keywords'] = str(self.keywords.text())
            else:
                arg_map['keywords'] = None

            print "arg_map returned from argsdialog", arg_map
            # return a containing the args
            return arg_map
        else:
            return None



