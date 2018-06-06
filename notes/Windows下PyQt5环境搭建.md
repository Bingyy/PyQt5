### 安装环境

- Anaconda3 --> Python3.6
- PyQt5
- Qt(支撑PyQt5)
- PyInstaller -- 服务器端不需要，只要能执行即可

### 1.Python安装

直接通过Anaconda满足即可。

### 2.PyQt5安装

`pip install PyQt5 -i https://pypi.douban.com/simple`

`pip install PyQt5-tools -i https://pypi.douban.com/simple 

这样就好了，比在MacOS下还要简单很多~~

为了打包，可以使用`pip install pyinstaller`

执行打包: `pyinstaller -F -w entrance.py`

**如何制作组合指令？？**

通过Designer画出界面并通过`pyinstaller`打包出去的程序是可以正常运行的，而自己写的总是出现一堆问题。