# -*- coding: utf-8 -*-
'''
Author: David J. Morfe,
        Antara V. Morfe,
        & Ali E. Khan
Application Name: ManageCraft
Functionality Purpose: A Minecraft Server Manager Application
Version: 0.0.3
'''
#3/19/20

'''
import sys, os, re, time, paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.10.204', username='jake', password='mantabayray51')

stdin, stdout, stderr = client.exec_command('cd /home/jake')
stdin, stdout, stderr = client.exec_command('./test.sh')

for line in stdout:
    print(line.strip('\n'))

client.close()'''

#Local Main Menu Button & self.file input via dialog file explorer

import paramiko
import re, os, sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFrame, QDialog
from PyQt5.QtWidgets import QStatusBar, QToolBar, QButtonGroup
from PyQt5.QtWidgets import QLabel, QPushButton, QRadioButton, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize
from functools import partial

class Window(QMainWindow):
    '''This class instantiates the main gui window'''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ManagerCraft")
        self.setCentralWidget(QWidget())
        self.setGeometry(100, 100, 1024, 540)
        self.setFixedSize(1024, 540)
        self._createMenu()
        self._createStatusBar()

        self.host = QLineEdit(); self.path = QLineEdit()
        self.user = QLineEdit(); self.pas = QLineEdit()
        self.pas.setEchoMode(QLineEdit.Password)
        self.host.setFixedSize(250, 20); self.user.setFixedSize(250, 20); self.pas.setFixedSize(250, 20)
        
        self.frameR = QFrame(self.centralWidget()); self.frameR.setFixedSize(1024, 540)
        self.frameL = QFrame(self.centralWidget()); self.frameL.hide(); self.frameL.setFixedSize(1024, 540)
        self.frameC = QFrame(self.centralWidget()); self.frameC.hide(); self.frameC.setFixedSize(1024, 540)
        self.frameS = QFrame(self.centralWidget()); self.frameS.hide(); self.frameS.setFixedSize(1024, 540)
        self._createFirstScreen()
        self.mainMenu = True; self.tools = None

        self.client = None


    def __returnTo(self, frame, prev):
        prev.hide()
        frame.show()
    def __DC(self):
        self.removeToolBar(self.tools)
        self.frameL.close()
        self.frameC.close()
        self.frameS.close()
        self.frameR.show()
    def __startServer(self, client):
        stdin, stdout, stderr = client.exec_command('systemctl start minecraft')
    def __stopServer(self, client):
        stdin, stdout, stderr = client.exec_command('systemctl stop minecraft')
    def __restartServer(self, client):
        stdin, stdout, stderr = client.exec_command('systemctl restart minecraft')
    def _createMenu(self):
        self.menu = self.menuBar().addMenu("Menu")
        self.menu.addAction("Disconnect", self.__DC)
        self.menu.addAction("Exit", self.close)
    def _createToolBar(self):
        self.tools = QToolBar(); self.tools.setMovable(False)
        self.addToolBar(Qt.LeftToolBarArea, self.tools)
        self.tools.addAction("CONFIGURATION", self.close)
        self.tools.addAction("STATUS", self.close)
    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("Server Status: Online / Offline")
        self.setStatusBar(status)
    def btnPressToggle(self, b, png):
        Png = QIcon(f"./graphics/{png}"); b.setIcon(Png)
        b.setIconSize(QSize(200, 40))

    def _createSecondScreen(self):
        vLayout = QVBoxLayout(self.centralWidget()); vLayout.setAlignment(Qt.AlignTop)
        hLayout = QHBoxLayout(self.centralWidget()); hLayout.setSpacing(0)
        hLayout.setAlignment(Qt.AlignHCenter)
        formLayout = QFormLayout(self.centralWidget()); formLayout.setFormAlignment(Qt.AlignHCenter)
        formLayout.setLabelAlignment(Qt.AlignRight)

        btnGroup = QButtonGroup(); btnGroup.setExclusive(True)
        title = QLabel()
        tPng = QPixmap("./graphics/ManageCraft.png"); title.setPixmap(tPng)
        btn1 = QPushButton(); btn1.setFixedSize(130, 40)
        btn1.setCheckable(True); btn1.setChecked(False)
        rcPng = QIcon("./graphics/RemoteBtn.png"); btn1.setIcon(rcPng)
        btn1.setIconSize(QSize(170, 40))
        btn2 = QPushButton(); btn2.setFixedSize(130, 40);
        btn2.setCheckable(True); btn2.setChecked(True)
        lcPng = QIcon("./graphics/LocalBtnChecked.png"); btn2.setIcon(lcPng)
        btn2.setIconSize(QSize(170, 40))
        btn3 = QPushButton("BROWSE!"); btn3.setFixedSize(200, 50)
        btn1.toggled.connect(self.remote); btnGroup.addButton(btn1)
        btn2.toggled.connect(self.local); btnGroup.addButton(btn2)
        btn3.clicked.connect(self.browse)
        btn1.pressed.connect(partial(self.btnPressToggle, btn1, "RemoteBtnChecked.png"))
        btn1.released.connect(partial(self.btnPressToggle, btn1, "RemoteBtn.png"))

        vLayout.addWidget(title, alignment=Qt.AlignCenter)
        hLayout.addWidget(btn1, alignment=Qt.AlignHCenter); hLayout.addWidget(btn2, alignment=Qt.AlignHCenter)
        vLayout.addLayout(hLayout)
        vLayout.addWidget(btn3, alignment=Qt.AlignCenter)

        self.frameL.setLayout(vLayout)
        self.mainMenu = False
        self.frameL.hide()
    def _createFirstScreen(self):
        vLayout = QVBoxLayout(self.centralWidget()); vLayout.setAlignment(Qt.AlignTop)
        hLayout = QHBoxLayout(self.centralWidget()); hLayout.setSpacing(0)
        hLayout.setAlignment(Qt.AlignHCenter)
        formLayout = QFormLayout(self.centralWidget()); formLayout.setFormAlignment(Qt.AlignHCenter)
        formLayout.setLabelAlignment(Qt.AlignRight)

        btnGroup = QButtonGroup(); btnGroup.setExclusive(True)
        title = QLabel()
        tPng = QPixmap("./graphics/ManageCraft.png"); title.setPixmap(tPng)
        btn1 = QPushButton(); btn1.setFixedSize(130, 40)
        btn1.setCheckable(True); btn1.setChecked(True)
        rcPng = QIcon("./graphics/RemoteBtnChecked.png"); btn1.setIcon(rcPng)
        btn1.setIconSize(QSize(170, 40))
        btn2 = QPushButton(); btn2.setFixedSize(130, 40);
        btn2.setCheckable(True); btn2.setChecked(False)
        lcPng = QIcon("./graphics/LocalBtn.png"); btn2.setIcon(lcPng)
        btn2.setIconSize(QSize(170, 40))
        btn3 = QPushButton(); btn3.setFixedSize(155, 45)
        cPng = QIcon("./graphics/ConnectBtn.png"); btn3.setIcon(cPng)
        btn3.setIconSize(QSize(200, 40))
        btn1.toggled.connect(self.remote); btnGroup.addButton(btn1)
        btn2.toggled.connect(self.local); btnGroup.addButton(btn2)
        btn3.clicked.connect(partial(self.connect,
                                     self.host,
                                     self.user, self.pas))
        btn2.pressed.connect(partial(self.btnPressToggle, btn2, "LocalBtnChecked.png"))
        btn2.released.connect(partial(self.btnPressToggle, btn2, "LocalBtn.png"))
        btn3.pressed.connect(partial(self.btnPressToggle, btn3, "ConnectBtnChecked.png"))
        btn3.released.connect(partial(self.btnPressToggle, btn3, "ConnectBtn.png"))

        formLayout.addRow("Host:", self.host)
        formLayout.addRow("Username:", self.user)
        formLayout.addRow("Password:", self.pas)
        vLayout.addWidget(title, alignment=Qt.AlignCenter)
        hLayout.addWidget(btn1, alignment=Qt.AlignHCenter); hLayout.addWidget(btn2, alignment=Qt.AlignHCenter)
        vLayout.addLayout(hLayout)
        vLayout.addLayout(formLayout)
        vLayout.addWidget(btn3, alignment=Qt.AlignCenter)

        self.frameR.setLayout(vLayout)
        self.mainMenu = False
        self._createSecondScreen()
    def remote(self):
        if self.frameR.isVisible():
            pass
        else:
            self.frameL.hide()
            self.frameR.show()
    def connect(self, host, user, pas): # Pack to config window
        title = QLabel(self.frameC)
        tPng = QPixmap("./graphics/ManageCraft.png"); tPng = tPng.scaled(450, 150, Qt.KeepAspectRatio); title.setPixmap(tPng);
        self._createToolBar()
        self.frameC.show()
        self.frameR.hide()
        '''client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, port=22, username=user, password=pas)
        self.client = client'''
    def local(self):
        if self.frameL.isVisible():
            pass
        else:
            self.frameR.hide()
            self.frameL.show()
    def browse(self): # Pack to browse window
        pass

if __name__ == "__main__":
    app = QApplication([])
    gui = Window()
    gui.show()
    sys.exit(app.exec())
