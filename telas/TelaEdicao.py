from PyQt5 import QtGui

from forms.EdicaoFotoForm import Ui_Edicao_Foto_Form
from PyQt5 import QtCore, QtWidgets

from funcoesModificao.cinzaImage import toGray
from funcoesModificao.filtroRealce import realce
from funcoesModificao.segmentacao import segmentar
from funcoesModificao.smoothing import smooth
from funcoesModificao.normal_Image import toNormal

IMAGE_NAME = "edited.jpg"
IMAGE_TAKED = "fotoTirada.jpg"

toUsandoFiltro = True

class TelaEdicao(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Edicao_Foto_Form()
        self.ui.setupUi(self)
        self.ui.image_label.setPixmap(QtGui.QPixmap(IMAGE_NAME))
        self.image = None

        #----- Setar a imagens dos Filtros ---------------------------------------

        self.ui.imagemNormal.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))

        self.ui.imagemCinza.setPixmap(QtGui.QPixmap(toGray(IMAGE_TAKED)))

        self.ui.imagemBlur.setPixmap(QtGui.QPixmap(smooth(IMAGE_TAKED)))

        self.ui.imgaemSegmentada.setPixmap(QtGui.QPixmap(segmentar(IMAGE_TAKED)))

        self.ui.imagemContraste.setPixmap(QtGui.QPixmap(toGray(IMAGE_TAKED))) # funcao de realçar

        self.ui.filtro6_imagem.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED))) # Fazer filtro 6

        self.ui.filtro7_imagem.setPixmap(QtGui.QPixmap(toGray(IMAGE_TAKED)))    # Fazer filtro 7

        self.ui.filtro8_imagem.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))  # Fazer filtro 8

        
        #----- Pages Buttons Actons on Clicked -------------------------------------

        self.ui.publicar.clicked.connect(self.switch_window)
        self.ui.tirarFoto.clicked.connect(self.telaTirarFoto)
        
        # ----Filters Buttons Actions on Clicked -----------------------
        
        self.ui.contraste.clicked.connect(self.cinza)
        self.ui.segmentar.clicked.connect(self.segmentarImage)
        self.ui.blur.clicked.connect(self.smooth)
        self.ui.cinzar.clicked.connect(self.cinza)
        self.ui.normal.clicked.connect(self.normal)
        self.ui.filtro6.clicked.connect(self.filtro6)
        self.ui.filtro7.clicked.connect(self.filtro7)
        self.ui.filtro8.clicked.connect(self.filtro8)

        # --- Buttons ( Filtros & Editar) Actions on Clicked -------------

        self.ui.botaoFiltro.clicked.connect(self.filtro8)
        self.ui.botaoEditar.clicked.connect(self.filtro8)


    def switch(self):
        self.switch_window.emit()

    #------------ Funções para mudar o nome de cada botao dentro do Scroll Area de acordo com sua função ( usar filtro (Botao Filter),  ou editar (Botao editar) )
     
   
    # ----------- Funções que são chamadas quando um botao especifico é clickado --------     

   
    def telaTirarFoto(self):
        print("Voltando para a tela de tirar a foto")    

    def normal(self):
         self.ui.imagemNormal.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))

    def realcar(self):
        self.ui.image_label.setPixmap(QtGui.QPixmap(realce(IMAGE_TAKED)))

    def segmentarImage(self):
        self.ui.image_label.setPixmap(QtGui.QPixmap(segmentar(IMAGE_TAKED)))

    def smooth(self):
        self.ui.image_label.setPixmap(QtGui.QPixmap(smooth(IMAGE_TAKED)))

    def cinza(self):
        self.ui.image_label.setPixmap(QtGui.QPixmap(toGray(IMAGE_TAKED)))

    def filtro6(self):                                                         # Mudar o filtro [ toGray() ] usado para o filtro 6 feito 
        self.ui.filtro6_imagem.setPixmap(QtGui.QPixmap(toGray(IMAGE_TAKED)))    

    def filtro7(self):                                                         # Mudar o filtro [ toNormal() ] usado para o filtro 7 feito 
        self.ui.filtro7_imagem.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))

    def filtro8(self):                                                          # Mudar o filtro [ toGray() ] usado para o filtro 8 feito
         self.ui.filtro8_imagem.setPixmap(QtGui.QPixmap(toGray(IMAGE_TAKED)))

   
