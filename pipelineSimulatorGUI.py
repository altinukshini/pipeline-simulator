#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CPU Pipeline algorithm GUI simulator.
This script simulates the CPU pipeline algorithm of a emu 8086 processor.
"""
__author__ = "Altin Ukshini"
__copyright__ = "Copyright (c) 2018, Altin Ukshini"

__license__ = "GPL v3.0"
__version__ = "1.0"
__maintainer__ = "Altin Ukshini"
__email__ = "altin.ukshini@gmail.com"
__status__ = "Development"

import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HelpDialog(object):
    def setupUi(self, HelpDialog):
        HelpDialog.setObjectName("HelpDialog")
        HelpDialog.resize(640, 437)
        self.helpContent = QtWidgets.QTextBrowser(HelpDialog)
        self.helpContent.setGeometry(QtCore.QRect(10, 10, 621, 381))
        self.helpContent.setObjectName("helpContent")
        self.okButton = QtWidgets.QPushButton(HelpDialog)
        self.okButton.setGeometry(QtCore.QRect(540, 400, 92, 30))
        self.okButton.setObjectName("okButton")
        self.actionOK = QtWidgets.QAction(HelpDialog)
        self.actionOK.setObjectName("actionOK")
        self.okButton.clicked.connect(HelpDialog.accept)

        self.retranslateUi(HelpDialog)
        QtCore.QMetaObject.connectSlotsByName(HelpDialog)

    def retranslateUi(self, HelpDialog):
        _translate = QtCore.QCoreApplication.translate
        HelpDialog.setWindowTitle(_translate("HelpDialog", "Dialog"))
        self.helpContent.setHtml(_translate("HelpDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n" "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n" "p, li { white-space: pre-wrap; }\n" "</style></head><body style=\" font-family:\'Open Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n" "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">The simulator takes four main arguments:</span></p>\n""<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- <span style=\" font-weight:600;\">Operand Stage:</span> Stage in which the operand is read (e.g., stage 1 (DI) out of cycles 0-5)</p>\n""<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- <span style=\" font-weight:600;\">Result Stage:</span> Stage in which results are available (e.g., stage 5 (WO) out of cycles 0-5)</p>\n""<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- <span style=\" font-weight:600;\">Instruction start:</span> The starting instruction for the execution chart.</p>\n""<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- <span style=\" font-weight:600;\">Instruction end:</span> The ending instruction for the execution chart (0 or &lt; starting instruction means no execution chart)</p>\n""<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n""<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Other arguments:</span></p>\n""<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- <span style=\" font-weight:600;\">Pipeline:</span> Pipeline stages/cycles depth. Has to be greater than 3 stages (exc: FI, DI, EI), or default FI,DI,CO,FO,EI,WO. Stages have to be comma separated.  </p>\n""<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- <span style=\" font-weight:600;\">Register size:</span> Number of registers </p>\n""<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n""<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Trace:</span></p>\n""<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Each line of trace contains three integers, representing the registers for operand 1, operand 2, and the result. A -1 in any of these positions means that the instruction doesn\'t use that operand, or doesn\'t produce a result. Operands or results must not be lower than -1 or greater than (register size - 1)</p>\n""<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n""<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Output:</span></p>\n""<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The main output will generate a graph and also provide some analysis, while the second output will provide the register status during execution.<br/></p>\n""<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Example of MIPS pipeline (5 stages):</span></p>\n""<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Change the result stage to \"4\" and Pipeline to \"IF,ID,EX,ME,WB\"</p>\n""<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.okButton.setText(_translate("HelpDialog", "OK"))
        self.actionOK.setText(_translate("HelpDialog", "OK"))
        self.actionOK.setToolTip(_translate("HelpDialog", "OK"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 569)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 99, 221, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.traceText = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.traceText.setObjectName("traceText")
        self.verticalLayout.addWidget(self.traceText)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(490, 90, 351, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.registernumbers = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.registernumbers.setMinimum(46)
        self.registernumbers.setMaximum(1000)
        self.registernumbers.setObjectName("registernumbers")
        self.gridLayout.addWidget(self.registernumbers, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 1, 1, 1)
        self.pipelineStages = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.pipelineStages.setObjectName("pipelineStages")
        self.gridLayout.addWidget(self.pipelineStages, 1, 0, 1, 1)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 831, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.operandstage = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.operandstage.setMaximum(5)
        self.operandstage.setProperty("value", 1)
        self.operandstage.setObjectName("operandstage")
        self.horizontalLayout.addWidget(self.operandstage)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.resultstage = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.resultstage.setMaximum(5)
        self.resultstage.setProperty("value", 5)
        self.resultstage.setObjectName("resultstage")
        self.horizontalLayout.addWidget(self.resultstage)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.startat = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.startat.setMaximum(1000)
        self.startat.setProperty("value", 1)
        self.startat.setObjectName("startat")
        self.horizontalLayout.addWidget(self.startat)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.endat = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.endat.setMaximum(1000)
        self.endat.setProperty("value", 10)
        self.endat.setObjectName("endat")
        self.horizontalLayout.addWidget(self.endat)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(7, 510, 831, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.simulateButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.simulateButton.setObjectName("simulateButton")
        self.horizontalLayout_2.addWidget(self.simulateButton)
        self.loadTrace = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.loadTrace.setObjectName("loadTrace")
        self.horizontalLayout_2.addWidget(self.loadTrace)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.helpButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.helpButton.setObjectName("helpButton")
        self.horizontalLayout_2.addWidget(self.helpButton)
        self.quitButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.quitButton.setFlat(False)
        self.quitButton.setObjectName("quitButton")
        self.horizontalLayout_2.addWidget(self.quitButton)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(240, 140, 601, 251))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.textOutput = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.textOutput.setFont(font)
        self.textOutput.setObjectName("textOutput")
        self.textOutput.ensureCursorVisible()
        self.verticalLayout_3.addWidget(self.textOutput)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(1060, 140, 160, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(240, 410, 601, 91))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textOutput2 = QtWidgets.QTextBrowser(self.verticalLayoutWidget_4)
        self.textOutput2.setObjectName("textOutput2")
        self.verticalLayout_4.addWidget(self.textOutput2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSimulate = QtWidgets.QAction(MainWindow)
        self.actionSimulate.setObjectName("actionSimulate")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.helpButton.clicked.connect(self.openHelp)
        self.simulateButton.clicked.connect(self.simulateCPUPipeline)
        self.quitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.actionLoadTrace = QtWidgets.QAction(MainWindow)
        self.actionLoadTrace.setObjectName("actionLoadTrace")
        self.loadTrace.clicked.connect(self.loadTraceLines)

        MainWindow.setCentralWidget(self.centralwidget)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSimulate = QtWidgets.QAction(MainWindow)
        self.actionSimulate.setObjectName("actionSimulate")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def openHelp(self):
        HelpDialog = QtWidgets.QDialog()
        ui2 = Ui_HelpDialog()
        ui2.setupUi(HelpDialog)
        HelpDialog.exec_()

    def loadTraceLines(self):
        self.traceText.setProperty("plainText", "-1 -1 13\n" "-1 -1 13\n""-1 5 45\n""45 3 44\n""-1 5 3\n""-1 -1 0\n""-1 -1 0\n""-1 -1 12\n""13 0 13\n""-1 -1 -1\n""-1 3 0\n""0 0 44\n""-1 -1 -1\n""-1 0 7\n""-1 7 44\n""44 -1 0\n""0 -1 44\n""-1 -1 -1\n""-1 -1 6\n""-1 -1 44\n""4 -1 4\n""44 4 -1\n""-1 -1 -1\n""15 4 -1\n""4 -1 4\n""14 4 -1\n""4 -1 4\n""13 4 -1\n""4 -1 4\n""7 -1 13\n""12 4 -1\n""4 -1 4\n""6 -1 12\n""5 4 -1\n""4 -1 4\n""3 4 -1\n""4 -1 4\n""4 -1 4\n""-1 7 44\n""44 -1 0\n""0 -1 44\n""-1 -1 -1\n""-1 7 5\n""5 -1 44\n""-1 -1 -1\n""-1 -1 45\n""-1 45 45\n""5 45 44\n""-1 -1 -1\n""-1 -1 44\n""-1 44 2\n""2 2 44\n""-1 -1 -1\n""-1 2 12\n""12 -1 12\n""-1 -1 45\n""-1 45 45\n""5 45 44\n""-1 -1 -1\n""-1 -1 44\n""-1 44 2\n""2 2 44\n""-1 -1 -1\n""-1 2 0\n""5 0 44\n""-1 -1 -1\n""-1 -1 45\n""-1 45 45\n""5 45 44\n""-1 -1 -1\n""-1 -1 44\n""-1 44 2\n""2 2 44\n""-1 -1 -1\n""-1 2 45\n""45 -1 44\n""44 2 -1\n""5 -1 44\n""12 -1 12\n""-1 -1 -1\n""-1 13 45\n""45 -1 44\n""-1 13 44\n""44 -1 5\n""-1 -1 -1\n""12 -1 3\n""-1 13 2\n""3 3 44\n""-1 -1 -1\n""-1 3 0\n""-1 0 45\n""45 -1 44\n""-1 -1 -1\n""-1 3 3\n""3 3 44\n""-1 -1 -1\n""4 -1 4\n""-1 4 3\n""4 -1 4\n""-1 4 5\n""4 -1 4\n""-1 4 12\n""4 -1 4\n""-1 4 13\n""4 -1 4\n""-1 4 14\n""4 -1 4\n""-1 4 15\n""4 -1 4\n""-1 4 44\n""4 -1 4\n""44 -1 -1\n""-1 -1 -1\n""12 -1 12\n""3 -1 3\n""-1 5 45\n""12 45 44\n""-1 -1 -1\n""-1 5 0\n""-1 0 45\n""45 -1 44\n""-1 -1 -1\n""-1 0 0\n""-1 0 0\n""0 -1 0\n""0 -1 44\n""-1 -1 -1\n""-1 5 11\n""11 11 44\n""-1 -1 -1\n""-1 5 1\n""-1 5 -1\n""1 5 -1\n""-1 -1 -1\n""-1 5 3\n""-1 3 0\n""0 0 44\n""-1 -1 -1\n""-1 0 7\n""-1 7 45\n""45 -1 44\n""-1 -1 -1\n""-1 7 1\n""1 -1 44\n""-1 -1 -1\n""-1 -1 0\n""-1 -1 -1\n""0 1 0\n""1 0 44\n""-1 -1 -1\n""1 -1 13\n""-1 -1 45\n""-1 45 45\n""45 13 44\n""0 5 -1\n""-1 -1 -1\n""-1 -1 44\n""-1 44 2\n""2 2 44\n""-1 -1 -1\n""-1 2 10\n""10 10 44\n""-1 -1 -1\n""13 -1 13\n""-1 5 45\n""45 13 44\n""-1 -1 -1\n""-1 5 45\n""45 -1 44\n""44 5 -1\n""-1 5 45\n""45 -1 44\n""44 5 -1\n""-1 5 0\n""-1 5 45\n""45 0 44\n""-1 -1 -1\n""-1 5 1\n""-1 -1 6\n""-1 -1 -1\n""-1 -1 -1\n""-1 1 45\n""45 -1 44\n""-1 -1 -1\n""-1 1 0\n""0 0 44\n""-1 -1 -1\n""-1 0 45\n""45 -1 44\n""-1 -1 -1\n""6 -1 6\n""1 -1 1\n""-1 5 45\n""6 45 44\n""-1 -1 -1\n""-1 5 1\n""-1 5 -1\n""1 5 -1\n""-1 -1 -1\n""-1 5 2\n""-1 2 0\n""0 0 44\n""-1 -1 -1\n""-1 -1 44\n""-1 44 9\n""-1 0 12\n""-1 2 14\n""9 9 44\n""-1 -1 -1\n""-1 12 44\n""44 -1 2\n""2 -1 44\n""-1 -1 -1\n""-1 5 45\n""45 -1 44\n""-1 -1 -1\n""-1 5 1\n""-1 1 6\n""6 6 44\n""-1 -1 -1\n""-1 -1 -1\n""-1 12 44\n""44 -1 0\n""0 -1 44\n""-1 -1 -1\n""0 -1 44\n""-1 -1 -1\n""0 -1 44\n""-1 -1 -1\n""-1 -1 2\n""12 -1 7\n""-1 -1 44\n""4 -1 4\n""44 4 -1\n""-1 -1 -1\n""14 4 -1\n""4 -1 4\n""2 -1 14\n""13 4 -1\n""4 -1 4\n""6 -1 13\n""12 4 -1\n""4 -1 4\n""5 4 -1\n""4 -1 4\n""7 -1 5\n""3 4 -1\n""4 -1 4\n""-1 7 44\n""44 -1 0\n""0 -1 44\n""-1 -1 -1\n""-1 7 3\n""-1 -1 45\n""-1 45 45\n""3 45 44\n""-1 -1 -1\n""-1 -1 44\n""-1 44 2\n""2 2 44\n""-1 -1 -1\n""-1 2 45\n""45 3 44\n""-1 -1 -1\n""13 13 44\n""-1 -1 -1\n""-1 13 1\n""1 1 44\n""-1 -1 -1\n""-1 1 2\n""-1 2 45\n""45 -1 44\n""-1 -1 -1\n""-1 1 1\n""1 1 44\n""-1 -1 -1\n""-1 1 2\n""-1 2 45\n""45 -1 44\n""-1 -1 -1\n""-1 2 44\n""44 -1 0\n""-1 5 45\n""0 45 44\n""-1 -1 -1\n""-1 2 5\n""-1 -1 45\n""-1 45 45\n""5 45 44\n""-1 -1 -1\n""5 -1 0\n""0 -1 0\n""0 5 0\n""0 -1 0\n""0 -1 0\n""-1 0 2\n""-1 0 12\n""2 2 44\n""-1 -1 -1\n""-1 2 45\n""45 5 44\n""-1 -1 -1\n""-1 -1 -1\n""-1 2 12\n""-1 -1 44\n""5 44 -1\n""-1 -1 44\n""2 44 -1\n""12 -1 0\n""0 0 14\n""14 -1 14\n""14 -1 13\n""-1 -1 44\n""-1 44 44\n""13 44 13\n""-1 2 45\n""45 5 44\n""-1 -1 -1\n""-1 -1 45\n""-1 45 45\n""3 45 44\n""-1 -1 -1\n""3 -1 0\n""0 -1 0\n""0 3 0\n""0 -1 0\n""0 -1 0\n""-1 0 2\n""-1 0 5\n""2 2 44\n""-1 -1 -1\n""-1 2 45\n""3 45 44\n""-1 -1 -1\n""-1 -1 44\n""3 44 -1\n""-1 -1 44\n""2 44 -1\n""12 2 -1\n""-1 13 2\n""-1 13 7\n""2 -1 44\n""-1 -1 -1\n""3 -1 44\n""-1 -1 -1\n""2 -1 44\n""2 -1 1\n""3 -1 8\n""-1 -1 -1\n""-1 -1 44\n""-1 44 10\n""-1 -1 44\n""-1 44 6\n""8 10 1\n""-1 1 44\n""44 -1 0\n""0 6 9\n""-1 -1 45\n""-1 45 45\n""9 45 44\n""-1 -1 -1\n""-1 1 44\n""44 -1 0\n""0 6 0\n""-1 -1 45\n""-1 45 45\n""0 45 44\n""-1 -1 -1\n""7 -1 44\n""-1 -1 -1\n""-1 -1 44\n""-1 44 6\n""7 -1 0\n""0 -1 0\n""-1 -1 -1\n""0 6 2\n""8 6 1\n""-1 2 0\n""0 1 -1\n""-1 2 0\n""0 0 44\n""-1 -1 -1\n""-1 -1 44\n""-1 44 0\n""14 0 44\n""3 44 -1\n""-1 -1 -1\n""-1 -1 0\n""3 2 -1\n""7 1 -1\n""-1 -1 -1\n""-1 4 3\n""4 -1 4\n""-1 4 5\n""4 -1 4\n""-1 4 12\n""4 -1 4\n""-1 4 13\n""4 -1 4\n""-1 4 14\n""4 -1 4\n""-1 4 44\n""4 -1 4\n""44 -1 -1\n""0 0 44\n""-1 -1 -1\n""12 -1 7\n""-1 -1 44\n""4 -1 4\n""44 4 -1\n""-1 -1 -1\n""15 4 -1\n""4 -1 4\n""7 -1 15\n""14 4 -1\n""4 -1 4\n""13 4 -1\n""4 -1 4\n""12 4 -1\n""4 -1 4\n""5 4 -1\n""4 -1 4\n""3 4 -1\n""4 -1 4\n""4 -1 4\n""-1 7 45\n""45 -1 44\n""-1 -1 -1\n""-1 15 45\n""45 -1 44\n""-1 -1 -1\n""-1 15 3\n""-1 -1 45\n""-1 45 45\n""3 45 44\n""-1 -1 -1\n""-1 -1 44\n""-1 44 2\n""2 2 44\n""-1 -1 -1\n""-1 2 5\n""5 5 44\n""-1 -1 -1\n""4 -1 4\n""-1 4 3\n""4 -1 4\n""-1 4 5\n""4 -1 4\n""-1 4 12\n""4 -1 4\n""-1 4 13\n""4 -1 4\n""-1 4 14\n""4 -1 4\n""-1 4 15\n""4 -1 4\n""-1 4 44\n""4 -1 4\n""44 -1 -1\n""-1 12 45\n""45 -1 44\n""-1 -1 -1\n""-1 12 3\n""3 -1 44\n""-1 -1 -1\n""-1 -1 45\n""-1 45 45\n""3 45 44\n""-1 -1 -1\n""-1 -1 44\n""-1 44 2\n""2 2 44\n""-1 -1 -1\n""-1 2 0\n""0 -1 0\n""-1 5 2\n""0 2 -1\n""-1 -1 -1\n""-1 14 45\n""45 -1 44\n""-1 -1 -1\n""-1 5 0\n""-1 12 44\n""44 -1 1\n""12 -1 7\n""-1 0 2\n""-1 0 6\n""-1 -1 44\n""4 -1 4\n""44 4 -1\n""-1 -1 -1\n""15 4 -1\n""4 -1 4\n""2 -1 15\n""14 4 -1\n""4 -1 4\n""6 -1 14\n""13 4 -1\n""4 -1 4\n""12 4 -1\n""4 -1 4\n""5 4 -1\n""4 -1 4\n""7 -1 5\n""3 4 -1\n""4 -1 4\n""4 -1 4\n""-1 7 45\n""45 -1 44\n""1 4 -1\n""-1 -1 -1\n""-1 7 3\n""-1 -1 45\n""-1 45 45\n""3 45 44\n""-1 -1 -1\n""-1 -1 44\n""-1 44 2\n""2 2 44\n""-1 -1 -1\n""-1 2 45\n""45 3 44\n""-1 -1 -1\n""-1 5 45\n""45 -1 44\n""-1 -1 -1\n""3 -1 44\n""-1 -1 -1\n""-1 -1 44\n""-1 44 13\n""13 13 44\n""-1 -1 -1\n""-1 13 0\n""-1 -1 44\n""0 44 -1\n""5 13 -1\n""-1 13 -1\n""-1 5 44\n""44 -1 0\n""0 -1 44\n""-1 -1 -1\n""-1 -1 0\n""-1 -1 -1\n""0 13 -1\n""5 -1 7\n""-1 -1 44\n""4 -1 4\n""44 4 -1\n""-1 -1 -1\n""12 4 -1\n""4 -1 4\n""5 4 -1\n""4 -1 4\n""-1 -1 5\n""3 4 -1\n""4 -1 4\n""-1 -1 3\n""4 -1 4\n""-1 4 12\n""7 4 -1\n""12 -1 7\n""-1 -1 44\n""4 -1 4\n""44 4 -1\n""-1 -1 -1\n""7 -1 0\n""-1 7 -1\n""-1 7 -1\n""-1 4 44\n""4 -1 4\n""44 -1 -1\n""-1 4 7\n""12 -1 2\n""-1 -1 6\n""-1 -1 44\n""4 -1 4\n""44 4 -1\n""-1 -1 -1\n""15 4 -1\n""4 -1 4\n""6 -1 15\n""2 -1 6\n""14 4 -1\n""4 -1 4\n""2 -1 14\n""13 4 -1\n""4 -1 4\n""12 4 -1\n""4 -1 4\n""5 4 -1\n""4 -1 4\n""3 4 -1\n""4 -1 4\n""4 -1 4\n""7 4 -1\n""-1 -1 44\n""4 -1 4\n""44 4 -1\n""15 -1 -1\n""4 -1 4\n""-1 7 0\n""6 -1 2\n""0 0 44\n""-1 -1 -1\n""-1 0 45\n""45 -1 44\n""-1 -1 -1\n""-1 0 6\n""2 -1 7\n""-1 -1 44\n""4 -1 4\n""44 4 -1\n""-1 -1 -1\n""12 4 -1\n""4 -1 4\n""6 -1 12\n""12 -1 12\n""5 4 -1\n""4 -1 4\n""7 -1 5\n""3 4 -1\n""4 -1 4\n""-1 7 7\n""6 -1 3\n""7 7 44\n""-1 -1 -1\n""-1 -1 44\n""-1 44 6\n""6 6 44\n""-1 -1 -1\n""-1 6 0\n""-1 -1 44\n""0 44 -1\n""3 -1 2\n""3 -1 3\n""-1 -1 0\n""2 -1 2\n""3 -1 1\n""-1 6 -1\n""-1 6 -1\n""2 -1 2\n""0 1 0\n""-1 5 45\n""45 -1 44\n""12 6 -1\n""2 6 44\n""0 44 -1\n""-1 -1 -1\n""-1 6 -1\n""-1 6 -1\n""6 5 -1\n""-1 -1 -1\n""6 5 -1\n""12 5 -1\n""-1 4 3\n""4 -1 4\n""-1 4 5\n""4 -1 4\n""-1 4 12\n""4 -1 4\n""-1 4 44\n""4 -1 4\n""44 -1 -1\n""-1 -1 0\n""4 -1 4\n""-1 4 44\n""4 -1 4\n""44 -1 -1\n""0 4 -1\n""0 -1 0\n""-1 -1 -1\n""-1 4 11\n""11 11 44\n""-1 -1 -1\n""-1 4 2\n""-1 2 0\n""0 0 44\n""-1 -1 -1\n""-1 0 44\n""44 -1 0\n""0 -1 1\n""-1 0 44\n""44 -1 0\n""1 4 -1\n""0 0 44\n""-1 -1 -1\n""0 -1 0\n""-1 4 -1\n""0 -1 0\n""0 4 -1\n""-1 4 3\n""-1 4 1\n""-1 4 2\n""1 3 44\n""44 -1 0\n""0 -1 44\n""-1 -1 -1\n""0 -1 44\n""-1 -1 -1\n""0 -1 44\n""-1 -1 -1\n""-1 4 45\n""45 -1 44\n""44 4 -1\n""-1 4 0\n""-1 4 45\n""45 0 44\n""-1 -1 -1\n""-1 4 3\n""-1 4 1\n""-1 4 2\n""1 3 44\n""44 -1 0\n""0 -1 44\n""-1 -1 -1\n""0 -1 44\n""-1 -1 -1\n""0 -1 44\n""-1 -1 -1\n""-1 4 45\n""45 -1 44\n""44 4 -1\n""-1 4 0\n""-1 4 45\n""45 0 44\n""-1 -1 -1\n""-1 -1 -1\n""-1 4 0\n""4 -1 4\n""-1 4 3\n""4 -1 4\n""-1 4 5\n""4 -1 4\n""-1 4 12\n""4 -1 4\n""-1 4 13\n""4 -1 4\n""-1 4 14\n""4 -1 4\n""-1 4 15\n""4 -1 4\n""-1 4 44\n""4 -1 4\n""44 -1 -1\n""-1 4 8\n""8 8 44\n""-1 -1 -1\n""-1 -1 9\n""9 8 6\n""9 -1 10\n""6 6 44\n""-1 -1 -1\n""-1 -1 7\n""-1 -1 11\n""-1 -1 -1\n""7 -1 1\n""11 -1 0\n""0 1 0\n""0 6 44\n""-1 -1 -1\n""0 -1 0\n""6 0 6\n""-1 8 0\n""0 10 0\n""0 -1 0\n""1 0 2\n""2 -1 44\n""-1 -1 -1\n""2 -1 44\n""-1 -1 -1\n""2 -1 44\n""-1 -1 -1\n""2 -1 44\n""-1 -1 -1\n""-1 2 0\n""0 -1 44\n""-1 -1 -1\n""2 -1 44\n""-1 -1 0\n""-1 -1 -1\n""3 0 3\n""6 6 44\n""-1 -1 -1\n""9 -1 9\n""9 -1 44\n""-1 -1 -1\n""9 8 6\n""9 -1 10\n""6 6 44\n""-1 -1 -1\n""9 -1 9\n""9 -1 44\n""-1 -1 -1\n""-1 8 8\n""8 8 44\n""-1 -1 -1\n""12 -1 7\n""-1 -1 44\n""4 -1 4\n""44 4 -1\n""-1 -1 -1\n""-1 7 0\n""0 0 44\n""-1 -1 -1\n""-1 -1 44\n""-1 44 1\n""-1 -1 -1\n""-1 0 2\n""1 0 -1\n""2 2 44\n""-1 -1 -1\n""-1 -1 44\n""0 44 -1\n""-1 7 -1\n""-1 7 -1\n""-1 4 44\n""4 -1 4\n""44 -1 -1\n""5 5 44\n""-1 -1 -1\n""4 -1 4\n""3 -1 0\n""-1 4 3\n""4 -1 4\n""-1 4 5\n""4 -1 4\n""-1 4 12\n""4 -1 4\n""-1 4 44\n""4 -1 4\n""44 -1 -1\n""15 -1 2\n""0 13 -1\n""-1 13 -1\n""-1 13 -1\n""2 -1 6\n""-1 13 -1\n""-1 4 0\n""-1 13 -1\n""-1 13 -1\n""6 13 -1\n""0 13 -1\n""-1 5 44\n""44 -1 1\n""-1 1 0\n""0 -1 44\n""-1 -1 -1\n""1 -1 44\n""-1 -1 -1\n""1 -1 44\n""-1 -1 -1\n""1 -1 44\n""-1 -1 -1\n""-1 -1 -1\n""1 -1 44\n""-1 -1 -1\n""-1 -1 -1\n""1 -1 44\n""-1 -1 -1\n""1 -1 44\n""-1 -1 -1\n""-1 5 0\n""0 -1 0\n""0 -1 44\n""-1 -1 -1\n""-1 -1 44\n""-1 44 8\n""5 8 44\n""-1 -1 -1\n""-1 -1 44\n""-1 44 7\n""5 7 44\n""-1 -1 -1\n""-1 -1 44\n""-1 44 11\n""5 11 44\n""-1 -1 -1\n""-1 -1 44\n""-1 44 9\n""5 9 44\n""-1 -1 -1\n""-1 -1 44\n""-1 44 10\n""5 10 44\n""-1 -1 -1\n""1 -1 44\n""-1 -1 -1\n""1 -1 44\n""-1 -1 1\n""-1 -1 1\n""-1 -1 -1\n""6 6 44\n""1 13 -1\n""-1 -1 -1\n""13 6 -1\n""14 14 44\n""2 -1 44\n""13 44 -1\n""-1 -1 -1\n""-1 14 12\n""-1 13 6\n""-1 13 8\n""-1 12 0\n""-1 12 2\n""0 6 44\n""-1 -1 -1\n""2 8 44\n""-1 -1 -1\n""8 -1 44\n""-1 -1 -1\n""2 -1 44\n""-1 -1 -1\n""0 6 44\n""-1 -1 -1\n""-1 -1 -1\n""2 8 44\n""-1 -1 -1\n""-1 -1 -1\n""8 -1 0\n""0 2 0\n""-1 -1 -1\n""-1 -1 -1\n""0 0 44\n""-1 -1 -1\n""8 -1 44\n""-1 -1 -1\n""6 -1 44\n""-1 -1 -1\n""12 -1 7\n""-1 -1 -1\n""-1 7 1\n""1 1 44\n""-1 -1 -1\n""-1 1 0\n""-1 1 2\n""0 6 44\n""-1 -1 -1\n""8 2 44\n""-1 -1 -1\n""0 6 44\n""-1 -1 -1\n""8 2 44\n""-1 -1 -1\n""-1 -1 -1\n""1 13 -1\n""13 1 -1\n""7 13 -1\n""13 7 -1\n""12 13 -1\n""-1 13 45\n""45 -1 44\n""-1 -1 -1\n""-1 5 45\n""45 -1 44\n""-1 -1 -1\n""-1 5 3\n""-1 -1 45\n""-1 45 45\n""3 45 44\n""-1 -1 -1\n""-1 -1 44\n""-1 44 2\n""2 2 44\n""-1 -1 -1\n""-1 2 44\n""44 -1 0\n""-1 -1 44\n""-1 44 2\n""0 0 0\n""0 -1 0\n""2 0 45\n""45 -1 44\n""-1 -1 -1\n""-1 5 45\n""45 -1 44\n""-1 -1 -1\n""-1 5 3\n""-1 -1 45\n""-1 45 45\n""3 45 44\n""-1 -1 -1\n""-1 -1 44\n""-1 44 2\n""2 2 44\n""-1 -1 -1\n""-1 2 44\n""44 -1 0\n""-1 -1 44\n""-1 44 6\n""0 0 0\n""0 -1 0\n""6 0 45\n""45 -1 44\n""-1 -1 -1\n""-1 5 3\n""-1 -1 45\n""-1 45 45\n""3 45 44\n""-1 5 44\n""44 -1 14\n""44 -1 14")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pipeline Simulator"))
        self.pipelineStages.setText(_translate("MainWindow", "FI,DI,CO,FO,EI,WO"))
        self.pipelineStages.setPlaceholderText(_translate("MainWindow", "comma separated: (FI,DI,CO,FO,EI,WO)"))
        self.label_6.setText(_translate("MainWindow", "Pipeline"))
        self.label_9.setText(_translate("MainWindow", "Trace:"))
        self.label_8.setText(_translate("MainWindow", "Register size"))
        self.label_5.setText(_translate("MainWindow", "Pipeline Setup"))
        self.label.setText(_translate("MainWindow", "Operand Stage"))
        self.label_4.setText(_translate("MainWindow", "Result Stage"))
        self.label_2.setText(_translate("MainWindow", "Instruction start"))
        self.label_3.setText(_translate("MainWindow", "Instruction end"))
        self.simulateButton.setText(_translate("MainWindow", "Run simulation"))
        self.helpButton.setText(_translate("MainWindow", "Help"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))
        self.label_10.setText(_translate("MainWindow", "Output"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setToolTip(_translate("MainWindow", "Quit"))
        self.actionSimulate.setText(_translate("MainWindow", "Simulate"))
        self.actionSimulate.setToolTip(_translate("MainWindow", "Simulate"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHelp.setToolTip(_translate("MainWindow", "Help"))
        self.loadTrace.setText(_translate("MainWindow", "Load example trace"))
        self.actionLoadTrace.setText(_translate("MainWindow", "LoadTrace"))
        self.actionLoadTrace.setToolTip(_translate("MainWindow", "LoadTrace"))

    def simulateCPUPipeline(self):
        # Typecasting variables as needed
        operandStage = int(self.operandstage.property("value"))
        resultStage = int(self.resultstage.property("value"))
        startChart = int(self.startat.property("value"))
        endChart = int(self.endat.property("value"))
        traceFile = self.traceText.property("plainText").splitlines()

        errors = ""

        if not self.pipelineStages.text().split(',') or len(self.pipelineStages.text().split(',')) <= 2:
            errors += "ERROR: Pipeline stages must not be empty, less than 3 stages, and should be comma separated\n"

        if not traceFile or len(traceFile) < len(self.pipelineStages.text().split(',')):
            errors += "ERROR: Trace must not be empty or less lines than the number of pipeline stages. Click on the \"Help\" button for more info.\n"

        if errors != "":
            self.textOutput.setProperty("plainText", errors)
            return

        pipelineStages = self.pipelineStages.text().split(',')
        numberRegisters = int(self.registernumbers.property("value"))

        textOutput = str("\nSTART SIMULATION: Pipeline simulation\n\n" +
                         "Operands Stage: " + str(operandStage) +
                         "\nResults Stage: " + str(resultStage) +
                         "\nStarting Instruction: " + str(startChart) +
                         "\nEnding Instruction: " + str(endChart)) + "\n\n"

        self.textOutput.setProperty("plainText", textOutput)

        instructionNumber = 0
        stageNum = 0
        stallNum = 0

        pipe = PipelineStatus(pipelineStages)
        regs = RegisterStatus(int(numberRegisters))

        textOutput2 = str(regs.printGraph())

        for position, line in enumerate(traceFile):

            if not line.split() or (len(line.split()) < 3 or len(line.split()) > 3) or \
                            all(int(i) > -2 for i in line.split()) is not True or \
                            all(int(i) < numberRegisters for i in line.split()) is not True:
                self.textOutput.setProperty("plainText", "ERROR: Trace lines are not formatted as should. Check line " + \
                                            str(position + 1) + ". Click on the \"Help\" button for more info.\n")
                return

            instructionNumber += 1

            op1 = int(line.split(" ")[0])
            op2 = int(line.split(" ")[1])
            result = int(line.split(" ")[2])

            if pipe.getStatus(resultStage):
                pipe.setInstrEx(pipe.getElement(resultStage).idNum)

            pipe.advancePipeline(resultStage)

            if pipe.getStatus(resultStage):
                regs.writeBack(pipe.getElement(resultStage))

            pipe.addInstruction(ProcessInfo(instructionNumber, op1, op2, result, False))

            # check and set stalls
            pipe.setStall(operandStage, regs.decode(pipe.getElement(operandStage)))

            if pipe.printGraph(stageNum, startChart, endChart):
                textOutput += str(pipe.printGraph(stageNum, startChart, endChart))

            stageNum += 1

            while pipe.getStall(operandStage):
                if pipe.getStatus(resultStage):
                    pipe.setInstrEx(pipe.getElement(resultStage).idNum)

                pipe.advancePipeline(resultStage)

                if pipe.getStatus(resultStage):
                    textOutput2 += str(regs.printGraph())
                    regs.writeBack(pipe.getElement(resultStage))

                # check and set stalls
                pipe.setStall(operandStage, regs.decode(pipe.getElement(operandStage)))

                if pipe.printGraph(stageNum, startChart, endChart):
                    textOutput += str(pipe.printGraph(stageNum, startChart, endChart))

                stageNum += 1
                stallNum += 1

        while not pipe.isEmpty():
            if pipe.getStatus(resultStage):
                pipe.setInstrEx(pipe.getElement(resultStage).idNum)

            pipe.advancePipeline(resultStage)

            if pipe.getStatus(resultStage):
                textOutput2 += str(regs.printGraph())
                regs.writeBack(pipe.getElement(resultStage))

            # check and set stalls
            pipe.setStall(operandStage, regs.decode(pipe.getElement(operandStage)))

            if pipe.printGraph(stageNum, startChart, endChart):
                textOutput += str(pipe.printGraph(stageNum, startChart, endChart))

            stageNum += 1

            # Handle Stalls
            if pipe.getStall(operandStage):
                stallNum += 1

        noPipeline = len(pipelineStages) * instructionNumber
        speedup = round(100 * (float(noPipeline) / float(stageNum)), 3)
        avgStalls = round(float(stallNum) / float(instructionNumber), 3)

        textOutput += str("\nAnalysis of the simulation: " +
                          "\nNumber of instructions executed: " + str(instructionNumber) +
                          "\nExpected Number of stages when unpipelined: " + str(noPipeline) +
                          "\nNumber of stall stages: " + str(stallNum) +
                          "\nNumber of stages in the pipeline simulation: " + str(stageNum) +
                          "\nAverage number of stalls per instruction: " + str(avgStalls) +
                          "\nSpeedup: " + str(speedup) + "%" +
                          "\n\nEND SIMULATION\n\n")

        self.textOutput.setProperty("plainText", textOutput)
        self.textOutput2.setProperty("plainText", textOutput2)


class ProcessInfo:
    idNum = 0
    operand1 = -1
    operand2 = -1
    stall = bool(False)
    result = -1

    def __init__(self, idNum=0, operand1=-1, operand2=-1, result=-1, stall=bool(False)):
        self.idNum = idNum
        self.operand1 = operand1
        self.operand2 = operand2
        self.result = result
        self.stall = bool(stall)


class PipelineStatus():
    size = 0
    instructionEx = 0
    stageID = []
    pipelineStatus = []

    def __init__(self, pipelineStages):
        self.size = len(pipelineStages)
        self.instructionEx = 0
        self.stageID = []
        self.pipelineStatus = []

        for stage in pipelineStages:
            self.stageID.append(stage)

        for i in range(0, self.size):
            self.pipelineStatus.append(ProcessInfo())

    def getStatus(self, index):
        if index < self.size:
            if self.pipelineStatus[index].idNum != 0:
                return bool(True)
            else:
                return bool(False)
        else:
            sys.exit("ERROR: index out of bounds on pipelineStatus structure!")

    def addInstruction(self, p):
        if self.pipelineStatus[0].idNum == 0:
            self.pipelineStatus[0] = p
        else:
            sys.exit("ERROR: FI is busy!")

    def setInstrEx(self, instructorNum):
        self.instructionEx = instructorNum

    def setStall(self, index, stall):
        if index < self.size:
            self.pipelineStatus[index].stall = bool(stall)

    def getStall(self, index):
        return self.pipelineStatus[index].stall

    def getElement(self, index):
        if index < self.size:
            return self.pipelineStatus[index]
        else:
            sys.exit("ERROR: Index out of bounds on pipelineStatus structure")

    def advancePipeline(self, resultStage):
        self.pipelineStatus[resultStage] = ProcessInfo()
        for i in range(self.size - 1, 0, -1):
            if (not self.pipelineStatus[i - 1].stall) and self.pipelineStatus[i].idNum == 0:
                self.pipelineStatus[i] = self.pipelineStatus[i - 1]
                self.pipelineStatus[i - 1] = ProcessInfo()

    def isEmpty(self):
        empty = bool(True)
        for i in range(0, self.size - 1):
            if self.pipelineStatus[i].idNum != 0:
                empty = bool(False)
        return empty

    def printGraph(self, cycleNum, startChart, stopChart):
        output = str()
        if self.pipelineStatus[0].idNum >= startChart and self.instructionEx <= stopChart and startChart > 0:
            for i in range(0, (self.instructionEx - startChart) + 1):
                output += str("   ")
                # sys.stdout.write("-- ")

            count = self.size
            while (count - 1) >= 0:
                if self.pipelineStatus[count - 1].idNum != 0:
                    if self.pipelineStatus[count - 1].idNum >= startChart and self.pipelineStatus[count - 1].idNum <= stopChart:
                        if self.pipelineStatus[count - 1].stall:
                            output += str("-- ")
                            count = 0
                        else:
                            output += str(self.stageID[count - 1] + " ")
                count -= 1

            output += str(os.linesep)
            return output


class RegisterInfo:
    lastWrite = 0
    nextWrite = 0

    def __init__(self):
        self.lastWrite = 0
        self.nextWrite = 0


class RegisterStatus:
    size = 0
    registerStatus = []

    def __init__(self, size):
        self.size = size
        self.registerStatus = []

        for i in range(0, self.size):
            self.registerStatus.append(RegisterInfo())

    def writeBack(self, p):
        if self.registerStatus[int(p.result)].nextWrite == p.idNum:
            self.registerStatus[int(p.result)].lastWrite = p.idNum
            self.registerStatus[int(p.result)].nextWrite = 0

    def decode(self, p):
        stall = bool(False)

        if p.operand1 != -1:
            if self.registerStatus[int(p.operand1)].nextWrite != 0 and self.registerStatus[
                int(p.operand1)].nextWrite < p.idNum:
                stall = bool(True)
        if p.operand2 != -1:
            if self.registerStatus[int(p.operand2)].nextWrite != 0 and self.registerStatus[
                int(p.operand2)].nextWrite < p.idNum:
                stall = bool(True)

        if (not stall) and p.result != -1:
            self.registerStatus[int(p.result)].nextWrite = p.idNum

        return stall

    def printGraph(self):
        textOutput = str("Register Status" + os.linesep)
        # sys.stdout.write("Register Status" + os.linesep)

        for i in range(0, self.size):
            if self.registerStatus[i].lastWrite != 0 or self.registerStatus[i].nextWrite != 0:
                textOutput += str("  Register " + str(i) + \
                                  ": Last Write - " + str(self.registerStatus[i].lastWrite) + \
                                  ", Next Write - " + str(self.registerStatus[i].nextWrite) + "\n")
        textOutput += os.linesep
        return textOutput


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
