import re, os, sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFrame, QDialog
from PyQt5.QtWidgets import QStatusBar, QToolBar, QButtonGroup, QFileDialog
from PyQt5.QtWidgets import QLabel, QPushButton, QRadioButton, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout
from PyQt5.QtWidgets import QTreeWidget, QDialog, QTreeWidgetItem, QTreeWidgetItemIterator
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt, QSize, QTimer
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
gui.setWindowTitle("ManagerCraft (Test Environment)")
gui.setGeometry(100, 100, 540, 480)

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

folderIcon = QIcon("./graphics/folder.jpeg")
tree = QTreeWidget(gui)
tree.setColumnCount(1)
tree.setAlternatingRowColors(True)
tree.setHeaderLabel("Name")
top = ["usr", "bin", "root", "home", "etc"]
low1 = {"home": ["jake", "david"]}
low2 = {"jake": ["CaliBot", "MCServer", "ngrok"]}
folders = {"top": top, "low": low1}
def grow_tree(dct):
    items = []
    for i in top:
        item = QTreeWidgetItem([i])
        item.setIcon(0, folderIcon)
        if i in dct["low"]:
            childs = []
            for child in dct["low"][i]:
                j = QTreeWidgetItem([child])
                j.setIcon(0, folderIcon)
                childs.append(j)
            item.addChildren(childs)
        items.append(item)
    tree.addTopLevelItems(items)
    #print(tree.findItems("home", Qt.MatchExactly, 0)[0].text(0))

'''a = QTreeWidgetItem(["home"])
a.setIcon(0, folderIcon)
b = QTreeWidgetItem(["mike"])
b.setIcon(0, folderIcon)
a.addChild(b)
tree.insertTopLevelItem(0, a)
index = tree.indexFromItem(b, 0)'''
#print(tree.itemFromIndex(index).text(0))
##cities =  QTreeWidgetItem(tree)
##cities.setText(0, "Cities")
##osloItem =  QTreeWidgetItem(cities)
##osloItem.setText(0, "Oslo")
##planets =  QTreeWidgetItem(tree, cities)
##planets.setText(0, "Planets")
grow_tree(folders)
#flags = QTreeWidgetItemIterator.Selected
a = 0
def func():
    it = QTreeWidgetItemIterator(tree, flags=QTreeWidgetItemIterator.All)
    mx = tree.topLevelItemCount(); c = 0
    tempath = []
    while it.value():
        if mx > c:
            item = it.value()
            if item.isExpanded():
                tempath = [item.text(0)]
            MX = item.childCount(); C = 0
            nit = QTreeWidgetItemIterator(item, flags=QTreeWidgetItemIterator.All)
            while nit.value():
                if MX > C:
                    global a
                    a = nit.value().parent()
                    if nit.value().text(0) == "jake":
                        tempath.append("jake")
                        MX = 0; mx = 0; break
                    nit += 1; C += 1
                else:
                    break
            it += 1; c += 1
        else:
            break

tree.itemExpanded.connect(func)
gui.show()
sys.exit(app.exec())
