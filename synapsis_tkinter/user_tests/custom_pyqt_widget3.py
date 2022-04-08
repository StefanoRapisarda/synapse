import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyWidget(QWidget):

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        
        self.clicked = False

        self.resize(220, 180)
        layout = QGridLayout()
        self.setLayout(layout)

        self._node = _Node()
        layout.addWidget(self._node,1,0)
        layout.addWidget(QWidget(),0,0)
        layout.addWidget(QWidget(),2,0)

        self._text_box = QLabel()
        self._text_box.setText('Test label')
        self._text_box.setVisible(False)
        layout.addWidget(self._text_box,0,1)

    def paintEvent(self, e):

        x = 40
        y = 90
        size=30
        length=100

        painter = QPainter(self)
        brush = QBrush()
        brush.setColor(QColor('black)'))
        brush.setStyle(Qt.SolidPattern)
        pen = QPen(Qt.black)
        pen.setWidth(2)
        painter.setBrush(brush)
        painter.setPen(pen)
        center = QPoint(x,y)
        if self.clicked:
            break1 = QPoint(center.x()+size*2,center.y()-size*2)
            break2 = QPoint(center.x()+size*2+length,center.y()-size*2)
            painter.drawLine(center,break1)
            painter.drawLine(break1,break2)
            # This will call another widget 
        painter.end()

    def mouseDoubleClickEvent(self,event):
        print('Double click')
        if not self.clicked:
            self.clicked = True
            self._text_box.setVisible(True)
        else:
            self.clicked = False
            self._text_box.setVisible(False)
        self.update()

class _Node(QWidget):

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

        self.resize(40,40)
        self.x = 20
        self.y = 20
        self.size=10
        self.length=100
        self.clicked = False

    def paintEvent(self, e):
        painter = QPainter(self)
        brush = QBrush()
        brush.setColor(QColor('black)'))
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)
        center = QPoint(self.x,self.y)
        painter.drawEllipse(center,self.size,self.size)
        painter.end()

app = QApplication(sys.argv)
# ex = CustomButtonPopup()
ex = MyWidget()
ex.show()
sys.exit(app.exec_())