import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyWidget(QWidget): # 继承自QWidget
	def __init__(self):
		super().__init__()
		self.resize(800,600) 
		self.setGeometry(0, 0, 800, 600) # 坐标 00 大小 800 600 
		self.setWindowTitle('myapp')
		self.setWindowIcon(QIcon('fire.ico'))

myapp = QApplication(sys.argv)
mywidget = MyWidget()
mywidget.show()
sys.exit(myapp.exec_())

