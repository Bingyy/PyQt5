#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
In this example, we create a bit
more complicated window layout using
the QGridLayout manager. 
'''
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		title = QLabel('Title')
		author = QLabel('Author')
		review = QLabel('Review')

		titleEdit = QLineEdit()
		authorEdit = QLineEdit()
		reviewEdit = QTextEdit()

		grid = QGridLayout()
		grid.setSpacing(10)

		grid.addWidget(title, 0, 0) # 行1列0
		grid.addWidget(titleEdit, 0, 1)

		grid.addWidget(author, 1, 0)
		grid.addWidget(authorEdit, 1, 1)

		grid.addWidget(review, 2, 0)
		grid.addWidget(reviewEdit, 2, 1, 5, 1) # 占据空间：5行，1列

		self.setLayout(grid) # 在Widget上使用grid布局
		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle('Review')
		self.show()
if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = Example()
	sys.exit(app.exec_())



