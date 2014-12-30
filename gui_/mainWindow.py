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
        MainWindow.setObjectName("The Harvester Graphical")
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
        self.goAndAbort = QtWidgets.QPushButton(self.centralwidget)
        self.goAndAbort.setObjectName("goAndAbort")
        self.domainContainer.addWidget(self.goAndAbort)
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
        self.resultsBox = QtWidgets.QPlainTextEdit(self.centralwidget)
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
        
        self.goAndAbort.clicked.connect(self.checkInputs)
        self.reset.clicked.connect(self.resetGUI)
        
        #Set all the strings, and connect the slots
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.domainName.setPlaceholderText(_translate("MainWindow", "Domain Name"))
        self.goAndAbort.setText(_translate("MainWindow", "Go!"))
        self.dataSource.setItemText(0, _translate("MainWindow", "Data Source"))
        self.dataSource.setItemText(1, _translate("MainWindow", "All"))
        self.dataSource.setItemText(2, _translate("MainWindow", "Google"))
        self.dataSource.setItemText(3, _translate("MainWindow", "GoogleCSE"))
        self.dataSource.setItemText(4, _translate("MainWindow", "GooglePlus"))
        self.dataSource.setItemText(5, _translate("MainWindow", "Google-Profiles"))
        self.dataSource.setItemText(6, _translate("MainWindow", "Bing"))
        self.dataSource.setItemText(7, _translate("MainWindow", "BingAPI"))
        self.dataSource.setItemText(8, _translate("MainWindow", "PGP"))
        self.dataSource.setItemText(9, _translate("MainWindow", "LinkedIn"))
        self.dataSource.setItemText(10, _translate("MainWindow", "People123"))
        self.dataSource.setItemText(11, _translate("MainWindow", "Jigsaw"))
        self.dataSource.setItemText(12, _translate("MainWindow", "Twitter"))
        self.queryShodan.setText(_translate("MainWindow", "Query hosts with Shodan"))
        self.limitResultsLabel.setText(_translate("MainWindow", "Limit Results"))
        self.limitResults.setText(_translate("MainWindow", "500"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.statusbar.showMessage(_translate("MainWindow", "Ready to go!"))
        
    
    def checkInputs(self):
        verification = verify_parameters.verify(self.domainName.text(), self.dataSource.currentText(), str(self.queryShodan.isChecked()), self.limitResults.text())
        
        if verification == True:
            print("We're all set")
        else:
            self.resultsBox.setPlainText(verification)
        
    def resetGUI(self):
        self.resultsBox.setPlainText("")
        self.domainName.setText("")
        self.limitResults.setText("")
        self.dataSource.setCurrentIndex(0)
        self.queryShodan.setChecked(False)