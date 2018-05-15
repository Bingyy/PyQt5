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
		# QToolTip.setFont(QFont('苹方简',12))
		QToolTip.setFont(QFont('微软雅黑',12)) # 设置字体，似乎并没变化，有待纠正

	# 定义关闭事件函数
	def closeEvent(self,event):
		# 询问窗体，四个参数
		# 1. 询问窗体所属的母体
		# 2. 弹出窗体标题
		# 3. 标准的Button
		# 4. 标准的Button
		reply = QMessageBox.question(self, '信息','确定退出？',QMessageBox.Yes, QMessageBox.No)
		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

myapp = QApplication(sys.argv) # 任何窗口程序都需要一个QApplication实例
mywidget = MyWidget()
mywidget.show() # 显示窗体
sys.exit(myapp.exec_()) # 窗体退出函数