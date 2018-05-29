学习案例中的布局是在`QWidget`上使用的，而在我自己的案例中，用到的是`QMainWindow`，当我试图同样在`initUI`函数中用：

`self.setLayout(grid)`设置布局时，发现并不能起到相应的效果。

查了资料发现，需要特别实例化一个新的`QWidget`,然后将其赋予给`QMainWindow`，然后布局也要赋给`QWidget`.

```python
def initUI(self):
	grid = QGridLayout()
	grid.setSpacing(8) 

    # 在MainWinWow上使用GridLayout
	new_widget = QWidget()
	new_widget.setLayout(grid)
	self.setCentralWidget(new_widget)
```



```python
palette = QPalette()
		palette.setBrush(self.backgroundRole(),QBrush(QPixmap('images/map.png'))) 
self.setPalette(palette)
```

上面这种写法可以加载图片作为窗体程序背景。

```python
pixmap = QPixmap('images/map.png')
lbl = QLabel()
lbl.setPixmap(pixmap)
ver.addWidget(lbl)
```

这种也能够放置图片，但是不能放大缩小窗体，大小被固定了。

### 关于嵌套布局

https://www.cnblogs.com/hhh5460/p/5173645.html

多个选择的Button，可以用QCombox代替。

