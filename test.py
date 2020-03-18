import paramiko
import re, os, sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog
from PyQt5.QtWidgets import QStatusBar, QToolBar
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout
from PyQt5.QtCore import Qt
from functools import partial

app = QApplication([])

gui = QWidget()
gui.setWindowTitle("ManagerCraft (Test Environment)")
gui.setGeometry(100, 100, 1024, 540)

'''layout = QFormLayout()
grab = QLineEdit()
pas = QLineEdit()
pas.setEchoMode(QLineEdit.Password)
grab.setFixedSize(50, 20)
pas.setFixedSize(50, 20)
layout.addRow("Username:", grab)
layout.addRow("Password:", pas)
btn = QPushButton("PUUUSH")
btn.clicked.connect(lambda: print(grab.text()))

layout.addWidget(btn)
gui.setLayout(layout)'''


textBox = QLineEdit(gui).resize(500, 20)
text = QLabel("Submit!", parent=gui).resize(100, 200)

gui.show()
sys.exit(app.exec())
