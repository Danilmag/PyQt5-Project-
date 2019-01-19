# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_urovni.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_urovni(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_menu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_menu.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_menu.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_menu.setObjectName("pushButton_menu")
        self.verticalLayout.addWidget(self.pushButton_menu)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_uroven1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_uroven1.setMaximumSize(QtCore.QSize(170, 100))
        self.pushButton_uroven1.setObjectName("pushButton_uroven1")
        self.horizontalLayout_2.addWidget(self.pushButton_uroven1)
        self.pushButton_uroven2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_uroven2.setMaximumSize(QtCore.QSize(170, 100))
        self.pushButton_uroven2.setObjectName("pushButton_uroven2")
        self.horizontalLayout_2.addWidget(self.pushButton_uroven2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_uroven3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_uroven3.setMaximumSize(QtCore.QSize(170, 100))
        self.pushButton_uroven3.setObjectName("pushButton_uroven3")
        self.horizontalLayout_3.addWidget(self.pushButton_uroven3)
        self.pushButton_uroven4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_uroven4.setMaximumSize(QtCore.QSize(170, 100))
        self.pushButton_uroven4.setObjectName("pushButton_uroven4")
        self.horizontalLayout_3.addWidget(self.pushButton_uroven4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_uroven5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_uroven5.setMaximumSize(QtCore.QSize(170, 100))
        self.pushButton_uroven5.setObjectName("pushButton_uroven5")
        self.horizontalLayout.addWidget(self.pushButton_uroven5)
        self.pushButton_uroven6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_uroven6.setMaximumSize(QtCore.QSize(170, 100))
        self.pushButton_uroven6.setObjectName("pushButton_uroven6")
        self.horizontalLayout.addWidget(self.pushButton_uroven6)
        self.verticalLayout.addLayout(self.horizontalLayout)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Выбор уровня"))
        MainWindow.setWindowIcon(QtGui.QIcon('иконка.png'))
        self.pushButton_menu.setText(_translate("MainWindow", "Главное меню"))
        self.pushButton_uroven1.setText(_translate("MainWindow", "Уровень 1"))
        self.pushButton_uroven2.setText(_translate("MainWindow", "Уровень 2"))
        self.pushButton_uroven3.setText(_translate("MainWindow", "Уровень 3"))
        self.pushButton_uroven4.setText(_translate("MainWindow", "Уровень 4"))
        self.pushButton_uroven5.setText(_translate("MainWindow", "Уровень 5"))
        self.pushButton_uroven6.setText(_translate("MainWindow", "Уровень 6"))
        self.pushButton_menu.setStyleSheet('QPushButton {background-color: #EEE8AA; border-radius: 15px}')
        self.pushButton_uroven1.setStyleSheet('QPushButton {background-color: #EEE8AA; border-radius: 15px}')
        self.pushButton_uroven2.setStyleSheet('QPushButton {background-color: #EEE8AA; border-radius: 15px}')
        self.pushButton_uroven3.setStyleSheet('QPushButton {background-color: #EEE8AA; border-radius: 15px}')
        self.pushButton_uroven4.setStyleSheet('QPushButton {background-color: #EEE8AA; border-radius: 15px}')
        self.pushButton_uroven5.setStyleSheet('QPushButton {background-color: #EEE8AA; border-radius: 15px}')
        self.pushButton_uroven6.setStyleSheet('QPushButton {background-color: #EEE8AA; border-radius: 15px}')

