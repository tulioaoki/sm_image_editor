# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arquivos_ui/telaedicao.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Edicao_Foto_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(645, 472)
        self.cinzar = QtWidgets.QPushButton(Form)
        self.cinzar.setGeometry(QtCore.QRect(10, 390, 86, 37))
        self.cinzar.setObjectName("cinzar")
        self.contraste = QtWidgets.QPushButton(Form)
        self.contraste.setGeometry(QtCore.QRect(100, 390, 86, 37))
        self.contraste.setObjectName("contraste")
        self.segmentar = QtWidgets.QPushButton(Form)
        self.segmentar.setGeometry(QtCore.QRect(10, 430, 86, 37))
        self.segmentar.setObjectName("segmentar")
        self.blur = QtWidgets.QPushButton(Form)
        self.blur.setGeometry(QtCore.QRect(100, 430, 86, 37))
        self.blur.setObjectName("blur")
        self.slider_brilho = QtWidgets.QSlider(Form)
        self.slider_brilho.setGeometry(QtCore.QRect(210, 410, 160, 16))
        self.slider_brilho.setSliderPosition(50)
        self.slider_brilho.setOrientation(QtCore.Qt.Horizontal)
        self.slider_brilho.setObjectName("slider_brilho")
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setGeometry(QtCore.QRect(10, 10, 621, 371))
        self.image_label.setObjectName("image_label")
        self.publicar = QtWidgets.QPushButton(Form)
        self.publicar.setGeometry(QtCore.QRect(550, 430, 86, 37))
        self.publicar.setObjectName("publicar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cam view"))
        self.cinzar.setText(_translate("Form", "Cinza"))
        self.contraste.setText(_translate("Form", "Contraste"))
        self.segmentar.setText(_translate("Form", "Segmentar"))
        self.blur.setText(_translate("Form", "Blur"))
        self.image_label.setText(_translate("Form", "TextLabel"))
        self.publicar.setText(_translate("Form", "Publicar"))
