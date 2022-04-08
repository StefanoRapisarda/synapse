from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import QPoint, Qt
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        widget1 = MyWidget()
        widget2 = MyWidget()

        


class MyWidget(QtWidgets.QWidget):

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

        layout = QtWidgets.QHBoxLayout()
        self._node = _Node()
        layout.addWidget(self._node)

        self._text_box = QtWidgets.QLabel()
        self._text_box.setText('This is a test label')
        layout.addWidget(self._text_box)

        self.setLayout(layout)

class _Node(QtWidgets.QWidget):

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

        self.x = 20
        self.y = 20
        self.size=10
        self.length=100
        self.clicked = False

    def mouseDoubleClickEvent(self,event):
        if not self.clicked:
            self.clicked = True
        else:
            self.clicked = False

    def mousePressEvent(self, event):
        self.x= event.pos().x()
        self.y = event.pos().y()
        self.update()

    def mouseMoveEvent(self, event):
        self.x= event.pos().x()
        self.y = event.pos().y()
        self.update()

    def mouseReleaseEvent(self, event):
        self.x= event.pos().x()
        self.y = event.pos().y()
        self.update()

    def paintEvent(self, e):
        painter = QPainter(self)
        brush = QBrush()
        brush.setColor(QColor('black)'))
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)
        center = QPoint(self.x,self.y)
        painter.drawEllipse(center,self.size,self.size)
        if self.clicked:
            break1 = QPoint(center.x()+self.size*2,center.y()-self.size*2)
            break2 = QPoint(center.x()+self.size*2+self.length,center.y()-self.size*2)
            painter.drawLine(center,break1)
            painter.drawLine(break1,break2)
            # This will call another widget 
        painter.end()

    def _trigger_refresh(self):
        self.update()


app = QtWidgets.QApplication([])
volume = MyWidget()
volume.show()
app.exec_()