### `QPixmap`是什么

`QPixmap`是用于处理图片的组件，是经过优化的用于在屏幕上显示图片的组件。

```python
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, 
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()   
        
    def initUI(self):      

        hbox = QHBoxLayout(self)
        pixmap = QPixmap("images/Rocket.png")

        # 通过label来显示
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)
        
        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()        
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

依托于`QLabel`，在此组件上画图。

使用的水平布局组件，布局组件上添加了`QLabel`组件。

