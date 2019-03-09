# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Asus\Desktop\Crypter.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(582, 488)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(582, 468))
        self.centralwidget.setMaximumSize(QtCore.QSize(582, 468))
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 181, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 121, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 220, 161, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 370, 81, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 400, 181, 16))
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 110, 521, 101))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(130, 370, 421, 20))
        self.textEdit_3.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 430, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 430, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 40, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(315, 40, 85, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(420, 40, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 250, 521, 101))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 450, 201, 20))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SevCRYPT 2019"))
        self.label.setText(_translate("MainWindow", "Выберите алгоритм шифрования:"))
        self.label_2.setText(_translate("MainWindow", "Исходное сообщение:"))
        self.label_3.setText(_translate("MainWindow", "Зашифрованное сообщение:"))
        self.label_4.setText(_translate("MainWindow", "Введите ключ:"))
        self.label_5.setText(_translate("MainWindow", "Выберите необходимую операцию:"))
        self.pushButton.setText(_translate("MainWindow", "EnCrypt"))
        self.pushButton_2.setText(_translate("MainWindow", "DeCrypt"))
        self.pushButton_3.setText(_translate("MainWindow", "XOR"))
        self.pushButton_4.setText(_translate("MainWindow", "Подстановка"))
        self.pushButton_5.setText(_translate("MainWindow", "ГОСТ"))
        self.label_6.setText(_translate("MainWindow", "© Created by Ivan.Sorochinsky ver.0.1"))

