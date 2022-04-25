import sys
#from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from gui.synapsis_dialogue import *
import shelve
from utilities import *

class MyForm(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.load_entries()
        self.ui.treeViewEntriesLeft.clicked.connect(self.print_row)

    def print_row(self):
        rows = self.ui.treeViewEntriesLeft.selectionModel().selectedIndexes()
        print (self.model.item(rows[0].row()).text()

    def load_entries(self):
        self.model = QtGui.QStandardItemModel()
        self.labels = ['date','category','subject','collection','activity','id']
        self.model.setHorizontalHeaderLabels(self.labels)
        self.ui.treeViewEntriesLeft.header().setDefaultSectionSize(80)
        self.ui.treeViewEntriesLeft.setModel(self.model)

        rows=read_entries(self.labels)
        for row in rows:
            row[0] = id_to_date(row[-1])
            items = [QtGui.QStandardItem(field) for field in row]
            self.model.appendRow(items)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyForm()
    win.show()
    sys.exit(app.exec_())