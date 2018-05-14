### 一、检查安装情况

```python
 from PyQt5.QtCore import QT_VERSION_STR
 print(QT_VERSION_STR)
```



### 二、基础知识

**窗口**



```python
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyWidget(QWidget):
    def __init__(self):
		super().__init__()
        self.setGeometry(0,0,800,600) # 设定坐标为0,0，大小为800,600
        self.setWindowTitle('myapp')
        
myapp = QApplication(sys.argv) # 任何窗口程序都需要一个QApplication实例
mywidget = MyWidget()
mywidget.show() # 显示窗体
sys.exit(myapp.exec_())
```



