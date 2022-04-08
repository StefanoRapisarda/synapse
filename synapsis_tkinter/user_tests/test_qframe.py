import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.txtFrame = QFrame(self)
        self.txtFrame.setGeometry(QRect(50, 50, 50, 50))
        self.txtFrame.setVisible(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    app.exec_()