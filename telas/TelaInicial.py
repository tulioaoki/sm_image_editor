from PyQt5 import QtGui
from PyQt5 import QtCore, QtWidgets
from forms.InicialForm import Ui_Inicial_Form


class TelaInicial(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    sair = QtCore.pyqtSignal()

    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Inicial_Form()
        self.ui.setupUi(self)
        self.image = None
        self.ui.buttom.clicked.connect(self.switch)
        self.ui.sair.clicked.connect(self.exit)

    def switch(self):
        self.switch_window.emit()

    def exit(self):
        self.sair.emit()
