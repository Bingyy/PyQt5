#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI() # 初始化UI

	def initUI(self):
		self.setGeometry(300,300,250,150)
		self.setWindowTitle('Event Handler')
		self.show()

	# 这种做法没有显示绑定槽
	def keyPressEvent(self,e):
		if e.key() == Qt.Key_Escape:
			self.close()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
