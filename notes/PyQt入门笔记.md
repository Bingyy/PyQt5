### 一、检查安装情况

```python
 from PyQt5.QtCore import QT_VERSION_STR
 print(QT_VERSION_STR)
```



### 二、基础知识



#### 大纲：

1. 窗口
2. 图标
3. 弹出信息提示
4. 关闭窗体时询问
5. 屏幕居中显示窗体
6. QMainWindow类
   1. 状态栏
   2. 菜单栏
   3. 信号-槽机制

1.**窗口**



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



2.**加上图标**

```python
# Time: 20180514
# Author: BEING -- notes from 《PyQt5入门》
# useage: Free to use 

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication

class MyWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.resize(800,600) 
		self.setWindowTitle('myapp') # 设置窗口标题
		self.setWindowIcon(QIcon('icons/lion.png')) # QIcon类实例
        
myapp = QApplication(sys.argv) # 任何窗口程序都需要一个QApplication实例
mywidget = MyWidget()
mywidget.show() # 显示窗体
sys.exit(myapp.exec_()) # 窗体退出函数
```

但是我在MAC上并没看到图标显示！！



3.**弹出信息提示**

```python
# Time: 20180514
# Author: BEING -- notes from 《PyQt5入门》
# useage: Free to use 

'''
在窗体停留一段时间，弹出信息提示

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
        
myapp = QApplication(sys.argv) # 任何窗口程序都需要一个QApplication实例
mywidget = MyWidget()
mywidget.show() # 显示窗体
sys.exit(myapp.exec_()) # 窗体退出函数
```



4.**关闭窗口事件处理函数**

```python
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
```

5.**窗体居中显示**

```python
# Time: 20180514
# Author: BEING -- notes from 《PyQt5入门》
# useage: Free to use 

'''
窗体居中显示
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
		self.center() # 调用窗体居中显示函数
		# QToolTip.setFont(QFont('苹方简',12))
		QToolTip.setFont(QFont('微软雅黑',12)) # 设置字体，似乎并没变化，有待纠正

	# 定义关闭事件函数
	def closeEvent(self,event):

		reply = QMessageBox.question(self, '信息','确定退出？',QMessageBox.Yes, QMessageBox.No)
		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

	# 窗体居中显示
	def center(self):
		screen = QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

myapp = QApplication(sys.argv) # 任何窗口程序都需要一个QApplication实例
mywidget = MyWidget()
mywidget.show() # 显示窗体
sys.exit(myapp.exec_()) # 窗体退出函数
```

整个`center`函数的作用效果就是窗体在屏幕上居中显示。



6.**QMainWindow类**

上面用的都是`QWidget`，而`QMainWindow`能够提供应用程序主窗口。二者的区别是：

- QWidget是所有可画类的基础，任何基于QWidget的类都可以作为独立窗体显示而不需要母体
- QMainWindow是针对主窗体的一般需求设计的，预定义了菜单栏，状态栏和其他的widget，QMainWindow继承自QWidget，前面的属性也一样适用。

```python
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
		self.setGeometry(0,0,800,600) # 设定坐标为0,0，大小为800,600
		self.setWindowTitle('myapp') # 设置窗口标题
		self.setToolTip('What are u staring at?') # 设置弹出的文本
		self.center()
		# QToolTip.setFont(QFont('苹方简',12))
		QToolTip.setFont(QFont('微软雅黑',12)) # 设置字体，似乎并没变化，有待纠正

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
mainwindow = MyWindow()
mainwindow.show() # 显示窗体

mainwindow.statusBar().showMessage('程序已就绪...') # 显示状态栏，在底部

sys.exit(myapp.exec_()) # 窗体退出函数

```

只是把继承的父类改成了`QMainWindow`，运行起来效果一样。



**添加菜单栏**



通过`QMainWindow`的`.menuBar`方法拿到一个菜单栏对象，接着用这个对象的`addMenu`方法创建新的菜单对象`QMenu`类，接受的参数是菜单显示文本。

紧接着可以给菜单对象加上动作，通过调用**菜单对象**的`addAction`方法。



**信号-槽机制**

某个对象发出某个信号，用`connect`将这个信号和某个槽（或者自己定义的某个函数）连接起来形成一个反射弧。



