#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication

# 继承自QObject的对象能够发送信号
class Communicate(QObject):
    
    closeApp = pyqtSignal() # 信号，信号绑定到槽，不是对象绑定到槽

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):      

        self.c = Communicate() # 实例化
        self.c.closeApp.connect(self.close) # 槽是自带的，信号自己发送的     
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()
        
    # 点击任意窗体程序位置鼠标时发送信号  
    def mousePressEvent(self, event):
        
        self.c.closeApp.emit()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
