import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication, Qt, pyqtSignal, pyqtSlot

from LayoutInAction import *

# 这部分是业务逻辑代码

class MyMainWindow(QMainWindow, Ui_MainWindow): # Ui_MainWindow是界面文件中的类，继承
	def __init__(self, parent=None):
		super(MyMainWindow, self).__init__(parent)
		self.setupUi(self) # 执行完这步，才有控件，此窗体继承了界面文件类，可以通过self.xx拿到控件
	
	@pyqtSlot()
	def on_pushButton_clicked(self):
		print('收益_min: ', self.doubleSpinBox_returns_min.text())
		print('收益_mx: ', self.doubleSpinBox_returns_max.text())
		print('最大回撤_min: ', self.doubleSpinBox_maxdrawdown_min.text())
		print('最大回撤_max: ', self.doubleSpinBox_maxdrawdown_max.text())

		print('夏普比_min: ', self.doubleSpinBox_sharp_min.text())
		print('夏普比_max: ', self.doubleSpinBox_sharp_max.text())


if __name__ == '__main__':
	app = QApplication(sys.argv)
	myWin = MyMainWindow()
	myWin.show()
	sys.exit(app.exec_())