from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(645, 459)
        self.control_bt = QtWidgets.QPushButton(Form)
        self.control_bt.setGeometry(QtCore.QRect(80, 400, 201, 41))
        self.control_bt.setObjectName("control_bt")
        self.editar = QtWidgets.QPushButton(Form)
        self.editar.setEnabled(True)
        self.editar.setGeometry(QtCore.QRect(390, 400, 211, 41))
        self.editar.setObjectName("editar")
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setGeometry(QtCore.QRect(10, 10, 621, 371))
        self.image_label.setObjectName("image_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cam view"))
        self.control_bt.setText(_translate("Form", "TIRAR FOTO"))
        self.editar.setText(_translate("Form", "EDITAR"))
        self.image_label.setText(_translate("Form", "TextLabel"))
