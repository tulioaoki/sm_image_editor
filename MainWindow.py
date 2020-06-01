"""
In this example, we demonstrate how to create simple camera viewer using Opencv3 and PyQt5
Author: Berrouba.A
Last edited: 21 Feb 2018
"""

# import system module
import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

# import Opencv module
import cv2

from Ui_MainWin import *


class MainWindow(QWidget):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.image=None

        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        self.ui.control_bt.clicked.connect(self.controlTimer)

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
        final = "{}.jpg".format("edited")
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(self.image, 'Nice Lucas', (30, 50), font, 2, (255, 0, 0), 2, cv2.LINE_AA)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        # Imagem src, Img Name, Position(x,y), Fontfamily, FontSize, color, widthFont, Default (deixa como esta)
        cv2.imwrite(final, self.image)
        self.ui.image_label.setPixmap(QtGui.QPixmap(final))

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.ui.control_bt.setText("Stop")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.ui.control_bt.setText("Start")
            self.take_photo()


if __name__ == '__main__':
    print(sys.argv)
    app = QApplication(sys.argv)
    # create and show mainWindow
    mainWindow=MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())