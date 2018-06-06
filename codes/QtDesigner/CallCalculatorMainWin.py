import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication, Qt, pyqtSignal, QObject

from Calculator import *

class MyMainWindow(QMainWindow, Ui_MainWindow): # Ui_MainWindow是界面文件中的类
	def __init__(self, parent=None):
		super(MyMainWindow, self).__init__(parent)
		self.setupUi(self)
	
if __name__ == '__main__':
	app = QApplication(sys.argv)
	myWin = MyMainWindow()
	myWin.show()
	sys.exit(app.exec_())