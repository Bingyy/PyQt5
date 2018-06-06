#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys,os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject, pyqtSlot, QUrl
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView

class CallHandler(QObject):

    @pyqtSlot(result=list)
    def myHello(self):
        print('call received')
        return [123,456]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    view = QWebEngineView()
    channel = QWebChannel()
    handler = CallHandler()
    channel.registerObject('pyjs', handler)
    view.page().setWebChannel(channel) 

    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "index.html"))
    local_url = QUrl.fromLocalFile(file_path)

    view.load(QUrl(local_url))
    view.show()
    sys.exit(app.exec_())