import os, os.path
import cv2


from PyQt5 import QtGui

from forms.EdicaoFotoForm import Ui_Edicao_Foto_Form
from PyQt5 import QtCore, QtWidgets

from funcoesModificao.cinzaImage import toGray
from funcoesModificao.normal_Image import toNormal
from funcoesModificao.brilho import brilho
from funcoesModificao.rotacao import rotacionar
from funcoesModificao.warmth import warmth
from funcoesModificao.saturation import saturaration
from funcoesModificao.contraste import contraste
from funcoesModificao.luminancia import luminancia
from funcoesModificao.vinheta import vinheta



IMAGE_FILTERED = "./images/PhotoInEdition/filtered.jpg"
IMAGE_TAKED = "./images/PhotoInEdition/fotoTirada.jpg"



class TelaEdicao(QtWidgets.QWidget):

    primeiraIteracao = 0

    voltando = QtCore.pyqtSignal()

    inicialScreen = QtCore.pyqtSignal()

    toUsandoFiltro = True

    sliderValues = [0] * 8

    sliderValues[0] = 127
    sliderValues[1] = 127
    sliderValues[2] = 127
    sliderValues[3] = 127
    sliderValues[4] = 127
    sliderValues[5] = 127
    sliderValues[6] = 127
    sliderValues[7] = 127

    queFuncaoEdicao = 0

    do_i_edited_an_image = os.path.exists("./images/PhotoInEdition/edited.jpg")
    do_i_filtered_an_image = os.path.exists("./images/PhotoInEdition/filtered.jpg")

    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Edicao_Foto_Form()
        self.ui.setupUi(self)
        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(IMAGE_TAKED))
        self.image = None
        self.ui.slider.setValue(self.sliderValues[0])
        #----- Setar a imagens dos Filtros ---------------------------------------

  
        self.ui.imagemFuncao1.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))

        self.ui.imagemFuncao2.setPixmap(QtGui.QPixmap(toGray(IMAGE_TAKED)))

        self.ui.imagemFuncao4.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))

        self.ui.imagemFuncao3.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))

        self.ui.imagemFuncao5.setPixmap(QtGui.QPixmap(toGray(IMAGE_TAKED))) # funcao de realçar

        self.ui.imagemFuncao6.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED))) # Fazer filtro 6

        self.ui.imagemFuncao7.setPixmap(QtGui.QPixmap(toGray(IMAGE_TAKED)))    # Fazer filtro 7

        self.ui.imagemFuncao8.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))  # Fazer filtro 8

                   
        
        #----- Pages Buttons Actons on Clicked -------------------------------------

        self.ui.publicar.clicked.connect(self.telaInicial)
        self.ui.voltar.clicked.connect(self.voltar)
        
        # ----Filters Buttons Actions on Clicked -----------------------
        
        self.ui.funcao1.clicked.connect(self.funcao1)
        self.ui.funcao2.clicked.connect(self.funcao2)
        self.ui.funcao3.clicked.connect(self.funcao3)
        self.ui.funcao4.clicked.connect(self.funcao4)
        self.ui.funcao5.clicked.connect(self.funcao5)
        self.ui.funcao6.clicked.connect(self.funcao6)
        self.ui.funcao7.clicked.connect(self.funcao7)
        self.ui.funcao8.clicked.connect(self.funcao8)

        # --- Buttons ( Filtros & Editar) Actions on Clicked -------------

        self.ui.botaoFiltro.clicked.connect(self.usandoFiltro)
        self.ui.botaoEditar.clicked.connect(self.usandoEdicao)

        # ----- Funcao que pega o valor do slider

        self.ui.slider.valueChanged.connect(self.sliderChange)
        

    # Funções Para mudar de Tela

    def telaInicial(self):

        self.do_i_edited_an_image  = os.path.exists("./images/PhotoInEdition/edited.jpg")
        
        self.do_i_filtered_an_image  = os.path.exists("./images/PhotoInEdition/filtered.jpg")
    
        
        img_dir = "./images/PublishedPhoto/" # Enter Directory of all images         
        length = len([name for name in os.listdir(img_dir) ])
        img = None

        if(self.do_i_edited_an_image == True):
            img = cv2.imread("./images/PhotoInEdition/edited.jpg")
        
        elif(self.do_i_filtered_an_image == True):
            
            img = cv2.imread(IMAGE_FILTERED)
        
        else:
            img = cv2.imread(IMAGE_TAKED)

        img_dir = "./images/PublishedPhoto/image"
        
        final = img_dir + "{}".format(length) + "{}".format(".jpg")
        
        cv2.imwrite(final, img)
        
        #--------- Limpando as fotos que estão nas pastas
        
        pasta1 = "./images/PhotoInEdition/" 
        pasta2 = "./images/FuncaoDeEdicao/" 
        

        for image in os.listdir(pasta1):
            os.remove(image)     
                
        for image in os.listdir(pasta2):
            os.remove(image)     

        self.inicialScreen.emit()

    def voltar(self):
        
        #--------- Limpando as fotos que estão nas pastas
        
        pasta1 = "./images/PhotoInEdition/" 
        pasta2 = "./images/FuncaoDeEdicao/" 
        

        for image in os.listdir(pasta1):
            os.remove(image)     
                
        for image in os.listdir(pasta2):
            os.remove(image)     

        self.voltando.emit()

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

        # ------------------------------------- Apagar Todas as imagens editadas e deixar a versao final na pasta PhotosInEdition
        
        img_dir = "./images/FuncaoDeEdicao/" 
        
        length = len([name for name in os.listdir(img_dir) ]) 
        
        finalimageEdited = "edited" + (length-1) + ".jpg"

        for image in os.listdir(img_dir):

            if(image == finalimageEdited):
                
                imagemEditada = img_dir + image

                img = cv2.imread(imagemEditada)
                cv2.imwrite("./images/PhotoInEdition/edited.jpg",img)
                
            os.remove(image)     

        # ------------------- Vê se existe a foto editada pelas funções de edição
        
        self.do_i_edited_an_image  = os.path.exists("./images/PhotoInEdition/edited.jpg")
    
        if(self.do_i_edited_an_image == True):
                
            self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toNormal("./images/PhotoInEdition/edited.jpg")))
            self.ui.imagemFuncao1.setPixmap(QtGui.QPixmap(toNormal("./images/PhotoInEdition/edited.jpg")))
            self.ui.imagemFuncao2.setPixmap(QtGui.QPixmap( toGray("./images/PhotoInEdition/edited.jpg")))
            self.ui.imagemFuncao3.setPixmap(QtGui.QPixmap(toGray("./images/PhotoInEdition/edited.jpg")))
            self.ui.imagemFuncao4.setPixmap(QtGui.QPixmap(toGray("./images/PhotoInEdition/edited.jpg")))
            self.ui.imagemFuncao5.setPixmap(QtGui.QPixmap(toGray("./images/PhotoInEdition/edited.jpg")))
            self.ui.imagemFuncao6.setPixmap(QtGui.QPixmap(toNormal("./images/PhotoInEdition/edited.jpg"))) # Fazer filtro 6
            self.ui.imagemFuncao7.setPixmap(QtGui.QPixmap(toNormal("./images/PhotoInEdition/edited.jpg"))) # Fazer filtro 7
            self.ui.imagemFuncao8.setPixmap(QtGui.QPixmap(toNormal("./images/PhotoInEdition/edited.jpg"))) # Fazer filtro 8

        else:
            self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))
            self.ui.imagemFuncao1.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))
            self.ui.imagemFuncao2.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))
            self.ui.imagemFuncao3.setPixmap(QtGui.QPixmap(toGray(IMAGE_TAKED)))
            self.ui.imagemFuncao4.setPixmap(QtGui.QPixmap(toGray(IMAGE_TAKED)))
            self.ui.imagemFuncao5.setPixmap(QtGui.QPixmap(toGray(IMAGE_TAKED)))
            self.ui.imagemFuncao6.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED))) # Fazer filtro 6
            self.ui.imagemFuncao7.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED))) # Fazer filtro 7
            self.ui.imagemFuncao8.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED))) # Fazer filtro 8
        
        # ------------------------------------ Tornando o Slider Invisivel e indisponivel

        self.ui.slider.setVisible(False)
        self.ui.slider.setEnabled(False)

        # -------------------------------------- Setando a variavel para mudar a funcao dos botoes para funções de filtro
        self.toUsandoFiltro = True

        # -------------------------------------- Mudando o nome dos botões ------------
        _translate = QtCore.QCoreApplication.translate        
        self.ui.funcao1.setText(_translate("Form", "Normal"))
        self.ui.funcao2.setText(_translate("Form", "Cinza"))
        self.ui.funcao3.setText(_translate("Form", "Função 3"))
        self.ui.funcao4.setText(_translate("Form", "Função 4"))
        self.ui.funcao5.setText(_translate("Form", "Função 5"))
        self.ui.funcao6.setText(_translate("Form", "Função 6"))
        self.ui.funcao7.setText(_translate("Form", "Função 7"))
        self.ui.funcao8.setText(_translate("Form", "Função 8"))
        
        #--------------------------------------- Seta a fonte dos botoes da cada filtro
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.ui.funcao1.setFont(font)
        self.ui.funcao3.setFont(font)            
        self.ui.funcao2.setFont(font)
        self.ui.funcao4.setFont(font)
        self.ui.funcao5.setFont(font)
        self.ui.funcao6.setFont(font)
        self.ui.funcao7.setFont(font)            
        self.ui.funcao8.setFont(font)
     
    def usandoEdicao(self):

        self.do_i_filtered_an_image = os.path.exists("./images/PhotoInEdition/filtered.jpg")
        
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
        self.ui.funcao1.setFont(font)

        #------------------------------------ Mudando as imagens que ficam em baixo dos botoes

        self.ui.imagemFuncao1.setPixmap(QtGui.QPixmap("./images/EditedIcons/brilhoIcon.png"))

        self.ui.imagemFuncao2.setPixmap(QtGui.QPixmap("./images/EditedIcons/saturacaoIcon.png"))

        self.ui.imagemFuncao3.setPixmap(QtGui.QPixmap("./images/EditedIcons/rotacaoIcon.png"))

        self.ui.imagemFuncao4.setPixmap(QtGui.QPixmap("./images/EditedIcons/temperaturaIcon.png"))
        
        self.ui.imagemFuncao5.setPixmap(QtGui.QPixmap("./images/EditedIcons/contrasteIcon.png")) # funcao de realçar

        self.ui.imagemFuncao6.setPixmap(QtGui.QPixmap("./images/EditedIcons/sombraIcon.png")) # Fazer filtro 6

        self.ui.imagemFuncao7.setPixmap(QtGui.QPixmap("./images/EditedIcons/nitidezIcon.png"))    # Fazer filtro 7

        self.ui.imagemFuncao8.setPixmap(QtGui.QPixmap("./images/EditedIcons/vinhetaIconIcon.png"))  # Fazer filtro 8

        # ------------------------------------ Tornando o Slider Visivel e disponivel

        self.ui.slider.setVisible(True)
        self.ui.slider.setEnabled(True)

        # -------------------------------------- Setando a variavel para mudar a funcao dos botoes para funções de edição 
        self.toUsandoFiltro = False
        
        # -------------------------------------- Mudando o nome dos botões ------------
        _translate = QtCore.QCoreApplication.translate        
        self.ui.funcao1.setText(_translate("Form", "Brilho"))
        self.ui.funcao2.setText(_translate("Form", "Saturação"))
        self.ui.funcao3.setText(_translate("Form", "Rotação"))
        self.ui.funcao4.setText(_translate("Form", "Temperatura"))
        self.ui.funcao5.setText(_translate("Form", "Contraste"))
        self.ui.funcao6.setText(_translate("Form", "Fazer Filtro"))
        self.ui.funcao7.setText(_translate("Form", "Iluminância"))
        self.ui.funcao8.setText(_translate("Form", "Vinheta"))

        # -------------------------------------- Mudando o valor do slider ------------
        self.primeiraIteracao = 0
         
    def funcao1(self):                                                         # Colocar Função de Filtro 1 aqui

        
        if(self.toUsandoFiltro):

            if(self.do_i_edited_an_image == True):

                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toNormal("./images/PhotoInEdition/edited.jpg")))
            
            else:
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))
            
            
        else:
            
            # Função de brilho
            
            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            font.setItalic(False)
            font.setUnderline(True)
            font.setWeight(75)
            self.ui.funcao1.setFont(font)

            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(50)
            
            self.ui.funcao3.setFont(font)            
            self.ui.funcao2.setFont(font)
            self.ui.funcao4.setFont(font)
            self.ui.funcao5.setFont(font)
            self.ui.funcao6.setFont(font)
            self.ui.funcao7.setFont(font)            
            self.ui.funcao8.setFont(font)

            
            self.queFuncaoEdicao = 0    # variavel queFuncaoEdicao escolhido para armazenar botao selecionado
            
            self.ui.slider.setEnabled(False) 
            self.primeiraIteracao = 0
            valor = self.sliderValues[0]
            self.ui.slider.setValue(valor)
            self.ui.slider.setEnabled(True)

    def funcao2(self):                                                         # Colocar Função de Filtro 2 aqui
        
        if(self.toUsandoFiltro):
            
            if(self.do_i_edited_an_image == True):
    
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toGray("./images/PhotoInEdition/edited.jpg")))  # Colocar Função 3
            
            else:
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toGray(IMAGE_TAKED)))
            
        else:

            # Saturação
            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            font.setItalic(False)
            font.setUnderline(True)
            font.setWeight(75)
            self.ui.funcao2.setFont(font)

            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(50)
            
            self.ui.funcao3.setFont(font)            
            self.ui.funcao1.setFont(font)
            self.ui.funcao4.setFont(font)
            self.ui.funcao5.setFont(font)
            self.ui.funcao6.setFont(font)
            self.ui.funcao7.setFont(font)            
            self.ui.funcao8.setFont(font)

            self.queFuncaoEdicao = 1    # variavel queFuncaoEdicao escolhido para armazenar botao selecionado
            
            self.ui.slider.setEnabled(False) 
            valor = self.sliderValues[1]
            self.ui.slider.setValue(valor)
            self.ui.slider.setEnabled(True)
            
    def funcao3(self):                                                         # Colocar Função de Filtro 3 aqui
        
        if(self.toUsandoFiltro):

            if(self.do_i_edited_an_image == True):
            
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toNormal("./images/PhotoInEdition/edited.jpg")))
            
            else:
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))
                

        else:
            # Rotação
            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            font.setItalic(False)
            font.setUnderline(True)
            font.setWeight(75)
            self.ui.funcao3.setFont(font)

            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(50)
            
            self.ui.funcao2.setFont(font)            
            self.ui.funcao1.setFont(font)
            self.ui.funcao4.setFont(font)
            self.ui.funcao5.setFont(font)
            self.ui.funcao6.setFont(font)
            self.ui.funcao7.setFont(font)            
            self.ui.funcao8.setFont(font)
    

            self.queFuncaoEdicao = 2    # variavel queFuncaoEdicao escolhido para armazenar botao selecionado
            
            self.ui.slider.setEnabled(False) 
            self.primeiraIteracao = 0
            valor = self.sliderValues[2]
            self.ui.slider.setValue(valor)
            self.ui.slider.setEnabled(True)
                       
    def funcao4(self):                                                         # Colocar Função de Filtro 4 aqui

        if(self.toUsandoFiltro):
            
            if(self.do_i_edited_an_image == True):
            
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toNormal("./images/PhotoInEdition/edited.jpg")))
            
            else:
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))

        else:
            # Temperatura
            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            font.setItalic(False)
            font.setUnderline(True)
            font.setWeight(75)
            self.ui.funcao4.setFont(font)

            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(50)
            
            self.ui.funcao2.setFont(font)            
            self.ui.funcao1.setFont(font)
            self.ui.funcao5.setFont(font)
            self.ui.funcao3.setFont(font)
            self.ui.funcao6.setFont(font)
            self.ui.funcao7.setFont(font)            
            self.ui.funcao8.setFont(font)
    

            self.queFuncaoEdicao = 3    # variavel queFuncaoEdicao escolhido para armazenar botao selecionado

            self.ui.slider.setEnabled(False) 
            self.primeiraIteracao = 0
            valor = self.sliderValues[3]
            self.ui.slider.setValue(valor)
            self.ui.slider.setEnabled(True)
     
    def funcao5(self):                                                         # Colocar Função de Filtro 5 aqui

        if(self.toUsandoFiltro):
           
            if(self.do_i_edited_an_image == True):
                
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toNormal("./images/PhotoInEdition/edited.jpg")))
            
            else:
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))

        else:

            #Contraste
            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            font.setItalic(False)
            font.setUnderline(True)
            font.setWeight(75)
            self.ui.funcao5.setFont(font)

            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(50)
            
            self.ui.funcao2.setFont(font)            
            self.ui.funcao1.setFont(font)
            self.ui.funcao4.setFont(font)
            self.ui.funcao3.setFont(font)
            self.ui.funcao6.setFont(font)
            self.ui.funcao7.setFont(font)            
            self.ui.funcao8.setFont(font)
    

            self.queFuncaoEdicao = 4    # variavel queFuncaoEdicao escolhido para armazenar botao selecionado
            self.ui.slider.setEnabled(False) 
            self.primeiraIteracao = 0
            valor = self.sliderValues[4]
            self.ui.slider.setValue(valor)
            self.ui.slider.setEnabled(True)
            
    def funcao6(self):                                                         # Colocar Função de Filtro 6 aqui 
        
        if(self.toUsandoFiltro):
            
            if(self.do_i_edited_an_image == True):
                
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toNormal("./images/PhotoInEdition/edited.jpg")))
            
            else:
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))

        else:

            # Iluminancia

            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            font.setItalic(False)
            font.setUnderline(True)
            font.setWeight(75)
            self.ui.funcao6.setFont(font)

            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(50)
            
            self.ui.funcao2.setFont(font)            
            self.ui.funcao1.setFont(font)
            self.ui.funcao4.setFont(font)
            self.ui.funcao3.setFont(font)
            self.ui.funcao5.setFont(font)
            self.ui.funcao7.setFont(font)            
            self.ui.funcao8.setFont(font)

            self.queFuncaoEdicao = 5    #                            variavel queFuncaoEdicao escolhido para armazenar botao selecionado
            self.ui.slider.setEnabled(False) 
            self.primeiraIteracao = 0
            valor = self.sliderValues[5]
            self.ui.slider.setValue(valor)
            self.ui.slider.setEnabled(True)
            
    def funcao7(self):                                                         # Colocar Função de Filtro 7 aqui
        
        if(self.toUsandoFiltro):
            
            if(self.do_i_edited_an_image == True):
                
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toNormal("./images/PhotoInEdition/edited.jpg")))
            
            else:
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))


        else:
            # Nitidez
            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            font.setItalic(False)
            font.setUnderline(True)
            font.setWeight(75)
            self.ui.funcao7.setFont(font)

            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(50)
            
            self.ui.funcao2.setFont(font)            
            self.ui.funcao1.setFont(font)
            self.ui.funcao4.setFont(font)
            self.ui.funcao3.setFont(font)
            self.ui.funcao5.setFont(font)
            self.ui.funcao6.setFont(font)            
            self.ui.funcao8.setFont(font)

            self.queFuncaoEdicao = 6    # variavel queFuncaoEdicao escolhido para armazenar botao selecionado
            
            valor = self.sliderValues[6]
            self.ui.slider.setEnabled(False) 
            self.primeiraIteracao = 0
            valor = self.sliderValues[6]
            self.ui.slider.setValue(valor)
            self.ui.slider.setEnabled(True)
        
    def funcao8(self):                                                         # Colocar Função de Filtro 8 aqui
        
        if(self.toUsandoFiltro):
            
            if(self.do_i_edited_an_image == True):
                
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toNormal("./images/PhotoInEdition/edited.jpg")))
            
            else:
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))

        else:

            # Vinheta
            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            font.setItalic(False)
            font.setUnderline(True)
            font.setWeight(75)
            self.ui.funcao8.setFont(font)

            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(50)
            
            self.ui.funcao2.setFont(font)            
            self.ui.funcao1.setFont(font)
            self.ui.funcao4.setFont(font)
            self.ui.funcao3.setFont(font)
            self.ui.funcao5.setFont(font)
            self.ui.funcao7.setFont(font)            
            self.ui.funcao6.setFont(font)

            self.queFuncaoEdicao = 7    # variavel queFuncaoEdicao escolhido para armazenar botao selecionado
            
            self.ui.slider.setEnabled(False) 
            self.primeiraIteracao = 0
            valor = self.sliderValues[7]
            self.ui.slider.setValue(valor)
            self.ui.slider.setEnabled(True)
            
            
            print("Usando edição Vinheta")

    def sliderChange(self):
        
        if(self.ui.slider.isEnabled):

            if(self.primeiraIteracao == 0):
                
                self.img_dir = "./images/FuncaoDeEdicao/" # Enter Directory of all images         
                self.length = len([name for name in os.listdir(self.img_dir) ])
                
                if(self.length > 0):
                    self.imagePath = "./images/FuncaoDeEdicao/edited"+"{}".format(self.length-1) + "{}".format(".jpg")
                else:
                    self.imagePath = "./images/FuncaoDeEdicao/edited"+"{}".format(self.length) + "{}".format(".jpg")

                self.tenhoEssaImagem = os.path.exists(self.imagePath)
                self.primeiraIteracao = 1
                
            
            if(self.queFuncaoEdicao == 0):  #Brilho
                            
                if( self.length > 0 ):
                    
                    self.ui.imagemCentral.setPixmap(QtGui.QPixmap(brilho(self.imagePath, self.ui.slider.value(), self.length )))
        
                else:
                    
                    if(self.do_i_filtered_an_image == True):
                        
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(brilho(IMAGE_FILTERED, self.ui.slider.value(), self.length)))
                    else:
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(brilho(IMAGE_TAKED, self.ui.slider.value(), self.length)))
                
                self.sliderValues[0] = self.ui.slider.value()
                
            elif(self.queFuncaoEdicao == 1): #Saturação

                if(self.length > 0):
                
                    self.ui.imagemCentral.setPixmap(QtGui.QPixmap(saturaration(self.imagePath, self.ui.slider.value(), self.length )))

                else:
                    if(self.do_i_filtered_an_image == True):
                        
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(saturaration(IMAGE_FILTERED, self.ui.slider.value(), self.length)))
                    else:
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(saturaration(IMAGE_TAKED, self.ui.slider.value(), self.length )))

                self.sliderValues[1] = self.ui.slider.value()
                        
            elif(self.queFuncaoEdicao == 2): #Rotação
                    
                if( self.length > 0):
                    
                    self.ui.imagemCentral.setPixmap(QtGui.QPixmap(rotacionar(self.imagePath, self.ui.slider.value(),self.length )))

                else:
                    
                    if(self.do_i_filtered_an_image == True):
                        
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(rotacionar(IMAGE_FILTERED, self.ui.slider.value(), self.length)))
                    else:
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(rotacionar(IMAGE_TAKED, self.ui.slider.value(), self.length)))

                self.sliderValues[2] =  self.ui.slider.value()   


            elif(self.queFuncaoEdicao == 3): #Temperatura
                    
                if( self.length > 0):
                    
                    self.ui.imagemCentral.setPixmap(QtGui.QPixmap(warmth(self.imagePath, self.ui.slider.value(),self.length )))

                else:
                    
                    if(self.do_i_filtered_an_image == True):
                        
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(warmth(IMAGE_FILTERED, self.ui.slider.value(), self.length)))
                    else:
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(warmth(IMAGE_TAKED, self.ui.slider.value(),self.length )))

                self.sliderValues[3] = self.ui.slider.value()    

            elif(self.queFuncaoEdicao == 4): #Contraste
                    
                if( self.length > 0):
                    
                    self.ui.imagemCentral.setPixmap(QtGui.QPixmap(contraste(self.imagePath, self.ui.slider.value(),self.length )))

                else:
                    
                    if(self.do_i_filtered_an_image == True):
                        
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(contraste(IMAGE_FILTERED, self.ui.slider.value(), self.length)))
                    else:
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(contraste(IMAGE_TAKED, self.ui.slider.value(),self.length )))

                self.sliderValues[4] = self.ui.slider.value()    
            
            elif(self.queFuncaoEdicao == 5): # Fazer Filtro usando luminancia como teste
                    
                if( self.length > 0):
                    
                    self.ui.imagemCentral.setPixmap(QtGui.QPixmap(luminancia(self.imagePath, self.ui.slider.value(),self.length )))

                else:
                    if(self.do_i_filtered_an_image == True):
                        
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(luminancia(IMAGE_FILTERED, self.ui.slider.value(), self.length)))
                    else:
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(luminancia(IMAGE_TAKED, self.ui.slider.value(),self.length )))

                self.sliderValues[5] = self.ui.slider.value()    

            elif(self.queFuncaoEdicao == 6): #Iluminancia

                if( self.length > 0):
                    
                    self.ui.imagemCentral.setPixmap(QtGui.QPixmap(luminancia(self.imagePath, self.ui.slider.value(),self.length )))

                else:
                    if(self.do_i_filtered_an_image == True):
                        
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(luminancia(IMAGE_FILTERED, self.ui.slider.value(), self.length)))
                    else:
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(luminancia(IMAGE_TAKED, self.ui.slider.value(),self.length )))

                self.sliderValues[6] = self.ui.slider.value()

            elif(self.queFuncaoEdicao == 7): # Vinheta

                if( self.length > 0):
                    
                    self.ui.imagemCentral.setPixmap(QtGui.QPixmap(vinheta(self.imagePath, self.ui.slider.value(),self.length )))

                else:
                    
                    if(self.do_i_filtered_an_image == True):
                        
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(vinheta(IMAGE_FILTERED, self.ui.slider.value(), self.length)))
                    else:
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(vinheta(IMAGE_TAKED, self.ui.slider.value(),self.length )))

                self.sliderValues[7] = self.ui.slider.value()

    