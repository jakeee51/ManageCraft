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

import paramiko
import re, os, sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog
from PyQt5.QtWidgets import QStatusBar, QToolBar
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QFormLayout
from PyQt5.QtCore import Qt
from functools import partial

class Window(QMainWindow):
    '''This class instantiates the main gui window'''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ManagerCraft")
        self.setCentralWidget(QWidget())
        self.setGeometry(100, 100, 720, 540)
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()
        self.host = QLineEdit(); self.user = QLineEdit(); self.pas = QLineEdit()
        self._createLoginScreen()

        self.client = None


    def _createMenu(self):
        self.menu = self.menuBar().addMenu("File")
        self.menu.addAction("Browse", self.close)
        self.menu.addAction("Disconnect", self.close)
        self.menu.addAction("Exit", self.close)
    def _createToolBar(self): # Keep tool bar attached
        tools = QToolBar()
        tools.addAction("CONFIGURATION", self.close)
        tools.addAction("STATUS", self.close)
        self.addToolBar(tools)
    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("Server Status: Online / Offline")
        self.setStatusBar(status)
    def _createLoginScreen(self):
        vLayout = QVBoxLayout()
        formLayout = QFormLayout()
        btn1 = QPushButton("Connect to Remote Server")
        btn2 = QPushButton("Connect to Local Server")
        btn1.clicked.connect(partial(self.connect, "hVar", "uVar", "pVar"))
        btn2.clicked.connect(self.browse)
        formLayout.addRow("Host:", self.host) # NOTE TO SELF:
        formLayout.addRow("Username:", self.user) # LAYOUT CONTROLS
        formLayout.addRow("Password:", self.pas) # ITS SIZE
        vLayout.addWidget(QLabel())
        vLayout.addLayout(formLayout)
        vLayout.addWidget(btn1)
        vLayout.addWidget(QLabel())
        vLayout.addWidget(QLabel())
        vLayout.addWidget(btn2)
      
        self.centralWidget().setLayout(vLayout)

    def connect(self, host, user, pas): # Pack to config window
        pass
        '''client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, port=22, username=user, password=pas)
        self.client = client'''
    def browse(self): # Pack to browse window
        pass

if __name__ == "__main__":
    app = QApplication([])
    gui = Window()
    gui.show()
    sys.exit(app.exec())

'''import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

def greeting():
    """Slot function."""
    if msg.text():
        msg.setText("")
    else:
        msg.setText("Hello World!")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals and slots')
layout = QVBoxLayout()

btn = QPushButton('Greet')
btn.clicked.connect(greeting)  # Connect clicked to greeting()

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())'''
