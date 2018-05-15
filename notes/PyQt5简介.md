### PyQt5是啥

参考链接：https://maicss.gitbooks.io/pyqt5/content/hello_world.html

Python的一个库，有620个类和6000个函数。**是一个跨平台的工具包。**

类别分为：

- QtCore
- QtGui
- QtWidgets
- QtMultimedia
- QtBluetooth
- QtNetwork
- QtPositioning
- Enginio
- QtWebSockets
- QtWebKit
- QtWebKitWidgets
- QtXml
- QtSvg
- QtSql
- QtTest



**QtCore**: 包含了核心的非GUI功能。此模块用于处理时间、文件和目录、各种数据类型、流、URL、MIME类型、线程或进程。

 **QtGui**: 包含类窗口系统集成、事件处理、二维图形、基本成像、字体和文本。 qtwidgets模块包含创造经典桌面风格的用户界面提供了一套UI元素的类。 

**QtMultimedia**: 包含的类来处理多媒体内容和API来访问相机和收音机的功能。 

**QtBluetooth**: 模块包含类的扫描设备和连接并与他们互动。

**QtNetwork**: 描述模块包含了网络编程的类。这些类便于TCP和IP和UDP客户端和服务器的编码，使网络编程更容易和更便携。

**QtPositioning**: 包含类的利用各种可能的来源，确定位置，包括卫星、Wi-Fi、或一个文本文件。

**Enginio**: 模块实现了客户端库访问Qt云服务托管的应用程序运行时。 **Qtwebsockets**: 模块包含实现WebSocket协议类。 

**QtWebKit**:包含一个基于Webkit2图书馆Web浏览器实现类。 

**Qtwebkitwidgets**: 包含的类的基础webkit1一用于qtwidgets应用Web浏览器的实现。 

**QtXml**: 包含与XML文件的类。这个模块为SAX和DOM API提供了实现。 

**QtSvg**: 模块提供了显示SVG文件内容的类。可伸缩矢量图形（SVG）是一种描述二维图形和图形应用的语言。 

**QtSql**: 模块提供操作数据库的类。 

**QtTest**:包含的功能，使pyqt5应用程序的单元测试.



没有父级的构造器被称之为窗口。

`move`用于修改控件位置。

控件创建后，将进入应用的主循环，事件处理器开始工作。

> 主循环从窗口上接收事件，并把事件派发到应用控件里。直到调用`exit()`方法或直接销毁主控件时，主循环结束。`sys.exit(myapp.exec_())`方法保证主循环安全退出。`exec_`方法带个下划线的原因是`exec`是`Python`的关键字。



#### 应用图标

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
	# 初始化界面
    def initUI(self):

        self.setGeometry(300, 300, 300, 220) # 是resize和move的结合体
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png')) # 设置应用图标     
        
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```



虽然这些都在入门那个笔记中有写到，重复一下也算是加深印象。

具体细节不必在开始是这么深究，而是要从大局出发，多写写，多复用，就自然水到渠成。



#### QPushButton

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        qbtn = QPushButton('Quit', self) # 在当前Widget上放一个按钮
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)       

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')    
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```



其中，`QPushButton(string text, QWidget parent = None)`。

`text`参数是想要显示的按钮名称，`parent`参数是放按钮的组件。



#### 信号-槽机制，Signal & Slot机制

比如，按钮被点击，点击信号被释放，槽即函数会被调用。Slot可以是Qt自带的或者是任何可调用的Python函数。

注意看这个`QCoreApplication.instance()`包含主事件循环，处理并分发所有的事件。

### Message Box

这个在入门的笔记里也有写过，这里再重复一下。

```python
import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):               
        
        self.setGeometry(300, 300, 250, 150)        
        self.setWindowTitle('Message box')    
        self.show()
        
        
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```



http://zetcode.com/gui/pyqt5/firstprograms/



