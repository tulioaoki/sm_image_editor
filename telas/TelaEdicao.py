import os, os.path
import cv2


from PyQt5 import QtGui

from forms.EdicaoFotoForm import Ui_Edicao_Foto_Form
from PyQt5 import QtCore, QtWidgets

from filters.normal_Image import toNormal
from filters.inkwell import toInkwell  # Cinza
from filters.reyes import toReyes
from filters.vintage import toVintage
from filters._1977 import to1977
from filters.gingham  import toGingham
from filters.amaro import toAmaro
from filters.clarendon import toClarendon


from funcoesDeEdicao.brilho import brilho
from funcoesDeEdicao.rotacao import rotacionar
from funcoesDeEdicao.warmth import warmth
from funcoesDeEdicao.saturation import saturaration
from funcoesDeEdicao.contraste import contraste
from funcoesDeEdicao.luminancia import luminancia
from funcoesDeEdicao.vinheta import vinheta
from funcoesDeEdicao.putGlass import toPutGlasses


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
    sliderValues[5] = 2
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
        
        self.ui.slider.setVisible(False)

        #----- Setar a imagens dos Filtros ---------------------------------------


        self.ui.imagemFuncao1.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))  # To Normal

        self.ui.imagemFuncao2.setPixmap(QtGui.QPixmap(toInkwell(IMAGE_TAKED)))    # toInkwell

        self.ui.imagemFuncao3.setPixmap(QtGui.QPixmap(toReyes(IMAGE_TAKED)))  # toReyes

        self.ui.imagemFuncao4.setPixmap(QtGui.QPixmap(toVintage(IMAGE_TAKED)))      # toVintage

        self.ui.imagemFuncao5.setPixmap(QtGui.QPixmap(to1977(IMAGE_TAKED))) # to1977

        self.ui.imagemFuncao6.setPixmap(QtGui.QPixmap(toGingham(IMAGE_TAKED))) # toGingham

        self.ui.imagemFuncao7.setPixmap(QtGui.QPixmap(toAmaro(IMAGE_TAKED)))    # toAmaro

        self.ui.imagemFuncao8.setPixmap(QtGui.QPixmap(toClarendon(IMAGE_TAKED)))  # Put sunglasses

        self.do_i_filtered_an_image = os.path.exists("./images/PhotoInEdition/filtered.jpg")


        imagemFiltradaAnteriormente = "./images/PhotoInEdition/filtered.jpg" 
            
        try:
            os.remove(imagemFiltradaAnteriormente)     
            
        except Exception as e:
            print("Erro ao deletar: " + "{}".format(e))        
                   
        self.do_i_filtered_an_image == False

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
        
        try:
            for image in os.listdir(pasta1):
                
                imagem = pasta1 + image
                os.remove(imagem)     
        
        except Exception as e:
            print("Erro ao deletar: " + "{}".format(e))        
        
        try:
        
            for image in os.listdir(pasta2):
                imagem = pasta2 + image
                os.remove(imagem)

        except Exception as e:
            print("Erro ao deletar: " + e)
        
        self.inicialScreen.emit()

    def voltar(self):
        
        #--------- Limpando as fotos que estão nas pastas
        
        pasta1 = "./images/PhotoInEdition/" 
        pasta2 = "./images/FuncaoDeEdicao/" 
        
        try:
            for image in os.listdir(pasta1):
                
                imagem = pasta1 + image
                os.remove(imagem)     
        
        except Exception as e:
            print("Erro ao deletar: " + "{}".format(e))        
        
        try:
        
            for image in os.listdir(pasta2):
                imagem = pasta2 + image
                os.remove(imagem)

        except Exception as e:
            print("Erro ao deletar: " + e)

        self.sliderValues[0] = 128
        self.sliderValues[1] = 128
        self.sliderValues[2] = 128
        self.sliderValues[3] = 128
        self.sliderValues[4] = 128
        self.sliderValues[5] = 2
        self.sliderValues[6] = 128
        self.sliderValues[7] = 128

        self.voltando.emit()

    def usandoFiltro(self):
        
        # Deletando a imagem que foi filtrada anteriormente para eu poder usar outros filtros

        self.do_i_filtered_an_image = os.path.exists("./images/PhotoInEdition/filtered.jpg")

        if(self.do_i_filtered_an_image == True):

        
            imagemFiltradaAnteriormente = "./images/PhotoInEdition/filtered.jpg" 
            
            try:
                    os.remove(imagemFiltradaAnteriormente)     
            
            except Exception as e:
                print("Erro ao deletar: " + "{}".format(e))        
        
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
        
        queImagem = length -1

        finalimageEdited = "edited" + "{}".format(queImagem) + ".jpg"

        try:
        
            for image in os.listdir(img_dir):
    
                imagemEditada = img_dir + image

                if(image == finalimageEdited):  # Salva a ultima foto editada e coloca ela na pasta PhotoEdition e apaga ela da pasta FuncaoDeEdicao
                    
                    img = cv2.imread(imagemEditada)
                    cv2.imwrite("./images/PhotoInEdition/edited.jpg",img)
                    
                os.remove(imagemEditada)     

        except Exception as e:
            print("Erro ao deletar: " + e)


        
        # ------------------- Vê se existe a foto editada pelas funções de edição

        self.do_i_edited_an_image  = os.path.exists("./images/PhotoInEdition/edited.jpg")
    
        if(self.do_i_edited_an_image == True):
                
            self.ui.imagemFuncao1.setPixmap(QtGui.QPixmap(toNormal("./images/PhotoInEdition/edited.jpg")))
            self.ui.imagemFuncao2.setPixmap(QtGui.QPixmap(toInkwell("./images/PhotoInEdition/edited.jpg")))    # toInkwell
            self.ui.imagemFuncao3.setPixmap(QtGui.QPixmap(toReyes("./images/PhotoInEdition/edited.jpg")))  # toReyes
            self.ui.imagemFuncao4.setPixmap(QtGui.QPixmap(toVintage("./images/PhotoInEdition/edited.jpg"))) # toVintage
            self.ui.imagemFuncao5.setPixmap(QtGui.QPixmap(to1977("./images/PhotoInEdition/edited.jpg")))  #to1977
            self.ui.imagemFuncao6.setPixmap(QtGui.QPixmap(toGingham("./images/PhotoInEdition/edited.jpg"))) #  toGingham
            self.ui.imagemFuncao7.setPixmap(QtGui.QPixmap(toAmaro("./images/PhotoInEdition/edited.jpg")))    # toAmaro
            self.ui.imagemFuncao8.setPixmap(QtGui.QPixmap(toClarendon("./images/PhotoInEdition/edited.jpg")))  # Put sunglasses

        else:
            self.ui.imagemFuncao1.setPixmap(QtGui.QPixmap(toNormal(IMAGE_TAKED)))  # To Normal
            self.ui.imagemFuncao2.setPixmap(QtGui.QPixmap(toInkwell(IMAGE_TAKED)))    # toInkwell
            self.ui.imagemFuncao3.setPixmap(QtGui.QPixmap(toReyes(IMAGE_TAKED)))  # toReyes
            self.ui.imagemFuncao4.setPixmap(QtGui.QPixmap(toVintage(IMAGE_TAKED))) # toVintage
            self.ui.imagemFuncao5.setPixmap(QtGui.QPixmap(to1977(IMAGE_TAKED)))  #to1977
            self.ui.imagemFuncao6.setPixmap(QtGui.QPixmap(toGingham(IMAGE_TAKED))) #  toGingham
            self.ui.imagemFuncao7.setPixmap(QtGui.QPixmap(toAmaro(IMAGE_TAKED)))    # toAmaro
            self.ui.imagemFuncao8.setPixmap(QtGui.QPixmap(toClarendon(IMAGE_TAKED)))  # Put sunglasses

        
        # ------------------------------------ Tornando o Slider Invisivel e indisponivel

        self.ui.slider.setVisible(False)
        self.ui.slider.setEnabled(False)

        # -------------------------------------- Setando a variavel para mudar a funcao dos botoes para funções de filtro
        self.toUsandoFiltro = True

        # -------------------------------------- Mudando o nome dos botões ------------
        _translate = QtCore.QCoreApplication.translate        
        self.ui.funcao1.setText(_translate("Form", "Normal"))
        self.ui.funcao2.setText(_translate("Form", "Inkwell"))
        self.ui.funcao3.setText(_translate("Form", "Reyes"))
        self.ui.funcao4.setText(_translate("Form", "Vintage"))
        self.ui.funcao5.setText(_translate("Form", "1977"))
        self.ui.funcao6.setText(_translate("Form", "Amaro"))
        self.ui.funcao7.setText(_translate("Form", "Gingham"))
        self.ui.funcao8.setText(_translate("Form", "Clarendon"))
        
        
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

        # Deletando a foto editada já que vamos editar ela denovo com brilho , rotação , contraste, ......

        self.do_i_edited_an_image = os.path.exists("./images/PhotoInEdition/edited.jpg")

        if(self.do_i_edited_an_image == True):

            print("Deletando foto filtrada")

            imagemEditadaAnteriormente = "./images/PhotoInEdition/edited.jpg" 
            
            try:
                    os.remove(imagemEditadaAnteriormente)     
            
            except Exception as e:
                print("Erro ao deletar: " + "{}".format(e))        
            

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

        self.ui.imagemFuncao6.setPixmap(QtGui.QPixmap("./images/EditedIcons/stickerIcon.png")) # Fazer filtro 6

        self.ui.imagemFuncao7.setPixmap(QtGui.QPixmap("./images/EditedIcons/iluminacaoIcon.png"))    # Fazer filtro 7

        self.ui.imagemFuncao8.setPixmap(QtGui.QPixmap("./images/EditedIcons/vinhetaIcon.png"))  # Fazer filtro 8

        # ------------------------------------ Tornando o Slider Visivel e disponivel

        self.ui.slider.setMaximum(255)
        self.ui.slider.setVisible(True)
        self.ui.slider.setEnabled(True)
        self.ui.slider.setTickInterval(128)
        self.ui.slider.setTickPosition( self.ui.slider.TicksBelow)

        # -------------------------------------- Setando a variavel para mudar a funcao dos botoes para funções de edição 
        self.toUsandoFiltro = False
        
        # -------------------------------------- Mudando o nome dos botões ------------
        _translate = QtCore.QCoreApplication.translate        
        self.ui.funcao1.setText(_translate("Form", "Brilho"))
        self.ui.funcao2.setText(_translate("Form", "Saturação"))
        self.ui.funcao3.setText(_translate("Form", "Rotação"))
        self.ui.funcao4.setText(_translate("Form", "Temperatura"))
        self.ui.funcao5.setText(_translate("Form", "Contraste"))
        self.ui.funcao6.setText(_translate("Form", "Sticker"))
        self.ui.funcao7.setText(_translate("Form", "Iluminação"))
        self.ui.funcao8.setText(_translate("Form", "Vinheta"))

        # -------------------------------------- Mudando o valor do slider ------------
        self.primeiraIteracao = 0
         
    def funcao1(self):                                                         # ToNormal

        
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
            
            self.ui.slider.setMaximum(255)

            self.primeiraIteracao = 0
            valor = self.sliderValues[0]
            self.ui.slider.setValue(valor)
            self.ui.slider.setTickInterval(128)
            self.ui.slider.setTickPosition( self.ui.slider.TicksBelow)
          
    def funcao2(self):                                                         # toInkwell
        
        if(self.toUsandoFiltro):
            
            if(self.do_i_edited_an_image == True):
    
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toInkwell("./images/PhotoInEdition/edited.jpg")))  # Colocar Função 3
            
            else:
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toInkwell(IMAGE_TAKED)))
            
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
            
            self.ui.slider.setMaximum(255)

            self.primeiraIteracao = 0 
            valor = self.sliderValues[1]
            self.ui.slider.setValue(valor)
            self.ui.slider.setTickInterval(128)
            self.ui.slider.setTickPosition( self.ui.slider.TicksBelow)
            
    def funcao3(self):                                                         # toReyes
        
        if(self.toUsandoFiltro):

            if(self.do_i_edited_an_image == True):
            
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toReyes("./images/PhotoInEdition/edited.jpg")))
            
            else:
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toReyes(IMAGE_TAKED)))
                

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
            
            self.ui.slider.setMaximum(255)

            self.primeiraIteracao = 0
            valor = self.sliderValues[2]
            self.ui.slider.setValue(valor)
            self.ui.slider.setTickInterval(128)
            self.ui.slider.setTickPosition( self.ui.slider.TicksBelow)

    def funcao4(self):                                                         # toVintage

        if(self.toUsandoFiltro):
            
            if(self.do_i_edited_an_image == True):
            
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toVintage("./images/PhotoInEdition/edited.jpg")))
            
            else:
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toVintage(IMAGE_TAKED)))

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

            self.ui.slider.setMaximum(255)

            self.primeiraIteracao = 0
            valor = self.sliderValues[3]
            self.ui.slider.setValue(valor)
            self.ui.slider.setTickInterval(128)
            self.ui.slider.setTickPosition( self.ui.slider.TicksBelow)
     
    def funcao5(self):                                                         # to1977

        if(self.toUsandoFiltro):
           
            if(self.do_i_edited_an_image == True):
                
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(to1977("./images/PhotoInEdition/edited.jpg")))
            
            else:
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(to1977(IMAGE_TAKED)))

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

            self.ui.slider.setMaximum(255)

            self.primeiraIteracao = 0
            valor = self.sliderValues[4]
            self.ui.slider.setValue(valor)
            self.ui.slider.setTickInterval(128)
            self.ui.slider.setTickPosition( self.ui.slider.TicksBelow)

    def funcao6(self):                                                         # toGingham 
        
        if(self.toUsandoFiltro):
            
            if(self.do_i_edited_an_image == True):
                
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toGingham("./images/PhotoInEdition/edited.jpg")))
            
            else:
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toGingham(IMAGE_TAKED)))

        else:

            print("Botão 6 -------------------------------------------")

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

            self.ui.slider.setMaximum(4)
        
            self.queFuncaoEdicao = 5    #                            variavel queFuncaoEdicao escolhido para armazenar botao selecionado
            self.primeiraIteracao = 0
            valor = self.sliderValues[5]
            self.ui.slider.setValue(valor)
            self.ui.slider.setTickInterval(1)
            self.ui.slider.setTickPosition( self.ui.slider.TicksBelow)
            
    def funcao7(self):                                                         # toAmaro
        
        if(self.toUsandoFiltro):
            
            if(self.do_i_edited_an_image == True):
                
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toAmaro("./images/PhotoInEdition/edited.jpg")))
            
            else:
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toAmaro(IMAGE_TAKED)))


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
            
            self.ui.slider.setMaximum(255)
        
            valor = self.sliderValues[6]
            self.primeiraIteracao = 0
            valor = self.sliderValues[6]
            self.ui.slider.setValue(valor)
            self.ui.slider.setTickInterval(128)
            self.ui.slider.setTickPosition( self.ui.slider.TicksBelow)
        
    def funcao8(self):                                                         # ToHighPass Precisa ajeitar coloquei o toNormal
        
        if(self.toUsandoFiltro):
            
            if(self.do_i_edited_an_image == True):
                
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toClarendon("./images/PhotoInEdition/edited.jpg")))
            
            else:
                self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toClarendon(IMAGE_TAKED)))

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
            
            
            self.ui.slider.setMaximum(255)

            self.primeiraIteracao = 0
            valor = self.sliderValues[7]
            self.ui.slider.setValue(valor)
            self.ui.slider.setTickInterval(128)
            self.ui.slider.setTickPosition( self.ui.slider.TicksBelow)

    def sliderChange(self):                                                    # Slider on Changed
        
        print(self.primeiraIteracao)
        
        if(self.primeiraIteracao == 0):
            
            self.img_dir = "./images/FuncaoDeEdicao/" # Enter Directory of all images         
            self.length = len([name for name in os.listdir(self.img_dir) ])
            
            if(self.length > 0):
                self.imagePath = "./images/FuncaoDeEdicao/edited"+"{}".format(self.length-1) + "{}".format(".jpg")
            else:
                self.imagePath = "./images/FuncaoDeEdicao/edited"+"{}".format(self.length) + "{}".format(".jpg")

            self.primeiraIteracao = 1
            
        else:

            if(self.queFuncaoEdicao == 0 and self.primeiraIteracao == 1):  #Brilho
                            
                if( self.length > 0 ):
                    self.ui.imagemCentral.setPixmap(QtGui.QPixmap(brilho(self.imagePath, self.ui.slider.value(), self.length )))
        
                else:
                    if(self.do_i_filtered_an_image == True):
                        
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(brilho(IMAGE_FILTERED, self.ui.slider.value(), self.length)))
                    else:
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(brilho(IMAGE_TAKED, self.ui.slider.value(), self.length)))
                
                self.sliderValues[0] = self.ui.slider.value()
                
            elif(self.queFuncaoEdicao == 1 and self.primeiraIteracao == 1): #Saturação

                if(self.length > 0):
                
                    self.ui.imagemCentral.setPixmap(QtGui.QPixmap(saturaration(self.imagePath, self.ui.slider.value(), self.length )))

                else:
                    if(self.do_i_filtered_an_image == True):
                        
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(saturaration(IMAGE_FILTERED, self.ui.slider.value(), self.length)))
                    
                    else:
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(saturaration(IMAGE_TAKED, self.ui.slider.value(), self.length )))

                self.sliderValues[1] = self.ui.slider.value()
                        
            elif(self.queFuncaoEdicao == 2 and self.primeiraIteracao == 1): #Rotação
                    
                if( self.length > 0):
                    
                    self.ui.imagemCentral.setPixmap(QtGui.QPixmap(rotacionar(self.imagePath, self.ui.slider.value(),self.length )))

                else:
                    
                    if(self.do_i_filtered_an_image == True):
                        
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(rotacionar(IMAGE_FILTERED, self.ui.slider.value(), self.length)))
                    else:
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(rotacionar(IMAGE_TAKED, self.ui.slider.value(), self.length)))

                self.sliderValues[2] =  self.ui.slider.value()   


            elif(self.queFuncaoEdicao == 3 and self.primeiraIteracao == 1): #Temperatura
                    
                if( self.length > 0):
                    
                    self.ui.imagemCentral.setPixmap(QtGui.QPixmap(warmth(self.imagePath, self.ui.slider.value(),self.length )))

                else:
                    
                    if(self.do_i_filtered_an_image == True):
                        
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(warmth(IMAGE_FILTERED, self.ui.slider.value(), self.length)))
                    else:
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(warmth(IMAGE_TAKED, self.ui.slider.value(),self.length )))

                self.sliderValues[3] = self.ui.slider.value()    

            elif(self.queFuncaoEdicao == 4 and self.primeiraIteracao == 1) : #Contraste
                    
                if( self.length > 0):
                    
                    self.ui.imagemCentral.setPixmap(QtGui.QPixmap(contraste(self.imagePath, self.ui.slider.value(),self.length )))

                else:
                    
                    if(self.do_i_filtered_an_image == True):
                        
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(contraste(IMAGE_FILTERED, self.ui.slider.value(), self.length)))
                    else:
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(contraste(IMAGE_TAKED, self.ui.slider.value(),self.length )))

                self.sliderValues[4] = self.ui.slider.value()    
            
            elif(self.queFuncaoEdicao == 5 and self.primeiraIteracao == 1): # Escolha seu Oculos


                if( self.length > 0):
                    
                    self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toPutGlasses(self.imagePath, self.ui.slider.value(),self.length )))

                else:
                    if(self.do_i_filtered_an_image == True):
                        
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toPutGlasses(IMAGE_FILTERED, self.ui.slider.value(), self.length)))
                    else:
                        self.ui.imagemCentral.setPixmap(QtGui.QPixmap(toPutGlasses(IMAGE_TAKED, self.ui.slider.value(),self.length )))

                self.sliderValues[5] = self.ui.slider.value()    

            elif(self.queFuncaoEdicao == 6): #Iluminação

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

    