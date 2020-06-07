# import system module
import sys

from PyQt5 import QtWidgets
from telas.TelaEdicao import TelaEdicao
from telas.TelaFoto import TelaFoto
# import some PyQt5 modules
# import Opencv module
from telas.TelaInicial import TelaInicial

IMAGE_NAME = "../edited.jpg"

class Controller:

    def __init__(self):
        self.edicao = None
        self.inicial = None
        self.tirar_foto = None

    def show_inicial(self):
        self.inicial = TelaInicial()
        self.inicial.switch_window.connect(self.show_tirar_foto)
        if self.edicao and self.edicao.isEnabled():
            self.edicao.close()
        self.inicial.show()

    def show_tirar_foto(self):
        self.tirar_foto = TelaFoto()
        self.tirar_foto.switch_window.connect(self.show_edicao)
        self.inicial.close()
        self.tirar_foto.show()

    def show_edicao(self):
        self.edicao = TelaEdicao()
        self.edicao.switch_window.connect(self.show_inicial)
        self.tirar_foto.close()
        self.edicao.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_inicial()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()