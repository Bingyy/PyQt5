# Time: 20180514
# Author: BEING -- notes from 《PyQt5入门》
# useage: Free to use 

'''
关闭窗体询问

'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.setGeometry(0,0,800,600) # 设定坐标为0,0，大小为800,600
		self.setWindowTitle('myapp') # 设置窗口标题
		self.setToolTip('What are u staring at?') # 设置弹出的文本
		self.center()
		# QToolTip.setFont(QFont('苹方简',12))
		QToolTip.setFont(QFont('微软雅黑',12)) # 设置字体，似乎并没变化，有待纠正

	# 定义关闭事件函数
	def closeEvent(self,event):

		reply = QMessageBox.question(self, '信息','确定退出？',QMessageBox.Yes, QMessageBox.No)
		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

	# 窗体居中显示
	def center(self):
		screen = QDesktopWidget().screenGeometry() # 返回表示屏幕的实例
		size = self.geometry() # 返回的是窗体实例
		self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2) # 向右向下移动

myapp = QApplication(sys.argv) # 任何窗口程序都需要一个QApplication实例
mywidget = MyWidget()
mywidget.show() # 显示窗体
sys.exit(myapp.exec_()) # 窗体退出函数