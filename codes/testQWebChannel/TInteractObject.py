from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

# 定义的是数据通信对象
class TInteractObj(QObject):

    SigReceivedMessFromJS = pyqtSignal(str)

    SigSendMessageToJS = pyqtSignal(list) # 括号内是传递数据类型

    def __init__(self, parent = None):
        super().__init__(parent)
        self.testString = "Hello World"

    # 在js中调用的必须是槽函数
    @pyqtSlot(str)
    def JSSendMessage(self, strParameter):
        # 这个形参在js代码中赋值，所以是从js往python传递数据
        print('JSSendMessage(%s) from Html' % strParameter)
        self.SigReceivedMessFromJS.emit(strParameter)

    @pyqtSlot(result=str)
    def fun(self):
        print('TInteractObj.fun()')
        return 'hello'