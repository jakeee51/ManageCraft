import re, os, sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFrame, QDialog
from PyQt5.QtWidgets import QStatusBar, QToolBar, QButtonGroup, QFileDialog
from PyQt5.QtWidgets import QLabel, QPushButton, QRadioButton, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout
from PyQt5.QtWidgets import QTreeWidget, QDialog, QTreeWidgetItem
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt, QSize
from functools import partial

def backBTN(b, prev):
    prev.close()
    b.show()

def login(main, back, t1, t2):
    frame2 = QFrame(main)
    layout = QVBoxLayout(frame2)
    u = t1.text(); p = t2.text()
    a = "Login Successful!<br>Username: " + u + "<br>Password: " + p
    L1 = QLabel(f"<h1>{a}</h1>")
    btn = QPushButton("BACK", parent=frame2)
    layout.addWidget(L1)
    layout.addWidget(btn)
    btn.clicked.connect(partial(backBTN, back, frame2))
    frame2.show()
    back.close()

app = QApplication([])

gui = QDialog()
gui.setStyleSheet("background-image: url(Frame_1.png);\
                  background-repeat: no-repeat;")
gui.setWindowTitle("ManagerCraft (Test Environment)")
gui.setGeometry(100, 100, 1024, 540)

'''frame = QFrame(gui)
#frame.setAttribute(Qt.WA_DeleteOnClose)
layout = QFormLayout(frame)

grab = QLineEdit(); pas = QLineEdit(); pas.setEchoMode(QLineEdit.Password)
grab.setFixedSize(100, 20); pas.setFixedSize(100, 20)
layout.addRow("Username:", grab); layout.addRow("Password:", pas)
btn = QPushButton("LOGIN", parent=frame)
btn.setFixedSize(100, 20); btn.setDown(True)
btn.clicked.connect(partial(login, gui, frame, grab, pas))

layout.addWidget(btn)
frame.setLayout(layout)'''

tree = QTreeWidget(gui)
cities =  QTreeWidgetItem(tree)
cities.setText(0, "Cities")
osloItem =  QTreeWidgetItem(cities)
osloItem.setText(0, "Oslo")
osloItem.setText(1, "Yes")
planets =  QTreeWidgetItem(tree, cities)
planets.setText(0, "Planets")
e = QTreeWidgetItem(tree)
e.setText(0, "Earth")
planets.insertChild(0, e)

gui.show()
sys.exit(app.exec())
