# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arquivos_ui/inicial.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Inicial_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(646, 467)
        self.buttom = QtWidgets.QPushButton(Form)
        self.buttom.setGeometry(QtCore.QRect(180, 420, 281, 37))
        self.buttom.setObjectName("buttom")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 621, 401))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 619, 399))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 601, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.image = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.image.setObjectName("image")
        self.verticalLayout_2.addWidget(self.image)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cam view"))
        self.buttom.setText(_translate("Form", "TIRAR FOTO"))
        self.image.setText(_translate("Form", "TextLabel"))
