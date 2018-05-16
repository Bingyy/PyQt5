#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):    

        self.menuBar().setNativeMenuBar(False) # 加上这句就有Windows下的显示了~

        # 创建子项动作，需要绑定到菜单
        exitAct = QAction(QIcon('icons/exit.png'), '&Exit', self)        
        exitAct.setShortcut('Ctrl+Q') # 设定快捷键
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit) # 绑定的槽是ctrl+q退出，Mac下是cmd+q

        self.statusBar().showMessage('准备好了~')

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Simple menu')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())