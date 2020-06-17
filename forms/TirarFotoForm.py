# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telatirarfoto.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(645, 649)
        self.control_bt = QtWidgets.QPushButton(Form)
        self.control_bt.setGeometry(QtCore.QRect(20, 580, 141, 41))
        self.control_bt.setObjectName("control_bt")
        self.editar = QtWidgets.QPushButton(Form)
        self.editar.setEnabled(False)
        self.editar.setGeometry(QtCore.QRect(470, 580, 141, 41))
        self.editar.setObjectName("editar")
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setGeometry(QtCore.QRect(0, 50, 651, 511))
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.voltar = QtWidgets.QPushButton(Form)
        self.voltar.setGeometry(QtCore.QRect(10, 10, 86, 37))
        self.voltar.setObjectName("voltar")
        self.desenhar = QtWidgets.QPushButton(Form)
        self.desenhar.setGeometry(QtCore.QRect(250, 580, 141, 41))
        self.desenhar.setObjectName("desenhar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cam view"))
        self.control_bt.setText(_translate("Form", "TIRAR FOTO"))
        self.editar.setText(_translate("Form", "EDITAR"))
        self.voltar.setText(_translate("Form", "Voltar"))
        self.desenhar.setText(_translate("Form", "DESENHAR: DESLIGADO"))
