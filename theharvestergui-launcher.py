import sys
from PyQt4 import QtCore, QtGui

from gui_ import *


#Start the gui
if __name__ == "__main__":
    ui = mainWindow.Ui_MainWindow()
  
    app = QtGui.QApplication(sys.argv)
    
    MainWindow = QtGui.QMainWindow()
    ui.setupUi(MainWindow)
    
    qr = MainWindow.frameGeometry()
    cp = QtGui.QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    MainWindow.move(qr.topLeft())
    
    MainWindow.show()
    app.exec_()

