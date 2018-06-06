使用PyInstaller打包生成可执行文件，只能在和打包机器系统相同的环境下运行，所以这个可执行文件不具有可移植性，只是代码具有而已。

`pip install pyinstaller`

`pyinstaller -F -w entrance.py` # 指定入口文件，会在当前目录下新建`dist`文件夹，生成对应的可执行文件。

