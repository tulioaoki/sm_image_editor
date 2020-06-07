# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inicial.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


IMAGE_NAME = "../images/edited.jpg"


class Ui_Inicial_Form (object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(645, 649)
        self.buttom = QtWidgets.QPushButton(Form)
        self.buttom.setEnabled(True)
        self.buttom.setGeometry(QtCore.QRect(180, 590, 281, 37))
        self.buttom.setObjectName("buttom")

        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(0, 40, 641, 541))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 622, 550))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout = QtWidgets.QVBoxLayout( self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        for i in range(4):  # For que irá percorrer a lista de fotos editadas

            if(i == 0):
                self.image = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                sizePolicy = QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(
                self.image.sizePolicy().hasHeightForWidth())

                self.image.setSizePolicy(sizePolicy)
                self.image.setMinimumSize(QtCore.QSize(604, 532))
                self.image.setText("")
                self.image.setPixmap(QtGui.QPixmap(IMAGE_NAME))
                self.image.setScaledContents(True)
                self.image.setObjectName("image")
                self.verticalLayout.addWidget(self.image)

            else:

                label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth( label.sizePolicy().hasHeightForWidth())
                label.setSizePolicy(sizePolicy)
                label.setMinimumSize(QtCore.QSize(604, 532))
                label.setPixmap(QtGui.QPixmap(IMAGE_NAME))
                label.setScaledContents(True)
                self.verticalLayout.addWidget(label)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.sair = QtWidgets.QPushButton(Form)
        self.sair.setGeometry(QtCore.QRect(520, 10, 95, 24))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.sair.setFont(font)
        self.sair.setObjectName("sair")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cam view"))
        self.buttom.setText(_translate("Form", "TIRAR FOTO"))
        self.sair.setText(_translate("Form", "Sair"))
