### `QPixmap`

用于处理图像的控件，为图片的显示做过优化。

Off-Screen Rendering: 离屏渲染，GPU在当前屏幕缓冲区以外开辟一个缓冲区进行渲染操作。

### `QPainter`

用于在组件上执行低层次的绘制操作，几乎可以用来绘制任何东西。从简单的线条到复杂的形状，都能做。

#### `paintEvent`

绘制操作的真正执行者是`paintEvent()`方法。

画画的代码放在：`begin()`和`end()`之间，这两个方法是`QPainter`对象的方法。

```python
def paintEvent(self):
    painter = QPainter() # 实例化绘制工程
    painter.begin(self) # 开始绘制
    
    painter.drawText(xxx) # 执行绘制
    
    painter.end() # 结束绘制,注意这里没有self,加上的话会报错
```

`setPen`和`setBrush`的区别是什么？

如何能让加载的图像不被压缩？

如何能让界面适应图片的大小？

https://doc.qt.io/qt-5/qwidget.html 

https://wiki.python.org/moin/PyQt/Creating%20a%20widget%20with%20a%20fixed%20aspect%20ratio 应该是这一篇



#### 固定窗体缩放比例

`MainWindow.resize(760,440)`

`MainWindow.setFixedSize(760,440)` 

固定尺寸

**目前还是没有搞定如何设定缩放只能等比缩放的问题。**

每次我们`resize`了窗体大小，`paint event`被触发。

### `Colors`

用于表示颜色的对象。

`setPen`和`setBrush`的区别，很简单，前者控制线条，后者控制大块颜色填充。这就像`stroke`和`fill`的区别。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
colors_20180603.py
ZetCode PyQt5 tutorial 

This example draws three rectangles in three
#different colours. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()    
        self.initUI()  
        
    def initUI(self):      
        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Colours')
        self.show()

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

        
    def drawRectangles(self, qp):
      
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col) # 设置边缘线颜色

        qp.setBrush(QColor(200, 0, 0)) # 设置填充颜色
        qp.drawRect(10, 15, 90, 60)

        qp.setBrush(QColor(255, 80, 0, 160))
        qp.drawRect(130, 15, 90, 60)

        qp.setBrush(QColor(25, 0, 90, 200))
        qp.drawRect(250, 15, 90, 60)
              
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```



### `QPen`

对比两个点：

```python
pen = QPen(Qt.black, 2, Qt.SolidLine)
qp.setPen(pen)

col = QColor(0, 0, 0)
col.setNamedColor('#d4d4d4')
qp.setPen(col) # 设置边缘线颜色
```



一个是`QPen`实例，可以将其设置到`QPainter`上，而另一个是铜鼓欧颜色对象定义，和`QPen`一样用在`QPainter`上。



### `QBrush`

### `QPainterPath`

绘制贝塞尔曲线。