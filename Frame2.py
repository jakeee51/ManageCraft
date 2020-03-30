# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Frame2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class UI2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(924, 495)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 271, 51))
        self.label.setStyleSheet("image: url(:/Labels/ManageCraft.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.restartBtn = QtWidgets.QPushButton(Form)
        self.restartBtn.setGeometry(QtCore.QRect(810, 30, 101, 31))
        self.restartBtn.setStyleSheet("border-image: url(:/Buttons/RSTButtonUnchecked.png);\n"
"border-image: url(:/Buttons/Restart.png);\n"
"")
        self.restartBtn.setText("")
        self.restartBtn.setObjectName("restartBtn")
        self.stopBtn = QtWidgets.QPushButton(Form)
        self.stopBtn.setGeometry(QtCore.QRect(710, 30, 101, 31))
        self.stopBtn.setStyleSheet("border-image: url(:/Buttons/Stop.png);")
        self.stopBtn.setText("")
        self.stopBtn.setObjectName("stopBtn")
        self.startBtn = QtWidgets.QPushButton(Form)
        self.startBtn.setGeometry(QtCore.QRect(610, 30, 101, 31))
        self.startBtn.setStyleSheet("border-image: url(:/Buttons/Start.png);")
        self.startBtn.setText("")
        self.startBtn.setObjectName("startBtn")
        self.lefty = QtWidgets.QWidget(Form)
        self.lefty.setGeometry(QtCore.QRect(30, 90, 381, 381))
        self.lefty.setStyleSheet("border-image: url(:/Buttons/F2Box.png); background-repeat: no-repeat;")
        self.lefty.setObjectName("lefty")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.lefty)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.lefty)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 363, 363))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.righty = QtWidgets.QWidget(Form)
        self.righty.setGeometry(QtCore.QRect(530, 90, 381, 381))
        self.righty.setStyleSheet("border-image: url(:/Buttons/F2Box.png); background-repeat: no-repeat;")
        self.righty.setObjectName("righty")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
import Logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = UI2()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
