from PyQt5 import QtGui

from forms.EdicaoFotoForm import Ui_Edicao_Foto_Form
from PyQt5 import QtCore, QtWidgets

from funcoesModificao.cinzaImage import toGray
from funcoesModificao.filtroRealce import realce
from funcoesModificao.segmentacao import segmentar
from funcoesModificao.smoothing import smooth
from funcoesModificao.normal_Image import toNormal


IMAGE_NAME = "./images/edited.jpg"
IMAGE_TAKED = "./images/fotoTirada.jpg"



class TelaEdicao(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()
    toUsandoFiltro = True

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

        self.ui.imgaemSegmentada.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))

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

        self.ui.botaoFiltro.clicked.connect(self.UsandoFiltro)
        self.ui.botaoEditar.clicked.connect(self.UsandoEdicao)



    def switch(self):
        self.switch_window.emit()

    #------------ Funções para mudar o nome de cada botao dentro do Scroll Area de acordo com sua função ( usar filtro (Botao Filter),  ou editar (Botao editar) )
     
   
    # ----------- Funções que são chamadas quando um botao especifico é clickado --------     


    def UsandoFiltro(self):
        
        
        # ----------------------------------- Sentando a Fonte do botao filtro
        
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        self.ui.botaoFiltro.setFont(font)
        
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.ui.botaoEditar.setFont(font)

        # ------------------------------------ Mudando as fotos

        self.ui.imagemNormal.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))

        self.ui.imagemCinza.setPixmap(QtGui.QPixmap(toGray(IMAGE_TAKED)))

        self.ui.imagemBlur.setPixmap(QtGui.QPixmap(smooth(IMAGE_TAKED)))

        self.ui.imgaemSegmentada.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))

        self.ui.imagemContraste.setPixmap(QtGui.QPixmap(toGray(IMAGE_TAKED))) # funcao de realçar

        self.ui.filtro6_imagem.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED))) # Fazer filtro 6

        self.ui.filtro7_imagem.setPixmap(QtGui.QPixmap(toGray(IMAGE_TAKED)))    # Fazer filtro 7

        self.ui.filtro8_imagem.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))  # Fazer filtro 8


        # ------------------------------------ Tornando o Slider Invisivel e indisponivel

        self.ui.slider.setVisible(False)
        self.ui.slider.setEnabled(False)

        # -------------------------------------- Setando a variavel para mudar a funcao dos botoes para funções de filtro
        self.toUsandoFiltro = True

        # -------------------------------------- Mudando o nome dos botões ------------
        _translate = QtCore.QCoreApplication.translate        
        self.ui.normal.setText(_translate("Form", "Normal"))
        self.ui.segmentar.setText(_translate("Form", "Segmentar"))
        self.ui.cinzar.setText(_translate("Form", "Cinza"))
        self.ui.blur.setText(_translate("Form", "Blur"))
        self.ui.contraste.setText(_translate("Form", "Contraste"))
        self.ui.filtro6.setText(_translate("Form", "Filtro6"))
        self.ui.filtro7.setText(_translate("Form", "Filtro7"))
        self.ui.filtro8.setText(_translate("Form", "Filtro 8"))
        
    def UsandoEdicao(self):
        
        # ----------------------------------- Sentando a Fonte do botao editar
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.ui.botaoEditar.setFont(font)

        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.ui.botaoFiltro.setFont(font)

        #------------------------------------ Mudando as imagens

        self.ui.imagemNormal.setPixmap(QtGui.QPixmap("./images/EditedIcons/brilhoIcon.jpg"))

        self.ui.imagemCinza.setPixmap(QtGui.QPixmap("./images/EditedIcons/contrasteIcon.jpg"))

        self.ui.imagemBlur.setPixmap(QtGui.QPixmap("./images/EditedIcons/temperaturaIcon.jpg"))

        self.ui.imgaemSegmentada.setPixmap(QtGui.QPixmap("./images/EditedIcons/rotacaoIcon.jpg"))

        self.ui.imagemContraste.setPixmap(QtGui.QPixmap("./images/EditedIcons/sombraIcon.jpg")) # funcao de realçar

        self.ui.filtro6_imagem.setPixmap(QtGui.QPixmap("./images/EditedIcons/saturacaoIcon.jpg")) # Fazer filtro 6

        self.ui.filtro7_imagem.setPixmap(QtGui.QPixmap("./images/EditedIcons/realcaoIcon.jpg"))    # Fazer filtro 7

        self.ui.filtro8_imagem.setPixmap(QtGui.QPixmap("./images/EditedIcons/nitidezicon.jpg"))  # Fazer filtro 8

        # ------------------------------------ Tornando o Slider Visivel e disponivel

        self.ui.slider.setVisible(True)
        self.ui.slider.setEnabled(True)

        # -------------------------------------- Setando a variavel para mudar a funcao dos botoes para funções de edição 
        self.toUsandoFiltro = False
        
        # -------------------------------------- Mudando o nome dos botões ------------
        _translate = QtCore.QCoreApplication.translate        
        self.ui.normal.setText(_translate("Form", "Brilho"))
        self.ui.segmentar.setText(_translate("Form", "Rotação"))
        self.ui.cinzar.setText(_translate("Form", "Saturação"))
        self.ui.blur.setText(_translate("Form", "Temperatura"))
        self.ui.contraste.setText(_translate("Form", "Contraste"))
        self.ui.filtro6.setText(_translate("Form", "Sombras"))
        self.ui.filtro7.setText(_translate("Form", "Nitidez"))
        self.ui.filtro8.setText(_translate("Form", "Vinheta"))
        
    def telaTirarFoto(self):
        print("Voltando para a tela de tirar a foto")    

    def normal(self):

        print("toUsandoFiltro = " + "{}".format(self.toUsandoFiltro))

        if(self.toUsandoFiltro):
            self.ui.image_label.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))
        else:
            print("Usando edição Brilho")

    def realcar(self):
        if(self.toUsandoFiltro):
            self.ui.image_label.setPixmap(QtGui.QPixmap(toGray(IMAGE_TAKED)))
        else:
            print("Usando edição Contraste")

    def segmentarImage(self):
        
        if(self.toUsandoFiltro):
            self.ui.image_label.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))
        else:
            print("Usando edição Rotação")        

    def smooth(self):

        if(self.toUsandoFiltro):
            self.ui.image_label.setPixmap(QtGui.QPixmap(smooth(IMAGE_TAKED)))
        else:
            print("Usando edição Temperatura")  
        

    def cinza(self):
        
        if(self.toUsandoFiltro):
            self.ui.image_label.setPixmap(QtGui.QPixmap(toGray(IMAGE_TAKED)))
        else:
            print("Usando edição Saturação")  

    def filtro6(self):                                                         # Mudar o filtro [ toGray() ] usado para o filtro 6 feito 
        
        if(self.toUsandoFiltro):
            self.ui.image_label.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))
        else:
            print("Usando edição Sombra")  

    def filtro7(self):                                                         # Mudar o filtro [ toNormal() ] usado para o filtro 7 feito 
        
        if(self.toUsandoFiltro):
            self.ui.image_label.setPixmap(QtGui.QPixmap(toGray(IMAGE_TAKED)))
        else:
            print("Usando edição Nitidez")
        
    def filtro8(self):                                                          # Mudar o filtro [ toGray() ] usado para o filtro 8 feito
        
        if(self.toUsandoFiltro):
            self.ui.image_label.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))
        else:
            print("Usando edição Vinheta")

   
    