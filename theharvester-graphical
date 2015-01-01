#!/usr/bin/python

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from gui_ import *


#Start the gui
if __name__ == "__main__":
    ui = mainWindow.Ui_MainWindow()
  
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)
    
    qr = MainWindow.frameGeometry()
    cp = QtWidgets.QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    MainWindow.move(qr.topLeft())
    
    MainWindow.show()
    app.exec_()

