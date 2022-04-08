from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QHBoxLayout,QListWidgetItem
from PyQt5.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.myListWidget1 = QListWidget()
        self.myListWidget2 = QListWidget()

        self.myListWidget2.setViewMode(QListWidget.IconMode)
        self.myListWidget1.setAcceptDrops(True)
        self.myListWidget1.setDragEnabled(True)
        
        self.myListWidget2.setAcceptDrops(True)
        self.myListWidget2.setDragEnabled(True)

        # x,y,width,height
        self.setGeometry(300,350,500,300)

        self.hboxlayout = QHBoxLayout()
        self.hboxlayout.addWidget(self.myListWidget1)
        self.hboxlayout.addWidget(self.myListWidget2)

        # Here you create item

