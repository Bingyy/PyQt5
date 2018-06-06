from PyQt5.QtWidgets import QDialog, QPlainTextEdit, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebChannel import *
from PyQt5.QtCore import QUrl, pyqtSignal

from TInteractObject import TInteractObj

import os

class TMainWindow(QDialog):

    SigSendMessageToJS = pyqtSignal(list) # 定义了一个发送信号的对象，这个和交互对象中的同名，但不是同一个

    def __init__(self, parent = None):
        super().__init__(parent)
        #---Qt widget and layout---
        self.mpQtContentTextEdit = QPlainTextEdit(self)
        self.mpQtContentTextEdit.setMidLineWidth(400)
        self.mpQtContentTextEdit.setReadOnly(True)

        self.mpQtSendLineEdit = QLineEdit(self)

        self.mpQtSendBtnByInteractObj = QPushButton('Send', self)
        self.mpQtSendBtnByInteractObj.setToolTip('Send message by Interact object style')

        self.mpQtSendBtnByJavaScript = QPushButton('Send2', self)
        self.mpQtSendBtnByJavaScript.setToolTip('Send message by runJavaScript style')

        self.pQtSendHLayout = QHBoxLayout()
        self.pQtSendHLayout.setSpacing(0)
        self.pQtSendHLayout.addWidget(self.mpQtSendLineEdit)
        self.pQtSendHLayout.addSpacing(5)
        self.pQtSendHLayout.addWidget(self.mpQtSendBtnByInteractObj)
        self.pQtSendHLayout.addSpacing(5)
        self.pQtSendHLayout.addWidget(self.mpQtSendBtnByJavaScript)

        self.pQtTotalVLayout = QVBoxLayout()
        self.pQtTotalVLayout.setSpacing(0)
        self.pQtTotalVLayout.addWidget(self.mpQtContentTextEdit)
        self.pQtTotalVLayout.setSpacing(5)
        self.pQtTotalVLayout.addLayout(self.pQtSendHLayout)

        self.pQtGroup = QGroupBox('Qt View', self)
        self.pQtGroup.setLayout(self.pQtTotalVLayout)

        #---Web widget and layout---
        self.mpJSWebView = QWebEngineView(self)
        self.pWebChannel = QWebChannel(self.mpJSWebView.page())
        self.pInteractObj = TInteractObj(self) # 实例化交互对象
        
        self.pWebChannel.registerObject("interactObj", self.pInteractObj)

        self.mpJSWebView.page().setWebChannel(self.pWebChannel)

        # 使用os加载html界面
        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "JSTest.html"))
        self.local_url = QUrl.fromLocalFile(self.file_path)

        # self.url = 'file:///D:/PyPro/PyQtJSInteract/JSTest.html'

        self.mpJSWebView.page().load(QUrl(self.local_url))
        self.mpJSWebView.show()

        self.pJSTotalVLayout = QVBoxLayout()
        self.pJSTotalVLayout.setSpacing(0)
        self.pJSTotalVLayout.addWidget(self.mpJSWebView)
        self.pWebGroup = QGroupBox('Web View', self)
        self.pWebGroup.setLayout(self.pJSTotalVLayout)

        #---TMainWindow total layout---
        self.mainLayout = QHBoxLayout()
        self.mainLayout.setSpacing(0)
        self.mainLayout.addWidget(self.pQtGroup)
        self.mainLayout.setSpacing(5)
        self.mainLayout.addWidget(self.pWebGroup)
        self.setLayout(self.mainLayout)
        self.setMinimumSize(1130, 680)

        self.mpQtSendBtnByInteractObj.clicked.connect(self.OnSendMessageByInteractObj)
       
        self.mpQtSendBtnByJavaScript.clicked.connect(self.OnSendMessageByJavaScript)
        
        self.pInteractObj.SigReceivedMessFromJS.connect(self.OnReceiveMessageFromJS)
        
        # 信号绑定
        self.SigSendMessageToJS.connect(self.pInteractObj.SigSendMessageToJS)

    def OnReceiveMessageFromJS(self, strParameter):
        print('OnReceiveMessageFromJS()')
        if not strParameter:
            return
        self.mpQtContentTextEdit.appendPlainText(strParameter)

    # Python对象向JS发送数据
    def OnSendMessageByInteractObj(self):

        strMessage = self.mpQtSendLineEdit.text() # Python获取用户输入
        if not strMessage:
            return
        self.SigSendMessageToJS.emit([[1,2,3,4],[5,6,7,8]]) # 发送信号，发送信号带有数据

    def OnSendMessageByJavaScript(self):
        strMessage = self.mpQtSendLineEdit.text()
        if not strMessage:
            return
        strMessage = 'Received string from Qt:' + strMessage
        self.mpJSWebView.page().runJavaScript("output(%s)" %strMessage)
        self.mpJSWebView.page().runJavaScript("showAlert()")

