import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_MainWin import Ui_MainWindow


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

    def show(self):
        self.main_win.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

    """
            self.pushButton.clicked.connect(self.show_image)
            self.pushButton_2.clicked.connect(self.show_segmentada)

            img = segmentar('digital.jpg')
            print("Imagem",img)
            self.image_right.setPixmap(QtGui.QPixmap(img))
            """