# import system module
import sys

from PyQt5 import QtWidgets
from telas.TelaEdicao import TelaEdicao
from telas.TelaFoto import TelaFoto
# import some PyQt5 modules
# import Opencv module
from telas.TelaInicial import TelaInicial

IMAGE_NAME = "./edited.jpg"

class Controller:

    def __init__(self):
        self.edicao = None
        self.inicial = None
        self.tirar_foto = None

    def show_inicial(self):
        self.inicial = TelaInicial()
       
        if (self.edicao != None and self.edicao.isVisible() ):
            self.edicao.close()

        if(self.tirar_foto != None and self.tirar_foto.isVisible() ):
            self.tirar_foto.close()

        self.inicial.switch_window.connect(self.show_tirar_foto)
        self.inicial.sair.connect(self.exit)
        self.inicial.show()

    def show_tirar_foto(self):

        self.tirar_foto = TelaFoto()
        
        if(self.inicial.isVisible() ):
            self.inicial.close()
        
        if( self.edicao != None and self.edicao.isVisible() ):
            self.edicao.close()

        self.tirar_foto.switch_window.connect(self.show_edicao)
        self.tirar_foto.voltar.connect(self.show_inicial)
        self.tirar_foto.show()

    def show_edicao(self):
        self.edicao = TelaEdicao()
        self.edicao.voltando.connect(self.show_tirar_foto)
        self.edicao.inicialScreen.connect(self.show_inicial)
        self.tirar_foto.close()
        self.edicao.show()

    def exit(self):
        if (self.inicial != None and self.inicial.isVisible() ):
            self.inicial.close()
            sys.exit()

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_inicial()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()