# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BLBrowser.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(540, 480)
        Dialog.setSizeGripEnabled(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeW = QtWidgets.QTreeWidget(Dialog)
        self.treeW.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.treeW.setObjectName("treeW")
        self.verticalLayout.addWidget(self.treeW)
        self.path = QtWidgets.QLineEdit(Dialog)
        self.path.setObjectName("path")
        self.verticalLayout.addWidget(self.path)
        self.btnBox = QtWidgets.QDialogButtonBox(Dialog)
        self.btnBox.setMinimumSize(QtCore.QSize(161, 32))
        self.btnBox.setOrientation(QtCore.Qt.Horizontal)
        self.btnBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Open)
        self.btnBox.setCenterButtons(False)
        self.btnBox.setObjectName("btnBox")
        self.verticalLayout.addWidget(self.btnBox)

        self.retranslateUi(Dialog)
        self.btnBox.accepted.connect(Dialog.accept)
        self.btnBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Open"))
        self.treeW.headerItem().setText(0, _translate("Dialog", "Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
