# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class UI(object):
    def setupUi(self, FrameC):
        FrameC.setObjectName("FrameC")
        FrameC.resize(640, 480)
        self.w1 = QtWidgets.QWidget(FrameC)
        self.w1.setGeometry(QtCore.QRect(9, 9, 308, 462))
        self.w1.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.w1.setObjectName("w1")
        self.formLayoutWidget = QtWidgets.QWidget(self.w1)
        self.formLayoutWidget.setGeometry(QtCore.QRect(19, 19, 271, 421))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.form = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.form.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.form.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.form.setContentsMargins(0, 0, 0, 0)
        self.form.setObjectName("form")
        self.abcLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.abcLabel.setObjectName("abcLabel")
        self.form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.abcLabel)
        self.abcSpinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.abcSpinBox.setObjectName("abcSpinBox")
        self.form.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.abcSpinBox)
        self.defLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.defLabel.setObjectName("defLabel")
        self.form.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.defLabel)
        self.defLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.defLineEdit.setObjectName("defLineEdit")
        self.form.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.defLineEdit)
        self.ghiLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.ghiLabel.setObjectName("ghiLabel")
        self.form.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ghiLabel)
        self.ghiComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.ghiComboBox.setObjectName("ghiComboBox")
        self.form.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ghiComboBox)
        self.jklLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.jklLabel.setObjectName("jklLabel")
        self.form.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.jklLabel)
        self.jklCheckBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.jklCheckBox.setObjectName("jklCheckBox")
        self.form.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.jklCheckBox)
        self.mnoLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.mnoLabel.setObjectName("mnoLabel")
        self.form.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.mnoLabel)
        self.mnoDial = QtWidgets.QDial(self.formLayoutWidget)
        self.mnoDial.setObjectName("mnoDial")
        self.form.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.mnoDial)
        self.w2 = QtWidgets.QWidget(FrameC)
        self.w2.setGeometry(QtCore.QRect(323, 9, 308, 462))
        self.w2.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.w2.setObjectName("w2")
        self.label = QtWidgets.QLabel(self.w2)
        self.label.setGeometry(QtCore.QRect(10, 10, 291, 441))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(FrameC)
        QtCore.QMetaObject.connectSlotsByName(FrameC)

    def retranslateUi(self, FrameC):
        _translate = QtCore.QCoreApplication.translate
        FrameC.setWindowTitle(_translate("FrameC", "Form"))
        self.abcLabel.setText(_translate("FrameC", "abc"))
        self.defLabel.setText(_translate("FrameC", "def"))
        self.ghiLabel.setText(_translate("FrameC", "ghi"))
        self.jklLabel.setText(_translate("FrameC", "jkl"))
        self.mnoLabel.setText(_translate("FrameC", "mno"))
        self.label.setText(_translate("FrameC", "VIEW MODS DIRECTORY HERE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrameC = QtWidgets.QWidget()
    ui = UI()
    ui.setupUi(FrameC)
    FrameC.show()
    sys.exit(app.exec_())
