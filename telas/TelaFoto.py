import cv2
import os
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer
# import some PyQt5 modules
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap

from forms.TirarFotoForm import Ui_Form
from PyQt5 import QtCore, QtWidgets

class TelaFoto(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    voltar = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.image = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Tire sua foto')

        #layout = QtWidgets.QGridLayout()

        self.button = QtWidgets.QPushButton('Login')
        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        self.controlTimer()
        self.ui.control_bt.clicked.connect(self.controlTimer)
        self.ui.editar.clicked.connect(self.editar)

        self.ui.voltar.clicked.connect(self.telaInicial)

    def telaInicial(self):
        self.timer.stop()
        # release video capture
        self.cap.release()
        self.voltar.emit()

    def editar(self):
        self.switch_window.emit()

        # view camera
    def viewCam(self):
        # read image in BGR format
        ret, self.image = self.cap.read()
        # convert image to RGB format
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = self.image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(self.image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))

    def take_photo(self):
        
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #cv2.putText(self.image, 'Nice Lucas', (30, 50), font, 2, (255, 0, 0), 2, cv2.LINE_AA)
        # Imagem src, Img Name, Position(x,y), Fontfamily, FontSize, color, widthFont, Default (deixa como esta)
        
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        cv2.imwrite( "./images/PhotoInEdition/edited.jpg", self.image)
        cv2.imwrite("./images/PhotoInEdition/fotoTirada.jpg", self.image)
        self.ui.image_label.setPixmap(QtGui.QPixmap("./images/PhotoInEdition/fotoTirada.jpg"))
        self.ui.editar.setEnabled(True)
        # start/stop timer

    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.ui.control_bt.setText("TIRAR FOTO")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.ui.control_bt.setText("TIRAR OUTRA FOTO")
            self.take_photo()