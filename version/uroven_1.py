# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uroven_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_uroven_1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 500)
        MainWindow.setMinimumSize(QtCore.QSize(450, 500))
        MainWindow.setMaximumSize(QtCore.QSize(450, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_vosvrat = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_vosvrat.setObjectName("pushButton_vosvrat")
        self.verticalLayout.addWidget(self.pushButton_vosvrat)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_y1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_y1_1.setMinimumSize(QtCore.QSize(170, 170))
        self.pushButton_y1_1.setMaximumSize(QtCore.QSize(170, 170))
        self.pushButton_y1_1.setObjectName("pushButton_y1_1")
        self.horizontalLayout.addWidget(self.pushButton_y1_1)
        self.pushButton_y1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_y1_2.setMinimumSize(QtCore.QSize(170, 170))
        self.pushButton_y1_2.setMaximumSize(QtCore.QSize(170, 170))
        self.pushButton_y1_2.setObjectName("pushButton_y1_2")
        self.horizontalLayout.addWidget(self.pushButton_y1_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_y1_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_y1_3.setMinimumSize(QtCore.QSize(170, 170))
        self.pushButton_y1_3.setMaximumSize(QtCore.QSize(170, 170))
        self.pushButton_y1_3.setObjectName("pushButton_y1_3")
        self.horizontalLayout_2.addWidget(self.pushButton_y1_3)
        self.pushButton_y1_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_y1_4.setMinimumSize(QtCore.QSize(170, 170))
        self.pushButton_y1_4.setMaximumSize(QtCore.QSize(170, 170))
        self.pushButton_y1_4.setObjectName("pushButton_y1_4")
        self.horizontalLayout_2.addWidget(self.pushButton_y1_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Уровень 1"))
        MainWindow.setWindowIcon(QtGui.QIcon('иконка.png'))
        self.pushButton_vosvrat.setText(_translate("MainWindow", "Вернуться назад"))
        self.pushButton_y1_1.setText(_translate("MainWindow", "X"))
        self.pushButton_y1_2.setText(_translate("MainWindow", "X"))
        self.pushButton_y1_3.setText(_translate("MainWindow", "X"))
        self.pushButton_y1_4.setText(_translate("MainWindow", "X"))

        self.pushButton_vosvrat.setStyleSheet('QPushButton {background-color: #EEE8AA;}')
        self.pushButton_y1_1.setStyleSheet('QPushButton {background-color: #EEE8AA; border-radius: 15px}')
        self.pushButton_y1_2.setStyleSheet('QPushButton {background-color: #EEE8AA; border-radius: 15px}')
        self.pushButton_y1_3.setStyleSheet('QPushButton {background-color: #EEE8AA; border-radius: 15px}')
        self.pushButton_y1_4.setStyleSheet('QPushButton {background-color: #EEE8AA; border-radius: 15px}')

