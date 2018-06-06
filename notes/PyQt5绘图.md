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
# colors_20180603.py
"""
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

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# pens_20180603.py
"""
ZetCode PyQt5 tutorial 

In this example we draw 6 lines using
different pen styles. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('Pen styles')
        self.show()
        
    # 框架自动触发执行的函数
    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()
        
        
    def drawLines(self, qp):
        
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.DashLine) # 设置画笔风格
        qp.setPen(pen)
        qp.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(20, 160, 250, 160)

        pen.setStyle(Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 200, 250, 200)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen)
        qp.drawLine(20, 240, 250, 240)
              
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

这部分是比较直接且易懂的，直接参考示例即可用起来了。

### `QBrush`

`QBrush`也是基础的图像工具。用于绘制图形形状。比如长方形，圆形，多边形等。画笔可以有三种：

- 预定义画笔
- 渐变画笔
- 纹理画笔

PS.关于`Painter already active`提示的原因：

```python
def paintEvent(self, e):
    qp = QPainter(self) # 1
    qp.begin(self) # 2
    self.drawBrushes(qp)
    qp.end()
```

如果`1`处有了`self`，则不用再有`begin/end`. 同时出现的话，就会出现上面的提示，当然是在终端提示的啦。

````python
painter.setBrush(Qt.white)
brush = QBrush(Qt.SolidPattern) # 定义画笔
qp.setBrush(brush)
qp.drawRect(10, 15, 90, 60)
````

这里和上面的`QPen`案例相似，**颜色**可以做画线条的`Pen`，也可以做画颜色块的`Brush`，区别在于赋予角色时：`setPen/setBrush`的选择了。

显式定义`QPen`,`QBrush`的方法可以更加精细化定义想要的效果。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This example draws nine rectangles in different
brush styles.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.setGeometry(300, 300, 355, 280)
        self.setWindowTitle('Brushes')
        self.show()
        

    def paintEvent(self, e):

        qp = QPainter(self)
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()
        
        
    def drawBrushes(self, qp):
      
        brush = QBrush(Qt.SolidPattern) # 定义画笔
        qp.setBrush(brush)
        qp.drawRect(10, 15, 90, 60)

        brush.setStyle(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 15, 90, 60)

        brush.setStyle(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 15, 90, 60)

        brush.setStyle(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)

        brush.setStyle(Qt.Dense5Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 105, 90, 60)

        brush.setStyle(Qt.Dense6Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 105, 90, 60)

        brush.setStyle(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 195, 90, 60)

        brush.setStyle(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRect(130, 195, 90, 60)

        brush.setStyle(Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawRect(250, 195, 90, 60)
                    
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

不过这里例子里，并没有改变颜色，可以在定义画笔时同时定义颜色。

PS. `QPainter`是个画板。画板上有什么是我们自己来定义的，这也是《黑客与画家》的另一个注解吧。

### `QPainterPath`

绘制贝塞尔曲线。

