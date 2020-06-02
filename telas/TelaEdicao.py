from PyQt5 import QtGui

from forms.EdicaoFotoForm import Ui_Edicao_Foto_Form
from PyQt5 import QtCore, QtWidgets

from funcoesModificao.cinzaImage import toGray
from funcoesModificao.filtroRealce import realce
from funcoesModificao.segmentacao import segmentar
from funcoesModificao.smoothing import smooth

IMAGE_NAME = "edited.jpg"


class TelaEdicao(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Edicao_Foto_Form()
        self.ui.setupUi(self)
        self.ui.image_label.setPixmap(QtGui.QPixmap(IMAGE_NAME))
        self.image = None
        self.ui.publicar.clicked.connect(self.switch_window)
        self.ui.contraste.clicked.connect(self.realcar)
        self.ui.segmentar.clicked.connect(self.segmentarImage)
        self.ui.blur.clicked.connect(self.smooth)
        self.ui.cinzar.clicked.connect(self.cinza)

    def switch(self):
        self.switch_window.emit()

    def realcar(self):
        self.ui.image_label.setPixmap(QtGui.QPixmap(realce(IMAGE_NAME)))

    def segmentarImage(self):
        self.ui.image_label.setPixmap(QtGui.QPixmap(segmentar(IMAGE_NAME)))

    def smooth(self):
        self.ui.image_label.setPixmap(QtGui.QPixmap(smooth(IMAGE_NAME)))

    def cinza(self):
        self.ui.image_label.setPixmap(QtGui.QPixmap(toGray(IMAGE_NAME)))
