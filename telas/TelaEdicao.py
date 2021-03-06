import os, os.path
import cv2


from PyQt5 import QtGui

from forms.EdicaoFotoForm import Ui_Edicao_Foto_Form
from PyQt5 import QtCore, QtWidgets



from funcoesModificao.cinzaImage import toGray
from funcoesModificao.filtroRealce import realce
from funcoesModificao.segmentacao import segmentar
from funcoesModificao.smoothing import smooth
from funcoesModificao.normal_Image import toNormal
from funcoesModificao.smoothingCopy import smoothTeste
from funcoesModificao.brilho import brilho
from funcoesModificao.rotacao import rotacionar
from funcoesModificao.temperatura import converte_temp


IMAGE_FILTERED = "./images/PhotoInEdition/filtered.jpg"
IMAGE_TAKED = "./images/PhotoInEdition/fotoTirada.jpg"



class TelaEdicao(QtWidgets.QWidget):

    
    voltando = QtCore.pyqtSignal()

    inicialScreen = QtCore.pyqtSignal()

    toUsandoFiltro = True

    sliderValues = [0,128,128,128,128,128,128,128]

    queFuncaoEdicao = 0

    do_i_edited_an_image = os.path.exists("./images/PhotoInEdition/edited.jpg")

    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Edicao_Foto_Form()
        self.ui.setupUi(self)
        self.ui.image_label.setPixmap(QtGui.QPixmap(IMAGE_TAKED))
        self.image = None

        #----- Setar a imagens dos Filtros ---------------------------------------

  
        self.ui.imagemNormal.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))

        self.ui.imagemCinza.setPixmap(QtGui.QPixmap(toGray(IMAGE_TAKED)))

        self.ui.imagemBlur.setPixmap(QtGui.QPixmap(smooth(IMAGE_TAKED)))

        self.ui.imagemSegmentada.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))

        self.ui.imagemContraste.setPixmap(QtGui.QPixmap(toGray(IMAGE_TAKED))) # funcao de realçar

        self.ui.filtro6_imagem.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED))) # Fazer filtro 6

        self.ui.filtro7_imagem.setPixmap(QtGui.QPixmap(toGray(IMAGE_TAKED)))    # Fazer filtro 7

        self.ui.filtro8_imagem.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))  # Fazer filtro 8

                   
        
        #----- Pages Buttons Actons on Clicked -------------------------------------

        self.ui.publicar.clicked.connect(self.telaInicial)
        self.ui.tirarFoto.clicked.connect(self.voltar)
        
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

        self.ui.botaoFiltro.clicked.connect(self.usandoFiltro)
        self.ui.botaoEditar.clicked.connect(self.usandoEdicao)

        # ----- Funcao que pega o valor do slider

        self.ui.slider.valueChanged.connect(self.sliderChange)
        

    # Funções Para mudar de Tela

    def telaInicial(self):
        
        img_dir = "./images/PublishedPhoto/" # Enter Directory of all images         
        length = len([name for name in os.listdir(img_dir) ])
        img = None

        if(self.do_i_edited_an_image == True):
            img = cv2.imread("./images/PhotoInEdition/edited.jpg",0)
        else:
            img = cv2.imread("./images/PhotoInEdition/filtered.jpg",0)

        img_dir = "./images/PublishedPhoto/image"
        final = img_dir + "{}".format(length) + "{}".format(".jpg")
        
        cv2.imwrite(final, img)
        self.inicialScreen.emit()

    def voltar(self):
        
        self.voltando.emit()

    #------------ Funções para mudar o nome de cada botao dentro do Scroll Area de acordo com sua função ( usar filtro (Botao Filter),  ou editar (Botao editar) )
     
   
    # ----------- Funções que são chamadas quando um botao especifico é clickado --------     


    def usandoFiltro(self):
        
        
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

        # ------------------------------------ Mudando as imagens que ficam em baixo dos botoes

        if(self.do_i_edited_an_image == True):
                
            self.ui.image_label.setPixmap(QtGui.QPixmap(toNormal("./images/PhotoInEdition/edited.jpg")))
            self.ui.imagemCinza.setPixmap(QtGui.QPixmap("./images/PhotoInEdition/edited.jpg"))
            self.ui.imagemSegmentada.setPixmap(QtGui.QPixmap("./images/PhotoInEdition/edited.jpg"))
            self.ui.imagemBlur.setPixmap(QtGui.QPixmap("./images/PhotoInEdition/edited.jpg"))
            self.ui.imagemContraste.setPixmap(QtGui.QPixmap("./images/PhotoInEdition/edited.jpg"))
            self.ui.filtro6_imagem.setPixmap(QtGui.QPixmap(toNormal("./images/PhotoInEdition/edited.jpg"))) # Fazer filtro 6
            self.ui.filtro7_imagem.setPixmap(QtGui.QPixmap(toNormal("./images/PhotoInEdition/edited.jpg"))) # Fazer filtro 7
            self.ui.filtro8_imagem.setPixmap(QtGui.QPixmap(toNormal("./images/PhotoInEdition/edited.jpg"))) # Fazer filtro 8

        else:
            self.ui.image_label.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))
            self.ui.imagemCinza.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))
            self.ui.imagemSegmentada.setPixmap(QtGui.QPixmap(IMAGE_TAKED))
            self.ui.imagemBlur.setPixmap(QtGui.QPixmap(IMAGE_TAKED))
            self.ui.imagemContraste.setPixmap(QtGui.QPixmap(IMAGE_TAKED))
            self.ui.filtro6_imagem.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED))) # Fazer filtro 6
            self.ui.filtro7_imagem.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED))) # Fazer filtro 7
            self.ui.filtro8_imagem.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED))) # Fazer filtro 8
        
        
         

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
        
    def usandoEdicao(self):
        
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

        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.ui.normal.setFont(font)


        #------------------------------------ Mudando as imagens que ficam em baixo dos botoes

        self.ui.imagemNormal.setPixmap(QtGui.QPixmap("./images/EditedIcons/brilhoIcon.png"))

        self.ui.imagemCinza.setPixmap(QtGui.QPixmap("./images/EditedIcons/contrasteIcon.png"))

        self.ui.imgaemSegmentada.setPixmap(QtGui.QPixmap("./images/EditedIcons/rotacaoIcon.png"))

        self.ui.imagemBlur.setPixmap(QtGui.QPixmap("./images/EditedIcons/temperaturaIcon.png"))
        
        self.ui.imagemContraste.setPixmap(QtGui.QPixmap("./images/EditedIcons/sombraIcon.png")) # funcao de realçar

        self.ui.filtro6_imagem.setPixmap(QtGui.QPixmap("./images/EditedIcons/saturacaoIcon.png")) # Fazer filtro 6

        self.ui.filtro7_imagem.setPixmap(QtGui.QPixmap("./images/EditedIcons/realcaoIcon.png"))    # Fazer filtro 7

        self.ui.filtro8_imagem.setPixmap(QtGui.QPixmap("./images/EditedIcons/nitidezicon.png"))  # Fazer filtro 8

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

        # -------------------------------------- Mudando o valor do slider ------------
        
 
    def normal(self):

        
        if(self.toUsandoFiltro):

            if(self.do_i_edited_an_image == True):

                self.ui.image_label.setPixmap(QtGui.QPixmap(toNormal("./images/PhotoInEdition/edited.jpg")))
            
            else:
                print("Função de normal usando foto taked")
                self.ui.image_label.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))
            
            
        else:
            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            font.setItalic(False)
            font.setUnderline(True)
            font.setWeight(75)
            self.ui.normal.setFont(font)

            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(50)
            
            self.ui.segmentar.setFont(font)            
            self.ui.cinzar.setFont(font)
            self.ui.blur.setFont(font)
            self.ui.contraste.setFont(font)
            self.ui.filtro6.setFont(font)
            self.ui.filtro7.setFont(font)            
            self.ui.filtro8.setFont(font)

            
            self.queFuncaoEdicao = 0    # variavel queFuncaoEdicao escolhido para armazenar botao selecionado
            self.ui.slider.setValue(self.sliderValues[0])

    
    def cinza(self):
        
        if(self.toUsandoFiltro):
            
            if(self.do_i_edited_an_image == True):
    
                self.ui.image_label.setPixmap(QtGui.QPixmap(toGray("./images/PhotoInEdition/edited.jpg")))
            
            else:
                print("Função de normal usando foto taked")
                self.ui.image_label.setPixmap(QtGui.QPixmap(toGray(IMAGE_TAKED)))
            
        else:
            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            font.setItalic(False)
            font.setUnderline(True)
            font.setWeight(75)
            self.ui.cinzar.setFont(font)

            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(50)
            
            self.ui.segmentar.setFont(font)            
            self.ui.normal.setFont(font)
            self.ui.blur.setFont(font)
            self.ui.contraste.setFont(font)
            self.ui.filtro6.setFont(font)
            self.ui.filtro7.setFont(font)            
            self.ui.filtro8.setFont(font)

            self.queFuncaoEdicao = 1    # variavel queFuncaoEdicao escolhido para armazenar botao selecionado
            self.ui.slider.setValue(self.sliderValues[1])  
        
    def segmentarImage(self):
        
        if(self.toUsandoFiltro):

            if(self.do_i_edited_an_image == True):
            
                self.ui.image_label.setPixmap(QtGui.QPixmap(toNormal("./images/PhotoInEdition/edited.jpg")))
            
            else:
                self.ui.image_label.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))
                

        else:

            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            font.setItalic(False)
            font.setUnderline(True)
            font.setWeight(75)
            self.ui.segmentar.setFont(font)

            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(50)
            
            self.ui.cinzar.setFont(font)            
            self.ui.normal.setFont(font)
            self.ui.blur.setFont(font)
            self.ui.contraste.setFont(font)
            self.ui.filtro6.setFont(font)
            self.ui.filtro7.setFont(font)            
            self.ui.filtro8.setFont(font)
    

            self.queFuncaoEdicao = 2    # variavel queFuncaoEdicao escolhido para armazenar botao selecionado
            self.ui.slider.setValue(self.sliderValues[2])
    
    
    def smooth(self):

        if(self.toUsandoFiltro):
            
            if(self.do_i_edited_an_image == True):
            
                self.ui.image_label.setPixmap(QtGui.QPixmap(smooth("./images/PhotoInEdition/edited.jpg")))
            
            else:
                self.ui.image_label.setPixmap(QtGui.QPixmap(smooth(IMAGE_TAKED)))

        else:

            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            font.setItalic(False)
            font.setUnderline(True)
            font.setWeight(75)
            self.ui.blur.setFont(font)

            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(50)
            
            self.ui.cinzar.setFont(font)            
            self.ui.normal.setFont(font)
            self.ui.contraste.setFont(font)
            self.ui.segmentar.setFont(font)
            self.ui.filtro6.setFont(font)
            self.ui.filtro7.setFont(font)            
            self.ui.filtro8.setFont(font)
    

            self.queFuncaoEdicao = 3    # variavel queFuncaoEdicao escolhido para armazenar botao selecionado
            self.ui.slider.setValue(self.sliderValues[3])
            print("Usando edição Temperatura")  
     
    def realcar(self):
        if(self.toUsandoFiltro):
           
            if(self.do_i_edited_an_image == True):
                
                self.ui.image_label.setPixmap(QtGui.QPixmap(toNormal("./images/PhotoInEdition/edited.jpg")))
            
            else:
                self.ui.image_label.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))

        else:

            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            font.setItalic(False)
            font.setUnderline(True)
            font.setWeight(75)
            self.ui.contraste.setFont(font)

            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(50)
            
            self.ui.cinzar.setFont(font)            
            self.ui.normal.setFont(font)
            self.ui.blur.setFont(font)
            self.ui.segmentar.setFont(font)
            self.ui.filtro6.setFont(font)
            self.ui.filtro7.setFont(font)            
            self.ui.filtro8.setFont(font)
    

            self.queFuncaoEdicao = 4    # variavel queFuncaoEdicao escolhido para armazenar botao selecionado
            self.ui.slider.setValue(self.sliderValues[4])
            print("Usando edição Contraste")

    def filtro6(self):                                                         # Mudar o filtro [ toGray() ] usado para o filtro 6 feito 
        
        if(self.toUsandoFiltro):
            
            if(self.do_i_edited_an_image == True):
                
                self.ui.image_label.setPixmap(QtGui.QPixmap(toNormal("./images/PhotoInEdition/edited.jpg")))
            
            else:
                self.ui.image_label.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))

        else:

            
            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            font.setItalic(False)
            font.setUnderline(True)
            font.setWeight(75)
            self.ui.filtro6.setFont(font)

            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(50)
            
            self.ui.cinzar.setFont(font)            
            self.ui.normal.setFont(font)
            self.ui.blur.setFont(font)
            self.ui.segmentar.setFont(font)
            self.ui.contraste.setFont(font)
            self.ui.filtro7.setFont(font)            
            self.ui.filtro8.setFont(font)

            self.queFuncaoEdicao = 5    #                            variavel queFuncaoEdicao escolhido para armazenar botao selecionado
            self.ui.slider.setValue(self.sliderValues[5])
            

    def filtro7(self):                                                         # Mudar o filtro [ toNormal() ] usado para o filtro 7 feito 
        
        if(self.toUsandoFiltro):
            
            if(self.do_i_edited_an_image == True):
                
                self.ui.image_label.setPixmap(QtGui.QPixmap(toNormal("./images/PhotoInEdition/edited.jpg")))
            
            else:
                self.ui.image_label.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))


        else:

            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            font.setItalic(False)
            font.setUnderline(True)
            font.setWeight(75)
            self.ui.filtro7.setFont(font)

            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(50)
            
            self.ui.cinzar.setFont(font)            
            self.ui.normal.setFont(font)
            self.ui.blur.setFont(font)
            self.ui.segmentar.setFont(font)
            self.ui.contraste.setFont(font)
            self.ui.filtro6.setFont(font)            
            self.ui.filtro8.setFont(font)

            self.queFuncaoEdicao = 6    # variavel queFuncaoEdicao escolhido para armazenar botao selecionado
            self.ui.slider.setValue(self.sliderValues[6])
            
            print("Usando edição Nitidez")
        
    def filtro8(self):                                                          # Mudar o filtro [ toGray() ] usado para o filtro 8 feito
        
        if(self.toUsandoFiltro):
            
            if(self.do_i_edited_an_image == True):
                
                self.ui.image_label.setPixmap(QtGui.QPixmap(toNormal("./images/PhotoInEdition/edited.jpg")))
            
            else:
                self.ui.image_label.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))

        else:

            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            font.setItalic(False)
            font.setUnderline(True)
            font.setWeight(75)
            self.ui.filtro8.setFont(font)

            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(50)
            
            self.ui.cinzar.setFont(font)            
            self.ui.normal.setFont(font)
            self.ui.blur.setFont(font)
            self.ui.segmentar.setFont(font)
            self.ui.contraste.setFont(font)
            self.ui.filtro7.setFont(font)            
            self.ui.filtro6.setFont(font)

            self.queFuncaoEdicao = 7    # variavel queFuncaoEdicao escolhido para armazenar botao selecionado
            self.ui.slider.setValue(self.sliderValues[7])
            print("Usando edição Vinheta")


    def sliderChange(self):
        
        if(self.queFuncaoEdicao == 0):
            
            self.ui.image_label.setPixmap(QtGui.QPixmap(brilho(IMAGE_TAKED, self.ui.slider.value())))
            self.sliderValues[0] = self.ui.slider.value

            print("Valor do slider= " + "{}".format(self.ui.slider.value))
        
        elif(self.queFuncaoEdicao == 1):

            if(self.do_i_edited_an_image == True):
            
                self.ui.image_label.setPixmap(QtGui.QPixmap(smoothTeste("./images/PhotoInEdition/edited.jpg", self.ui.slider.value())))

            else:
                self.ui.image_label.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))

                    
        elif(self.queFuncaoEdicao == 2):
                
            if(self.do_i_edited_an_image == True):
                
                self.ui.image_label.setPixmap(QtGui.QPixmap(rotacionar("./images/PhotoInEdition/edited.jpg", self.ui.slider.value())))

            else:
                self.ui.image_label.setPixmap(QtGui.QPixmap(rotacionar(IMAGE_TAKED, self.ui.slider.value())))
        
        elif(self.queFuncaoEdicao == 3):
                
            if(self.do_i_edited_an_image == True):
                
                self.ui.image_label.setPixmap(QtGui.QPixmap(converte_temp("./images/PhotoInEdition/edited.jpg", self)))
            else:
                
                self.ui.image_label.setPixmap(QtGui.QPixmap(converte_temp(IMAGE_TAKED, self)))

        elif(self.queFuncaoEdicao == 4):
                
            if(self.do_i_edited_an_image == True):
                
                self.ui.image_label.setPixmap(QtGui.QPixmap(converte_temp("./images/PhotoInEdition/edited.jpg", self)))
                
            else:
                self.ui.image_label.setPixmap(QtGui.QPixmap(converte_temp(IMAGE_TAKED, self)))
        
        elif(self.queFuncaoEdicao == 5):
                
            if(self.do_i_edited_an_image == True):
                
                self.ui.image_label.setPixmap(QtGui.QPixmap(converte_temp("./images/PhotoInEdition/edited.jpg", self)))

            else:
                self.ui.image_label.setPixmap(QtGui.QPixmap(converte_temp(IMAGE_TAKED, self)))    
                

        elif(self.queFuncaoEdicao == 6):

            if(self.do_i_edited_an_image == True):
                
                self.ui.image_label.setPixmap(QtGui.QPixmap(converte_temp("./images/PhotoInEdition/edited.jpg", self)))
              
            else:
                self.ui.image_label.setPixmap(QtGui.QPixmap(converte_temp(IMAGE_TAKED, self)))
        
        elif(self.queFuncaoEdicao == 7):

            if(self.do_i_edited_an_image == True):
                
                self.ui.image_label.setPixmap(QtGui.QPixmap(converte_temp("./images/PhotoInEdition/edited.jpg", self)))
            
            else:
                
                self.ui.image_label.setPixmap(QtGui.QPixmap(converte_temp(IMAGE_TAKED, self)))


    