# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaedicao.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Edicao_Foto_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(645, 649)
        self.slider = QtWidgets.QSlider(Form)
        self.slider.setEnabled(False)
        self.slider.setVisible(False)
        self.slider.setGeometry(QtCore.QRect(150, 570, 311, 21))
        self.slider.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.slider.setMaximum(255)
        self.slider.setProperty("value", 129)
        self.slider.setSliderPosition(129)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.publicar = QtWidgets.QPushButton(Form)
        self.publicar.setGeometry(QtCore.QRect(550, 10, 86, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.publicar.setFont(font)
        self.publicar.setObjectName("publicar")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(-10, 370, 661, 161))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 80))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(-481, 0, 1140, 142))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.funcao7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.funcao7.sizePolicy().hasHeightForWidth())
        self.funcao7.setSizePolicy(sizePolicy)
        self.funcao7.setMinimumSize(QtCore.QSize(135, 30))
        self.funcao7.setObjectName("funcao7")
        self.gridLayout.addWidget(self.funcao7, 0, 7, 1, 1)
        self.imagemFuncao2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagemFuncao2.sizePolicy().hasHeightForWidth())
        self.imagemFuncao2.setSizePolicy(sizePolicy)
        self.imagemFuncao2.setMinimumSize(QtCore.QSize(135, 85))
        self.imagemFuncao2.setText("")
        self.imagemFuncao2.setScaledContents(True)
        self.imagemFuncao2.setObjectName("imagemFuncao2")
        self.gridLayout.addWidget(self.imagemFuncao2, 1, 2, 1, 1)
        self.imagemFuncao3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imagemFuncao3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagemFuncao3.sizePolicy().hasHeightForWidth())
        self.imagemFuncao3.setSizePolicy(sizePolicy)
        self.imagemFuncao3.setMinimumSize(QtCore.QSize(135, 85))
        self.imagemFuncao3.setText("")
        self.imagemFuncao3.setScaledContents(True)
        self.imagemFuncao3.setObjectName("imagemFuncao3")
        self.gridLayout.addWidget(self.imagemFuncao3, 1, 3, 1, 1)
        self.funcao1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.funcao1.sizePolicy().hasHeightForWidth())
        self.funcao1.setSizePolicy(sizePolicy)
        self.funcao1.setMinimumSize(QtCore.QSize(135, 30))
        self.funcao1.setObjectName("funcao1")
        self.gridLayout.addWidget(self.funcao1, 0, 1, 1, 1)
        self.imagemFuncao4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagemFuncao4.sizePolicy().hasHeightForWidth())
        self.imagemFuncao4.setSizePolicy(sizePolicy)
        self.imagemFuncao4.setMinimumSize(QtCore.QSize(135, 85))
        self.imagemFuncao4.setText("")
        self.imagemFuncao4.setScaledContents(True)
        self.imagemFuncao4.setObjectName("imagemFuncao4")
        self.gridLayout.addWidget(self.imagemFuncao4, 1, 4, 1, 1)
        self.funcao6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.funcao6.sizePolicy().hasHeightForWidth())
        self.funcao6.setSizePolicy(sizePolicy)
        self.funcao6.setMinimumSize(QtCore.QSize(135, 30))
        self.funcao6.setObjectName("funcao6")
        self.gridLayout.addWidget(self.funcao6, 0, 6, 1, 1)
        self.funcao2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.funcao2.sizePolicy().hasHeightForWidth())
        self.funcao2.setSizePolicy(sizePolicy)
        self.funcao2.setMinimumSize(QtCore.QSize(135, 30))
        self.funcao2.setObjectName("funcao2")
        self.gridLayout.addWidget(self.funcao2, 0, 2, 1, 1)
        self.funcao4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.funcao4.sizePolicy().hasHeightForWidth())
        self.funcao4.setSizePolicy(sizePolicy)
        self.funcao4.setMinimumSize(QtCore.QSize(135, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.funcao4.setFont(font)
        self.funcao4.setObjectName("funcao4")
        self.gridLayout.addWidget(self.funcao4, 0, 4, 1, 1)
        self.funcao5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.funcao5.sizePolicy().hasHeightForWidth())
        self.funcao5.setSizePolicy(sizePolicy)
        self.funcao5.setMinimumSize(QtCore.QSize(135, 30))
        self.funcao5.setObjectName("funcao5")
        self.gridLayout.addWidget(self.funcao5, 0, 5, 1, 1)
        self.imagemFuncao5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagemFuncao5.sizePolicy().hasHeightForWidth())
        self.imagemFuncao5.setSizePolicy(sizePolicy)
        self.imagemFuncao5.setMinimumSize(QtCore.QSize(135, 85))
        self.imagemFuncao5.setText("")
        self.imagemFuncao5.setScaledContents(True)
        self.imagemFuncao5.setObjectName("imagemFuncao5")
        self.gridLayout.addWidget(self.imagemFuncao5, 1, 5, 1, 1)
        self.imagemFuncao1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagemFuncao1.sizePolicy().hasHeightForWidth())
        self.imagemFuncao1.setSizePolicy(sizePolicy)
        self.imagemFuncao1.setMinimumSize(QtCore.QSize(135, 85))
        self.imagemFuncao1.setText("")
        self.imagemFuncao1.setScaledContents(True)
        self.imagemFuncao1.setObjectName("imagemFuncao1")
        self.gridLayout.addWidget(self.imagemFuncao1, 1, 1, 1, 1)
        self.imagemFuncao6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagemFuncao6.sizePolicy().hasHeightForWidth())
        self.imagemFuncao6.setSizePolicy(sizePolicy)
        self.imagemFuncao6.setMinimumSize(QtCore.QSize(135, 85))
        self.imagemFuncao6.setText("")
        self.imagemFuncao6.setScaledContents(True)
        self.imagemFuncao6.setObjectName("imagemFuncao6")
        self.gridLayout.addWidget(self.imagemFuncao6, 1, 6, 1, 1)
        self.funcao3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.funcao3.sizePolicy().hasHeightForWidth())
        self.funcao3.setSizePolicy(sizePolicy)
        self.funcao3.setMinimumSize(QtCore.QSize(135, 30))
        self.funcao3.setObjectName("funcao3")
        self.gridLayout.addWidget(self.funcao3, 0, 3, 1, 1)
        self.imagemFuncao7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagemFuncao7.sizePolicy().hasHeightForWidth())
        self.imagemFuncao7.setSizePolicy(sizePolicy)
        self.imagemFuncao7.setMinimumSize(QtCore.QSize(135, 85))
        self.imagemFuncao7.setText("")
        self.imagemFuncao7.setScaledContents(True)
        self.imagemFuncao7.setObjectName("imagemFuncao7")
        self.gridLayout.addWidget(self.imagemFuncao7, 1, 7, 1, 1)
        self.funcao8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.funcao8.sizePolicy().hasHeightForWidth())
        self.funcao8.setSizePolicy(sizePolicy)
        self.funcao8.setMinimumSize(QtCore.QSize(135, 30))
        self.funcao8.setObjectName("funcao8")
        self.gridLayout.addWidget(self.funcao8, 0, 8, 1, 1)
        self.imagemFuncao8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagemFuncao8.sizePolicy().hasHeightForWidth())
        self.imagemFuncao8.setSizePolicy(sizePolicy)
        self.imagemFuncao8.setMinimumSize(QtCore.QSize(135, 85))
        self.imagemFuncao8.setText("")
        self.imagemFuncao8.setScaledContents(True)
        self.imagemFuncao8.setObjectName("imagemFuncao8")
        self.gridLayout.addWidget(self.imagemFuncao8, 1, 8, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.imagemCentral = QtWidgets.QLabel(Form)
        self.imagemCentral.setGeometry(QtCore.QRect(0, 50, 651, 321))
        self.imagemCentral.setText("")
        self.imagemCentral.setScaledContents(True)
        self.imagemCentral.setObjectName("imagemCentral")
        self.botaoFiltro = QtWidgets.QPushButton(Form)
        self.botaoFiltro.setGeometry(QtCore.QRect(50, 600, 91, 41))
        self.botaoFiltro.setMinimumSize(QtCore.QSize(91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        self.botaoFiltro.setFont(font)
        self.botaoFiltro.setMouseTracking(False)
        self.botaoFiltro.setObjectName("botaoFiltro")
        self.botaoEditar = QtWidgets.QPushButton(Form)
        self.botaoEditar.setGeometry(QtCore.QRect(480, 600, 91, 41))
        self.botaoEditar.setMinimumSize(QtCore.QSize(91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.botaoEditar.setFont(font)
        self.botaoEditar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.botaoEditar.setObjectName("botaoEditar")
        self.voltar = QtWidgets.QPushButton(Form)
        self.voltar.setGeometry(QtCore.QRect(10, 10, 86, 37))
        self.voltar.setMinimumSize(QtCore.QSize(86, 37))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.voltar.setFont(font)
        self.voltar.setObjectName("voltar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cam view"))
        self.publicar.setText(_translate("Form", "Publicar"))
        self.botaoFiltro.setText(_translate("Form", "Filtro"))
        self.botaoEditar.setText(_translate("Form", "Editar"))
        self.voltar.setText(_translate("Form", "Voltar"))

        
        self.funcao1.setText(_translate("Form", "Normal"))
        self.funcao2.setText(_translate("Form", "Cinza"))
        self.funcao3.setText(_translate("Form", "Filtro 3"))
        self.funcao4.setText(_translate("Form", "Filtro 4"))
        self.funcao5.setText(_translate("Form", "Filtro 5"))
        self.funcao6.setText(_translate("Form", "Filtro 6"))
        self.funcao7.setText(_translate("Form", "Filtro 7"))
        self.funcao8.setText(_translate("Form", "Filtro 8"))
        