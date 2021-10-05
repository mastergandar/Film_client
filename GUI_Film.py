# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledyMhoFQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1182, 820)
        MainWindow.setStyleSheet(u"-")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit_Name = QTextEdit(self.centralwidget)
        self.textEdit_Name.setObjectName(u"textEdit_Name")
        self.textEdit_Name.setGeometry(QRect(440, 80, 311, 31))
        self.textEdit_actor = QTextEdit(self.centralwidget)
        self.textEdit_actor.setObjectName(u"textEdit_actor")
        self.textEdit_actor.setGeometry(QRect(820, 30, 311, 161))
        self.textEdit_coments = QTextEdit(self.centralwidget)
        self.textEdit_coments.setObjectName(u"textEdit_coments")
        self.textEdit_coments.setGeometry(QRect(420, 290, 761, 391))
        self.comboBox_category = QComboBox(self.centralwidget)
        self.comboBox_category.setObjectName(u"comboBox_category")
        self.comboBox_category.setGeometry(QRect(440, 130, 211, 31))
        self.comboBox_country = QComboBox(self.centralwidget)
        self.comboBox_country.setObjectName(u"comboBox_country")
        self.comboBox_country.setGeometry(QRect(440, 180, 211, 31))
        self.label_Name = QLabel(self.centralwidget)
        self.label_Name.setObjectName(u"label_Name")
        self.label_Name.setGeometry(QRect(260, 80, 181, 41))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Name.setFont(font)
        self.label_Name_2 = QLabel(self.centralwidget)
        self.label_Name_2.setObjectName(u"label_Name_2")
        self.label_Name_2.setGeometry(QRect(260, 130, 131, 31))
        self.label_Name_2.setFont(font)
        self.label_Name_3 = QLabel(self.centralwidget)
        self.label_Name_3.setObjectName(u"label_Name_3")
        self.label_Name_3.setGeometry(QRect(260, 180, 111, 31))
        self.label_Name_3.setFont(font)
        self.label_Name_4 = QLabel(self.centralwidget)
        self.label_Name_4.setObjectName(u"label_Name_4")
        self.label_Name_4.setGeometry(QRect(270, 300, 121, 51))
        self.label_Name_4.setFont(font)
        self.label_Name_5 = QLabel(self.centralwidget)
        self.label_Name_5.setObjectName(u"label_Name_5")
        self.label_Name_5.setGeometry(QRect(890, 6, 121, 20))
        self.label_Name_5.setFont(font)
        self.pushButton_Image = QPushButton(self.centralwidget)
        self.pushButton_Image.setObjectName(u"pushButton_Image")
        self.pushButton_Image.setGeometry(QRect(290, 690, 81, 61))
        self.pushButton_Delete = QPushButton(self.centralwidget)
        self.pushButton_Delete.setObjectName(u"pushButton_Delete")
        self.pushButton_Delete.setGeometry(QRect(950, 700, 131, 51))
        self.pushButton_Change = QPushButton(self.centralwidget)
        self.pushButton_Change.setObjectName(u"pushButton_Change")
        self.pushButton_Change.setGeometry(QRect(790, 700, 131, 51))
        self.pushButton_Create = QPushButton(self.centralwidget)
        self.pushButton_Create.setObjectName(u"pushButton_Create")
        self.pushButton_Create.setGeometry(QRect(630, 700, 131, 51))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(260, 250, 931, 51))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_NumberD = QLabel(self.centralwidget)
        self.label_NumberD.setObjectName(u"label_NumberD")
        self.label_NumberD.setGeometry(QRect(260, 30, 151, 31))
        self.label_NumberD.setFont(font)
        self.textEdit_Number = QTextEdit(self.centralwidget)
        self.textEdit_Number.setObjectName(u"textEdit_Number")
        self.textEdit_Number.setGeometry(QRect(440, 30, 311, 31))
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 251, 501))
        self.pushButton_Search = QPushButton(self.centralwidget)
        self.pushButton_Search.setObjectName(u"pushButton_Search")
        self.pushButton_Search.setGeometry(QRect(450, 700, 131, 51))
        self.label_pic = QLabel(self.centralwidget)
        self.label_pic.setObjectName(u"label_pic")
        self.label_pic.setGeometry(QRect(10, 510, 265, 265))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1182, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_Name.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.label_Name_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label_Name_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u043d\u0430", None))
        self.label_Name_4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.label_Name_5.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442\u0435\u0440\u044b", None))
        self.pushButton_Image.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.pushButton_Delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton_Change.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButton_Create.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_NumberD.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0414\u0438\u0441\u043a\u0430", None))
        self.pushButton_Search.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0434\u0438\u0441\u043a\u0443", None))
        self.label_pic.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

