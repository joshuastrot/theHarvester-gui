#!/usr/bin/python
# -*- coding: utf-8 -*-

#Import needed libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from tools_ import *


#Start the main class
class Ui_MainWindow(QtCore.QObject):
    #Function to set up the GUI
    def setupUi(self, MainWindow):
        
        #Set window name and size. Should be full resizable.
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("The Harvester GUI")
        MainWindow.resize(800, 502)
        
        #Set up the Central Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.centralWidgetContainer = QtWidgets.QVBoxLayout(self.centralwidget)
        self.centralWidgetContainer.setObjectName("centralWidgetContainer")
        
        #Set up main layout
        self.mainContainer = QtWidgets.QVBoxLayout()
        self.mainContainer.setObjectName("mainContainer")
        self.centralWidgetContainer.addLayout(self.mainContainer)
        
        #Set up the Domain and Submit Bar
        self.domainContainer = QtWidgets.QHBoxLayout()
        self.domainContainer.setObjectName("domainContainer")
        self.domainName = QtWidgets.QLineEdit(self.centralwidget)
        self.domainName.setObjectName("domainName")
        self.domainContainer.addWidget(self.domainName)
        self.goButton = QtWidgets.QPushButton(self.centralwidget)
        self.goButton.setObjectName("goButton")
        self.domainContainer.addWidget(self.goButton)
        self.abortButton = QtWidgets.QPushButton(self.centralwidget)
        self.abortButton.setObjectName("abortButton")
        self.abortButton.setEnabled(False)
        self.domainContainer.addWidget(self.abortButton)
        self.mainContainer.addLayout(self.domainContainer)
        
        #Set up the Data Source bar
        self.dataSourceContainer = QtWidgets.QHBoxLayout()
        self.dataSourceContainer.setObjectName("dataSourceContainer")
        self.dataSource = QtWidgets.QComboBox(self.centralwidget)
        self.dataSource.setObjectName("dataSource")
        dataSizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        dataSizePolicy.setHorizontalStretch(0)
        dataSizePolicy.setVerticalStretch(0)
        dataSizePolicy.setHeightForWidth(self.dataSource.sizePolicy().hasHeightForWidth())
        self.dataSource.setSizePolicy(dataSizePolicy)
        self.dataSource.addItem("") #Leave these blank so they can be added in the translate function
        self.dataSource.addItem("") 
        self.dataSource.addItem("")
        self.dataSource.addItem("")
        self.dataSource.addItem("")
        self.dataSource.addItem("")
        self.dataSource.addItem("")
        self.dataSource.addItem("")
        self.dataSource.addItem("")
        self.dataSource.addItem("")
        self.dataSource.addItem("")
        self.dataSource.addItem("")
        self.dataSource.addItem("")
        self.dataSourceContainer.addWidget(self.dataSource)
        self.queryShodan = QtWidgets.QCheckBox(self.centralwidget)
        self.queryShodan.setObjectName("queryShodan")
        self.dataSourceContainer.addWidget(self.queryShodan)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.dataSourceContainer.addItem(spacerItem)
        self.mainContainer.addLayout(self.dataSourceContainer)
        
        #Set up the Limit Results bar
        self.limitResultsContainer = QtWidgets.QHBoxLayout()
        self.limitResultsContainer.setObjectName("limitResultsContainer")
        self.limitResultsLabel = QtWidgets.QLabel(self.centralwidget)
        self.limitResultsLabel.setObjectName("limitResultsLabel")
        self.limitResultsContainer.addWidget(self.limitResultsLabel)
        self.limitResults = QtWidgets.QLineEdit(self.centralwidget)
        self.limitResults.setObjectName("limitResults")
        limitResultsSizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        limitResultsSizePolicy.setHorizontalStretch(0)
        limitResultsSizePolicy.setVerticalStretch(0)
        limitResultsSizePolicy.setHeightForWidth(self.limitResults.sizePolicy().hasHeightForWidth())
        self.limitResults.setSizePolicy(limitResultsSizePolicy)
        self.limitResults.setMinimumSize(QtCore.QSize(0, 0))
        self.limitResultsContainer.addWidget(self.limitResults)
        limitResultsSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.limitResultsContainer.addItem(limitResultsSpacer)
        self.mainContainer.addLayout(self.limitResultsContainer)
        
        #Set up the Results Box
        self.resultsBox = QtWidgets.QTextEdit(self.centralwidget)
        self.resultsBox.setReadOnly(True)
        self.resultsBox.setObjectName("resultsBox")
        self.mainContainer.addWidget(self.resultsBox)
        resultsSpacer = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.mainContainer.addItem(resultsSpacer)
        
        #Set up Reset bar
        self.resetContainer = QtWidgets.QHBoxLayout()
        self.resetContainer.setObjectName("resetContainer")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setObjectName("reset")
        self.resetContainer.addWidget(self.reset)
        resetSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.resetContainer.addItem(resetSpacer)
        self.mainContainer.addLayout(self.resetContainer)
        
        #Set up Status Bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.goButton.clicked.connect(self.checkInputs)
        self.abortButton.clicked.connect(self.abort)
        self.reset.clicked.connect(self.resetGUI)
        
        #Set all the strings, and connect the slots
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
    def retranslateUi(self, MainWindow):
        global _translate 
        _translate = QtCore.QCoreApplication.translate
        self.domainName.setPlaceholderText(_translate("MainWindow", "Domain Name"))
        self.goButton.setText(_translate("MainWindow", "Go"))
        self.abortButton.setText(_translate("MainWindow", "Abort"))
        self.dataSource.setItemText(0, _translate("MainWindow", "Data Source"))
        self.dataSource.setItemText(1, _translate("MainWindow", "all"))
        self.dataSource.setItemText(2, _translate("MainWindow", "google"))
        self.dataSource.setItemText(3, _translate("MainWindow", "googleCSE"))
        self.dataSource.setItemText(4, _translate("MainWindow", "googleplus"))
        self.dataSource.setItemText(5, _translate("MainWindow", "google-profiles"))
        self.dataSource.setItemText(6, _translate("MainWindow", "bing"))
        self.dataSource.setItemText(7, _translate("MainWindow", "bingapi"))
        self.dataSource.setItemText(8, _translate("MainWindow", "pgp"))
        self.dataSource.setItemText(9, _translate("MainWindow", "linkedin"))
        self.dataSource.setItemText(10, _translate("MainWindow", "people123"))
        self.dataSource.setItemText(11, _translate("MainWindow", "jigsaw"))
        self.dataSource.setItemText(12, _translate("MainWindow", "twitter"))
        self.queryShodan.setText(_translate("MainWindow", "Query hosts with Shodan"))
        self.limitResultsLabel.setText(_translate("MainWindow", "Limit Results"))
        self.limitResults.setText(_translate("MainWindow", "500"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.statusbar.showMessage(_translate("MainWindow", "Ready to go!"))
        
    def parseData(self, data):
        data = str(data)
        
        data = data.replace("\n", "<br>")
        data = data.replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;")
        data = data.replace("<strong>", "")
        data = data.replace("<<", "<")
        
        if ( data.startswith('b"') and data.endswith('"') ) or ( data.startswith("b'") and data.endswith("'") ):
            data = data[2:-1]
        
        if data.endswith("<"):
            data = data[0:-1]
            
        if data.startswith("<br>*"):
            if data.endswith("<br><br><br>"):
                return None
            else:
                data = data.split("<br><br><br>")[1]
            
        return data
        
    def dataReady(self):
        cursor = self.resultsBox.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertHtml(self.parseData(self.process.readAll()))
        self.resultsBox.ensureCursorVisible()
    
    def finished(self):
        self.statusbar.showMessage(_translate("MainWindow", "Finished"))
        self.abortButton.setEnabled(False)
        self.goButton.setEnabled(True)
        
    def checkInputs(self):
        parametersList = [self.domainName.text(), self.dataSource.currentText(), str(self.queryShodan.isChecked()), self.limitResults.text()]
        verification = verify_parameters.verify(parametersList[0], parametersList[1], parametersList[2], parametersList[3])
        
        if verification == True:
            self.statusbar.showMessage(_translate("MainWindow", "Running"))
            self.resultsBox.setPlainText("")
            self.goButton.setEnabled(False)
            self.abortButton.setEnabled(True)
            
            self.process = QtCore.QProcess(self)
            self.process.setProcessChannelMode(QtCore.QProcess.MergedChannels)
            self.process.readyReadStandardOutput.connect(self.dataReady)
            self.process.finished.connect(self.finished)
            
            self.process.start("python2", ["-u", "/opt/theharvester-git/theHarvester.py", "-d", self.domainName.text(), "-l", self.limitResults.text(), "-b", self.dataSource.currentText(), "-h" if self.queryShodan.isChecked() else ""])
        else:
            self.resultsBox.setPlainText(verification)
            
    def abort(self):
        if self.process.pid() > 0:
            self.process.close()
            
        self.statusbar.showMessage(_translate("MainWindow", "Aborted"))
        self.abortButton.setEnabled(False)
        self.goButton.setEnabled(True)
        
    def resetGUI(self):
        self.abort()
        self.resultsBox.setPlainText("")
        self.domainName.setText("")
        self.limitResults.setText("500")
        self.dataSource.setCurrentIndex(0)
        self.queryShodan.setChecked(False)
        self.statusbar.showMessage(_translate("MainWindow", "Ready to go!"))
        self.abortButton.setEnabled(False)
        self.goButton.setEnabled(True)
        
