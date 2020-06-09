# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaedicao.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Edicao_Foto_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(645, 459)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 390, 86, 37))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 390, 86, 37))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 390, 86, 37))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 390, 86, 37))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(430, 400, 160, 16))
        self.horizontalSlider.setSliderPosition(50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setGeometry(QtCore.QRect(10, 10, 621, 371))
        self.image_label.setObjectName("image_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cam view"))
        self.pushButton.setText(_translate("Form", "Cinza"))
        self.pushButton_2.setText(_translate("Form", "Contraste"))
        self.pushButton_3.setText(_translate("Form", "Segmentar"))
        self.pushButton_4.setText(_translate("Form", "PushButton"))
        self.image_label.setText(_translate("Form", "TextLabel"))
