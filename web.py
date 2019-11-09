import sys, os, time
from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebChannel import *
from PyQt5.QtWebEngine import *
from PyQt5.QtWebSockets import *


class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://duckduckgo.com/"))
        self.setCentralWidget(self.browser)
        self.browser.loadStarted.connect(self.loadStartedHandler)
        self.browser.loadProgress.connect(self.loadProgressHandler)
        self.browser.loadFinished.connect(self.loadFinishedHandler)
        
        navtb = QToolBar("Navigation")
        navtb.setIconSize(QSize(250, 250))
        navtb.setFixedHeight(50)
        self.addToolBar(navtb)

        self.proxy = QtNetwork.QNetworkProxy()

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 15)
        self.textbox.resize(500,20)

        self.textboxproxyip = QLineEdit(self)
        self.textboxproxyip.move(740, 15)
        self.textboxproxyip.resize(300,20)
        
        self.textboxproxyport = QLineEdit(self)
        self.textboxproxyport.move(1200, 15)
        self.textboxproxyport.resize(100,20)

        self.label1 = QLabel(self)
        self.label1.move(1300, 10)
        self.label1.setText("Port")

        self.label2 = QLabel(self)
        self.label2.move(1050, 10)
        self.label2.setText("ip")

        self.button_reloadproxy = QPushButton('Reload Proxy', self)
        self.button_reloadproxy.move(1600,10)

        self.button_proxyhttp = QPushButton('H', self)
        self.button_proxyhttp.move(1600,50)
        self.button_proxyhttp.resize(30,30)
        
        self.button_proxysocks5 = QPushButton('S5', self)
        self.button_proxysocks5.move(1630,50)
        self.button_proxysocks5.resize(30,30)

        self.button_proxychttp = QPushButton('CH', self)
        self.button_proxychttp.move(1660,50)
        self.button_proxychttp.resize(30,30)
        
        self.button_proxydefault = QPushButton('D', self)
        self.button_proxydefault.move(1690,50)
        self.button_proxydefault.resize(30,30)

        self.button_noproxy = QPushButton('NP', self)
        self.button_noproxy.move(1720,50)
        self.button_noproxy.resize(30,30)

        self.button_search = QPushButton('Enter', self)
        self.button_search.move(530,10)

        self.button_back = QPushButton('Back', self)
        self.button_back.move(630,10)
        
        self.button_search.clicked.connect(self.on_click_button_search)
        self.button_back.clicked.connect(self.on_click_button_back)
        self.button_reloadproxy.clicked.connect(self.on_click_button_reloadproxy)
        self.button_proxyhttp.clicked.connect(self.on_click_button_proxyhttp)
        self.button_proxysocks5.clicked.connect(self.on_click_button_proxysocks5)
        self.button_proxychttp.clicked.connect(self.on_click_button_proxychttp)
        self.button_proxydefault.clicked.connect(self.on_click_button_proxydefault)
        self.button_noproxy.clicked.connect(self.on_click_button_noproxy)

        self.show()


    @QtCore.pyqtSlot()
    def loadStartedHandler(self):
        print(time.time(), ": load started")

    @QtCore.pyqtSlot(int)
    def loadProgressHandler(self, prog):
        print(time.time(), ":load progress", prog)

    @QtCore.pyqtSlot()
    def loadFinishedHandler(self):
        print(time.time(), ": load finished")

    def on_click_button_search(self):
        textboxValue = self.textbox.text()
        if 'http' in textboxValue:
            self.browser.setUrl(QUrl(textboxValue))
        
        if not 'http' in textboxValue:
            self.browser.setUrl(QUrl("http://"+textboxValue))

    def on_click_button_reloadproxy(self):

        textboxproxyipValue = self.textboxproxyip.text()
        textboxproxyportValue = self.textboxproxyport.text()
        
        self.proxy.setHostName(textboxproxyipValue)
        self.proxy.setPort(int(textboxproxyportValue))
        
        QtNetwork.QNetworkProxy.setApplicationProxy(self.proxy)
        
        print(textboxproxyipValue)
        print(textboxproxyportValue)

    def on_click_button_back(self):
        self.browser.back()
    
    def on_click_button_proxyhttp(self):
        self.proxy.setType(QtNetwork.QNetworkProxy.HttpProxy)
        QtNetwork.QNetworkProxy.setApplicationProxy(self.proxy)
        print("http")
    
    def on_click_button_proxysocks5(self):
        self.proxy.setType(QtNetwork.QNetworkProxy.Socks5Proxy)
        QtNetwork.QNetworkProxy.setApplicationProxy(self.proxy)
        print("socks5")
    
    def on_click_button_proxychttp(self):
        self.proxy.setType(QtNetwork.QNetworkProxy.HttpCachingProxy)
        QtNetwork.QNetworkProxy.setApplicationProxy(self.proxy)
        print("chttp")

    def on_click_button_proxydefault(self):
        self.proxy.setType(QtNetwork.QNetworkProxy.DefaultProxy)
        QtNetwork.QNetworkProxy.setApplicationProxy(self.proxy)
        print("proxydefault")
    
    def on_click_button_noproxy(self):
        self.proxy.setType(QtNetwork.QNetworkProxy.NoProxy)
        QtNetwork.QNetworkProxy.setApplicationProxy(self.proxy)
        print("noproxy")


app = QApplication(sys.argv)

app.setApplicationName("1377 h4xor br0ws3r")
app.setOrganizationName("1377 h4xor br0ws3r")
app.setOrganizationDomain("1377h4xorbr0ws3r.org")

window = MainWindow()

sys.exit(app.exec_())