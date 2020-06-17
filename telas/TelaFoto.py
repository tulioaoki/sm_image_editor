import cv2
import os
import numpy as np
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

    pararDeDesenhar = False

    imgResult = None

    myColors = [[149, 157, 0, 179, 255, 255],   # [Rosa Marca-Texto]
                    [30, 120, 90, 80, 255, 255],    # [Verde Marca-Texto]
                    ]     # [Azul Bebe]

                        ## BGR
    myColorValues = [[255,0,255],       # [Rosa]
                        [0,255,0],         # [Verde]
                        [242,208,128]]      # [Azul Bebe]   
                        #[255,0,0]] 
    myPoints =  []  ## [x , y , colorId ]
    



    def __init__(self):
        super().__init__()
        self.image = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('Tire sua foto')
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
        self.ui.desenhar.clicked.connect(self.desenhar)

    
    def telaInicial(self):
        self.timer.stop()
        # release video capture
        self.cap.release()
        self.voltar.emit()

    def editar(self):
        self.switch_window.emit()

        # view camera
    def viewCam(self):

        ret, self.image = self.cap.read()
        self.image = cv2.flip(self.image, 1)

        if(self.pararDeDesenhar == True):
            
            newPoints = self.findColor(self.image, self.myColors, self.myColorValues)
            if len(newPoints)!=0:
                for newP in newPoints:
                    self.myPoints.append(newP)
            if len(self.myPoints)!=0:
                self.drawOnCanvas(self.myPoints,self.myColorValues)

        # read image in BGR format
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
        
        del self.myPoints [:] # Deletar os pontos que eu desenhei
        self.ui.desenhar.setEnabled(False)
            
        self.pararDeDesenhar == False
        _translate = QtCore.QCoreApplication.translate
        self.ui.desenhar.setText(_translate("Form", "DESENHAR: DESLIGADO"))
       
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        cv2.imwrite("./images/PhotoInEdition/fotoTirada.jpg", self.image)
        self.ui.image_label.setPixmap(QtGui.QPixmap("./images/PhotoInEdition/fotoTirada.jpg"))
        self.ui.editar.setEnabled(True)

    def controlTimer(self):
        # if timer is stopped
        
        if not self.timer.isActive():
            # create video capture
            self.ui.desenhar.setEnabled(True)
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
            _translate = QtCore.QCoreApplication.translate
            self.ui.desenhar.setText(_translate("Form", "DESENHAR: LIGADO"))
            self.take_photo()

    def desenhar(self):
    
        if(self.pararDeDesenhar == False):
            self.pararDeDesenhar = True
            _translate = QtCore.QCoreApplication.translate
            self.ui.desenhar.setText(_translate("Form", "DESENHAR: LIGADO"))
        else:
            self.pararDeDesenhar = False
            _translate = QtCore.QCoreApplication.translate
            self.ui.desenhar.setText(_translate("Form", "DESENHAR: DESLIGADO"))
            del self.myPoints [:]  # Deletar todos os pontos que desenhei
            

    def findColor(self,img,myColors,myColorValues):


        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        count = 0
        newPoints=[]
        for color in myColors:
            lower = np.array(color[0:3])
            upper = np.array(color[3:6])
            mask = cv2.inRange(imgHSV,lower,upper)
            x,y= self.getContours(mask)
            cv2.circle(self.image,(x,y),15,myColorValues[count],cv2.FILLED)
            if x!=0 and y!=0:
                newPoints.append([x,y,count])
            count +=1
        return newPoints
 
    def getContours(self,img):
        contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        x,y,w,h = 0,0,0,0
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area>500:
                peri = cv2.arcLength(cnt,True)
                approx = cv2.approxPolyDP(cnt,0.02*peri,True)
                x, y, w, h = cv2.boundingRect(approx)
        
        return x+w//2,y
 
    def drawOnCanvas(self,myPoints,myColorValues):
        for point in myPoints:
            cv2.circle(self.image, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)
 