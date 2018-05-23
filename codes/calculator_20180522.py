#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
In this example, we create a skeleton
of a calculator using QGridLayout.
'''
import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication

class Calculator(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		grid = QGridLayout() #布局类
		self.setLayout(grid)

		names = ['Cls', 'Bck', '', 'Close', 
				'7', '8', '9', '/',
				'4', '5', '6', '*',
				'1', '2', '3', '-',
				'0', '.', '=', '+']
		positions = [(i,j) for i in range(5) for j in range(4)] # 5行4列

		for position, name in zip(positions, names): # 按照行列序号
			if name == '':
				continue
			button = QPushButton(name)
			grid.addWidget(button, *position)
		
		self.move(300,150)
		self.setWindowTitle('Calculator')
		self.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	calculator = Calculator()
	sys.exit(app.exec_())
