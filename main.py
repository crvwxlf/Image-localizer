#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

__author__ = "Kwalix"
__version__ = "1.0.0"

import sys
import webbrowser
from GPSPhoto import gpsphoto
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Image localizer")
        self.setWindowIcon(QIcon("img/imageLocalizer-icons.png"))
        self.setFixedSize(500, 600)

        self.bg_image = QImage('img/background.jpg')
        self.img_size = self.bg_image.scaled(QSize(500,600))

        self.palette = QPalette()
        self.palette.setBrush(QPalette.ColorRole(10), QBrush(self.bg_image))
        self.setPalette(self.palette)

        self.title = QLabel(self)
        self.title.setGeometry(100, 20, 300, 150)
        self.titlePixmap = QPixmap("img/titleImage.png")
        self.title.setPixmap(self.titlePixmap)

        self.selectFileBtn = QPushButton("Select image", self)
        self.selectFileBtn.setGeometry(100, 470, 140, 51)

        self.viewOnMapBtn = QPushButton("View on map", self)
        self.viewOnMapBtn.setGeometry(261, 470, 140, 51)
        self.viewOnMapBtn.setEnabled(False)

        self.filePathLb = QLabel(self)
        self.filePathLb.setText("Image path :")
        self.filePathLb.setGeometry(100, 227, 101, 21)
        self.filePathLb.setFont("Segoe UI Black")
        self.filePathLb.setStyleSheet("font-size: 15px;"
                                      "color: white;")

        self.logBoxLb = QLabel(self)
        self.logBoxLb.setText("Logs :")
        self.logBoxLb.setGeometry(100, 290, 101, 21)
        self.logBoxLb.setFont("Segoe UI Black")
        self.logBoxLb.setStyleSheet("font-size: 15px;"
                                      "color: white;")

        self.selectFileBtn.clicked.connect(self.selectFile)
        self.viewOnMapBtn.clicked.connect(self.openBrowserMap)


        self.pathInputLabel = QLabel(self)
        self.pathInputLabel.text = "Path of image :"
        self.pathInputLabel.setGeometry(100, 195, 150, 30)

        self.pathInput = QLineEdit(self)
        self.pathInput.setGeometry(100, 250, 300, 20)
        self.pathInput.setReadOnly(True)

        self.logBox = QPlainTextEdit(self)
        self.logBox.setGeometry(100, 315, 300, 111)
        self.logBox.setReadOnly(True)

        self.lat = ""
        self.long = ""

    def selectFile(self):
        path_to_file, _ = QFileDialog.getOpenFileName(self, self.tr("Load Image"), filter=self.tr("Images (*.jpg)"))

        if self.logBox and self.pathInput != '':
            self.pathInput.setText("")
            self.logBox.setPlainText("")
        self.pathInput.insert(path_to_file)
        self.logBox.insertPlainText("File selected : {0}".format(path_to_file) + "\n")
        self.logBox.insertPlainText("Trying to extract data from image file..." + "\n")
        imgData = gpsphoto.getGPSData(path_to_file)
        try:
            self.lat = imgData.get('Latitude')
            self.long = imgData.get('Longitude')
            if self.lat and self.long != None or self.lat and self.long != '':
                self.logBox.insertPlainText(f"GPS data found : \nLatitude : {self.lat}\nLongitude : {self.long}" + "\n")
                self.viewOnMapBtn.setEnabled = True
            elif self.lat and self.long == '':
                self.viewOnMapBtn.setEnabled = False
                self.logBox.insertPlainText(f"GPS data not found\nSelect other image :/" + "\n")

        except Exception:
            self.logBox.insertPlainText(f"GPS data not found\nSelect other image :/" + "\n")

        print(imgData)

    def openBrowserMap(self):
        url = f'https://www.google.com/maps/search/{self.lat}+{self.long}'
        webbrowser.open(url)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
