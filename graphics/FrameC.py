# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Frame_2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1026, 540)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, -10, 271, 71))
        self.label.setStyleSheet("image: url(:/Labels/ManageCraft.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 90, 371, 441))
        self.widget.setStyleSheet("border-image: url(:/Buttons/F2Box.png);")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(640, 90, 371, 441))
        self.widget_2.setStyleSheet("border-image: url(:/Buttons/F2Box.png);")
        self.widget_2.setObjectName("widget_2")
        self.restartBtn = QtWidgets.QPushButton(Form)
        self.restartBtn.setGeometry(QtCore.QRect(210, 60, 101, 31))
        self.restartBtn.setStyleSheet("border-image: url(:/Buttons/RSTButtonUnchecked.png);\n"
"")
        self.restartBtn.setText("")
        self.restartBtn.setObjectName("restartBtn")
        self.stopBtn = QtWidgets.QPushButton(Form)
        self.stopBtn.setGeometry(QtCore.QRect(110, 60, 101, 31))
        self.stopBtn.setStyleSheet("border-image: url(:/Buttons/Stop.png);")
        self.stopBtn.setText("")
        self.stopBtn.setObjectName("stopBtn")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 60, 101, 31))
        self.pushButton_3.setStyleSheet("border-image: url(:/Buttons/Start.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.widget.raise_()
        self.label.raise_()
        self.widget_2.raise_()
        self.restartBtn.raise_()
        self.stopBtn.raise_()
        self.pushButton_3.raise_()

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
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
