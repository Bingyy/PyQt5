from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,os
class SelectDialog(QDialog):
    def __init__(self, parent=None):
        super(SelectDialog, self).__init__(parent)
        self.path = os.getcwd()
        self.initUI()
        self.setWindowTitle("选择")
        self.resize(240, 100)
    def initUI(self):
        grid = QGridLayout()
        grid.addWidget(QLabel("路径："), 0, 0)
        self.pathLineEdit = QLineEdit()
        self.pathLineEdit.setFixedWidth(200)
        self.pathLineEdit.setText(self.path)
        grid.addWidget(self.pathLineEdit, 0, 1)
        button = QPushButton("更改")
        button.clicked.connect(self.changePath)
        grid.addWidget(button, 0, 2)
        
        buttonBox = QDialogButtonBox()
        buttonBox.setOrientation(Qt.Horizontal)  # 设置为水平方向
        buttonBox.setStandardButtons(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)  # 确定
        buttonBox.rejected.connect(self.reject)  # 取消
        grid.addWidget(buttonBox, 2, 1)
        self.setLayout(grid)
    def changePath(self):
        open = QFileDialog()
        self.path=open.getOpenFileName()
        print(self.path)
        #self.path = open.getExistingDirectory()
        self.pathLineEdit.setText(self.path[0])
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = SelectDialog()
    if dialog.exec_():
        pass