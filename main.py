# -*- coding: utf-8 -*-
'''
Author: David J. Morfe
Application Name: ManageCraft
Functionality Purpose: A Minecraft Server Manager Application
Version: 0.0.1
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
from PyQt5.QtWidgets import QStatusBar, QToolBar
from PyQt5.QtWidgets import QLabel, QPushButton, QRadioButton, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout
from PyQt5.QtCore import Qt
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

        self.frame0 = QFrame(self.centralWidget()); self.frame0.setFixedSize(1024, 540)
        self.frame1 = QFrame(self.centralWidget()); self.frame1.hide(); self.frame1.setFixedSize(1024, 540)
        self.frame2 = QFrame(self.centralWidget()); self.frame2.hide(); self.frame2.setFixedSize(1024, 540)
        self.frame3 = QFrame(self.centralWidget()); self.frame3.hide(); self.frame3.setFixedSize(1024, 540)
        self._createLoginScreen()
        self.mainMenu = True; self.tools = None

        self.client = None


    def __returnTo(self, frame, prev):
        prev.hide()
        frame.show()
    def __DC(self):
        self.removeToolBar(self.tools)
        self.frame1.close()
        self.frame2.close()
        self.frame3.close()
        self.frame0.show()
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
        self.tools = QToolBar()
        self.addToolBar(self.tools)
        self.tools.addAction("CONFIGURATION", self.close)
        self.tools.addAction("STATUS", self.close)
    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("Server Status: Online / Offline")
        self.setStatusBar(status)
    def _createLoginScreen(self):
        vLayout = QVBoxLayout(self.centralWidget()); vLayout.setAlignment(Qt.AlignTop)
        hLayout = QHBoxLayout(self.centralWidget()); hLayout.setSpacing(0)
        hLayout.setAlignment(Qt.AlignHCenter)
        formLayout = QFormLayout(self.centralWidget()); formLayout.setFormAlignment(Qt.AlignHCenter)
        formLayout.setLabelAlignment(Qt.AlignRight)

        title = QLabel("<h1>MANAGECRAFT</h1>")
        btn1 = QPushButton("REMOTE"); btn1.setFixedSize(170, 40)
        btn1.setCheckable(True); btn1.setChecked(True)
        btn2 = QPushButton("LOCAL"); btn2.setFixedSize(170, 40);
        btn2.setCheckable(True); btn2.setChecked(False)
        btn3 = QPushButton("CONNECT!"); btn3.setFixedSize(200, 50)
        btn1.clicked.connect(self.remote)
        btn2.clicked.connect(self.local)
        btn3.clicked.connect(partial(self.connect,
                                     self.host,
                                     self.user, self.pas))

        formLayout.addRow("Host:", self.host)
        formLayout.addRow("Username:", self.user)
        formLayout.addRow("Password:", self.pas)
        vLayout.addWidget(title, alignment=Qt.AlignCenter)
        hLayout.addWidget(btn1, alignment=Qt.AlignHCenter); hLayout.addWidget(btn2, alignment=Qt.AlignHCenter)
        vLayout.addLayout(hLayout)
        vLayout.addLayout(formLayout)
        vLayout.addWidget(btn3, alignment=Qt.AlignCenter)

        self.frame0.setLayout(vLayout)
        self.mainMenu = False
    def remote(self):
        pass
    def connect(self, host, user, pas): # Pack to config window
        L1 = QLabel("<H2>MANAGECRAFT</h2>", parent=self.frame1)
        self._createToolBar()
        self.frame1.show()
        self.frame0.hide()
        '''client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, port=22, username=user, password=pas)
        self.client = client'''
    def local(self):
        pass
    def browse(self): # Pack to browse window
        pass

if __name__ == "__main__":
    app = QApplication([])
    gui = Window()
    gui.show()
    sys.exit(app.exec())
