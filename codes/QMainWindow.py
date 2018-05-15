# Time: 20180514
# Author: BEING -- notes from 《PyQt5入门》
# useage: Free to use 

'''
QMainWindow

'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	

	def initUI(self):
		self.resize(800,600) 
		self.center()
		self.setWindowTitle('myapp') # 设置窗口标题
		
		# 菜单栏
		menu_control = self.menuBar().addMenu('Control')
		act_quit = menu_control.addAction('quit')
		act_quit.triggered.connect(self.close) 

		menu_help = self.menuBar().addMenu('Help')
		act_about = menu_help.addAction('about...') # 返回一个动作对象
		act_about.triggered.connect(self.about) # 连接的是定义的函数
		act_aboutqt = menu_help.addAction('aboutqt')
		act_aboutqt.triggered.connect(self.aboutqt)
		
		# 状态栏
		self.statusBar().showMessage('程序已就绪...')
		self.show()

	def about(self):
		QMessageBox.about(self,'about this software','wise system')

	def aboutqt(self):
		QMessageBox.abouQt(self)

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
mainwindow = MainWindow()

# mainwindow.show() # 显示窗体, initUI中的self.show()取代了这个

sys.exit(myapp.exec_()) # 窗体退出函数

