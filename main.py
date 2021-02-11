#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

__author__ = "Kwalix - hallerlucas@outlook.com"
__version__ = "0.1.0"

import sys
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Image localizer")
        self.setWindowIcon(QIcon("img/imageLocalizer-icons.png"))
        self.resize(500, 600)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
