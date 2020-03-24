# -*- coding: utf-8 -*-
'''
Author: David J. Morfe,
        Antara V. Morfe,
        & Ali E. Khan
Application Name: ManageCraft
Functionality Purpose: A Minecraft Server Manager Application
Version: 0.0.7
'''
#3/24/20


'''import sys, os, re, time, paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=pas)

stdin, stdout, stderr = client.exec_command('pwd')

for line in stdout:
    print(line.strip('\n'))

client.close()'''

#Get server directory path for remote
  #Send commands to server for each file path changed
  #Get pwd, and ls -d */ and next child folders
#Run paramiko connection test to build exception handler
#Account for server shutdown mid-use

import paramiko, socket
import re, os, sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFrame, QDialog
from PyQt5.QtWidgets import QStatusBar, QToolBar, QButtonGroup, QFileDialog
from PyQt5.QtWidgets import QLabel, QPushButton, QRadioButton, QLineEdit, QDialog
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt, QSize
from functools import partial
from BLBrowser import UI_Dialog
from FrameTest import UI

class Window(QMainWindow):
    '''This class instantiates the main gui window'''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ManagerCraft")
        self.setCentralWidget(QWidget())
        self.styleFrame = QFrame(self.centralWidget()); self.styleFrame.setFixedSize(1024, 500)
        self.styleFrame.setStyleSheet("border-image: url(./graphics/WindowFrame.png);\
background-image: url(./graphics/Frame_R.png); background-repeat: no-repeat;")
        self.setGeometry(100, 100, 1024, 540)
        self.setFixedSize(1024, 540)
        self._createMenu()
        self._createStatusBar()

        font = QFont("Minecrafter", 22)

        self.host = QLineEdit(); self.path = QLineEdit()
        self.user = QLineEdit(); self.pas = QLineEdit()
        self.host.setFont(font); #self.path.setFont(font)
        self.user.setFont(font); self.pas.setFont(font)
        self.pas.setEchoMode(QLineEdit.Password)
        self.host.setFixedSize(250, 50); self.path.setFixedSize(350, 35)
        self.user.setFixedSize(250, 50); self.pas.setFixedSize(250, 50)


        self.dialog = QDialog(self.centralWidget(), Qt.WindowTitleHint|Qt.WindowSystemMenuHint)
        self.dialog.setModal(True)
        self.dui = UI_Dialog(); self.dui.setupUi(self.dialog)
        self.frameR = QFrame(self.centralWidget()); self.frameR.setFixedSize(1024, 540)
        self.frameL = QFrame(self.centralWidget()); self.frameL.hide(); self.frameL.setFixedSize(1024, 540)
        self.frameC = QFrame(self.centralWidget()); self.frameC.hide(); self.frameC.setFixedSize(1024, 540)
        self.frameS = QFrame(self.centralWidget()); self.frameS.hide(); self.frameS.setFixedSize(1024, 540)
        self.err = QLabel("<h2><font color='red'>Error: Invalid Input! Try again!</font></h2>", parent=self.frameR)
        self.err.hide()
        self.ui = UI(); self.ui.setupUi(self.frameC)
        self._createFirstScreen()
        self.mainMenu = True; self.tools = None; self.status = None

        self.client = None

    def __returnTo(self, frame, prev):
        prev.hide()
        frame.show()
    def __DC(self):
        try:
            self.client.close()
        except AttributeError:
            pass
        self.removeToolBar(self.tools)
        self.frameL.close()
        self.frameC.close()
        self.frameS.close()
        self.frameR.show()
    def __startServer(self, client):
        stdin, stdout, stderr = client.exec_command('systemctl start minecraft')
        #stdin, stdout, stderr = client.exec_command('systemctl start ngrok')
    def __stopServer(self, client):
        stdin, stdout, stderr = client.exec_command('systemctl stop minecraft')
        #stdin, stdout, stderr = client.exec_command('systemctl stop ngrok')
    def __restartServer(self, client):
        stdin, stdout, stderr = client.exec_command('systemctl restart minecraft')
        #stdin, stdout, stderr = client.exec_command('systemctl restart ngrok')
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
        self.status = QStatusBar();
        self.status.addPermanentWidget(QLabel("Server Status: N/A"))
        self.status.showMessage("Be sure you're under the same network as your server or connected via VPN!")
        self.setStatusBar(self.status)

    def _createSecondScreen(self):
        vLayout = QVBoxLayout(self.centralWidget()); vLayout.setAlignment(Qt.AlignTop)
        vLayout.addWidget(QLabel())
        hLayout = QHBoxLayout(); hLayout.setSpacing(0)
        hLayout.setAlignment(Qt.AlignHCenter)
        formLayout = QFormLayout(self.centralWidget()); formLayout.setFormAlignment(Qt.AlignHCenter)
        formLayout.setLabelAlignment(Qt.AlignRight)

        btnGroup = QButtonGroup(); btnGroup.setExclusive(True)
        title = QLabel()
        tPng = QPixmap("./graphics/ManageCraft.png"); title.setPixmap(tPng)
        btn1 = QPushButton(); btn1.setFixedSize(130, 40)
        btn1.setCheckable(True); btn1.setChecked(False)
        rcPng = QIcon("./graphics/RemoteBtn.png")
        btn1.setIcon(rcPng); btn1.setIconSize(QSize(170, 40))
        btn2 = QPushButton(); btn2.setFixedSize(130, 40);
        btn2.setCheckable(True); btn2.setChecked(True)
        lcPng = QIcon("./graphics/LocalBtnChecked.png")
        btn2.setIcon(lcPng); btn2.setIconSize(QSize(170, 40))
        btn3 = QPushButton(); btn3.setFixedSize(130, 40)
        bPng = QIcon("./graphics/BrowseBtn.png")
        btn3.setIcon(bPng); btn3.setIconSize(QSize(200, 40))
        btn1.toggled.connect(self.remote); btnGroup.addButton(btn1)
        btn2.toggled.connect(self.local); btnGroup.addButton(btn2)
        btn3.clicked.connect(self.browseL)
        btn1.pressed.connect(partial(self.btnPressToggle, btn1, "RemoteBtnChecked.png"))
        btn1.released.connect(partial(self.btnPressToggle, btn1, "RemoteBtn.png"))
        btn3.pressed.connect(partial(self.btnPressToggle, btn3, "BrowseBtnChecked.png"))
        btn3.released.connect(partial(self.btnPressToggle, btn3, "BrowseBtn.png"))

        vLayout.addWidget(title, alignment=Qt.AlignCenter)
        hLayout.addWidget(btn1, alignment=Qt.AlignHCenter); hLayout.addWidget(btn2, alignment=Qt.AlignHCenter)
        vLayout.addLayout(hLayout)
        vLayout.addWidget(self.path, alignment=Qt.AlignHCenter)
        vLayout.addWidget(btn3, alignment=Qt.AlignCenter)

        self.frameL.setLayout(vLayout)
        self.mainMenu = False
        self.frameL.hide()
    def _createFirstScreen(self):
        vLayout = QVBoxLayout(self.centralWidget()); vLayout.setAlignment(Qt.AlignTop)
        vLayout.addWidget(QLabel())
        hLayout = QHBoxLayout(); hLayout.setSpacing(0)
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
        btn3.clicked.connect(partial(self.browseR))
        btn2.pressed.connect(partial(self.btnPressToggle, btn2, "LocalBtnChecked.png"))
        btn2.released.connect(partial(self.btnPressToggle, btn2, "LocalBtn.png"))
        btn3.pressed.connect(partial(self.btnPressToggle, btn3, "ConnectBtnChecked.png"))
        btn3.released.connect(partial(self.btnPressToggle, btn3, "ConnectBtn.png"))

        host = QLabel(); hPng = QPixmap("./graphics/Host.png"); host.setPixmap(hPng)
        user = QLabel(); uPng = QPixmap("./graphics/Username.png"); user.setPixmap(uPng)
        pas = QLabel(); pPng = QPixmap("./graphics/Password.png"); pas.setPixmap(pPng)

        formLayout.addRow(host, self.host)
        formLayout.addRow(user, self.user)
        formLayout.addRow(pas, self.pas)
        vLayout.addWidget(title, alignment=Qt.AlignCenter)
        hLayout.addWidget(btn1, alignment=Qt.AlignHCenter); hLayout.addWidget(btn2, alignment=Qt.AlignHCenter)
        vLayout.addLayout(hLayout)
        vLayout.addLayout(formLayout)
        vLayout.addWidget(btn3, alignment=Qt.AlignCenter)
        vLayout.addWidget(self.err, alignment=Qt.AlignHCenter)

        self.frameR.setLayout(vLayout)
        self.mainMenu = False
        self._createSecondScreen()

    def remote(self):
        if self.frameR.isVisible():
            pass
        else:
            self.styleFrame.setStyleSheet("border-image: url(./graphics/WindowFrame.png);\
background-image: url(./graphics/Frame_R.png); background-repeat: no-repeat;")
            self.frameL.hide()
            self.frameR.show()
    def connect(self, path): # Pack to config window
        self._createToolBar()
        self.frameR.hide()
        self.ui.label.setText("Changed!")
        self.frameC.show()
    def local(self):
        if self.frameL.isVisible():
            pass
        else:
            self.styleFrame.setStyleSheet("border-image: url(./graphics/WindowFrame.png);\
background-image: url(./graphics/Frame_L.png); background-repeat: no-repeat;")
            self.frameR.hide()
            self.frameL.show()
    def browseL(self):
        getPath = QFileDialog().getExistingDirectory()
        self.path.setText(getPath)
        if self.path.text() != '':
            self.setWindowTitle(f"{self.path.text()} - ManageCraft")
            self._createToolBar()
            self.frameL.hide()
            self.frameC.show()
    def browseR(self):
        if self.host.text() == '' or self.user.text() == '' or self.pas.text() == '':
            self.err.show()
        else:
            try:
                self.err.hide()
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(self.host.text(), port=22, username=self.user.text(), password=self.pas.text())
                self.client = client
                #self.dui.btnBox.accepted.connect(partial(self.connect, self.path.text()))
                self.plant_tree(self.client)
                self.dialog.show()
                self.path.setText(self.dui.path.text())
                if self.path.text() != '':
                    self.setWindowTitle(f"{self.path.text()} - ManageCraft")
                    self._createToolBar()
                    self.frameR.hide()
                    self.frameC.show()
                #Don't proceed until connected
            except socket.gaierror:
                self.err.show()
            #Don't proceed unless path given
##            if self.path.text() != '':
##                self.setWindowTitle(f"{self.path.text()} - ManageCraft")
##                self.connect(self.host.text(), self.path.text(), self.user.text(), self.pas.text())
    def plant_tree(self, client):
        folderIcon = QIcon("./graphics/folder.jpeg")
        self.dui.treeW.setColumnCount(1); self.dui.treeW.setAlternatingRowColors(True)
        stdin, stdout, stderr = client.exec_command('ls -d */')
        top = [i.strip('/\n') for i in stdout if True]
        print(top)
    def btnPressToggle(self, b, png):
        Png = QIcon(f"./graphics/{png}"); b.setIcon(Png)
        b.setIconSize(QSize(200, 40))

if __name__ == "__main__":
    app = QApplication([])
    gui = Window()
    gui.show()
    sys.exit(app.exec())
