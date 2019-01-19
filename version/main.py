import sys  # sys нужен для передачи argv в QApplication

from design_urovni import Ui_MainWindow_urovni
from uroven_1 import Ui_MainWindow_uroven_1
from uroven_2 import Ui_MainWindow_uroven_2
from uroven_3 import Ui_MainWindow_uroven_3
from uroven_4 import Ui_MainWindow_uroven_4
from uroven_5 import Ui_MainWindow_uroven_5
from uroven_6 import Ui_MainWindow_uroven_6
from PyQt5 import QtCore, QtGui
import time
import random
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtCore import Qt

nomera = []
uroven = ''


class opening(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 250, 200, 200)
        self.setWindowTitle("Тренер памяти")
        self.setWindowIcon(QtGui.QIcon('иконка.png'))

        self.btn = QPushButton('Начать', self)
        self.btn.resize(200, 150)

        self.btv = QPushButton('Выход', self)
        self.btv.resize(200, 50)
        self.btv.move(0, 150)

        self.btn.setStyleSheet('QPushButton {background-color: #9CEE90;}')
        self.btv.setStyleSheet('QPushButton {background-color: #FFE4C4;}')

        self.btn.clicked.connect(self.perechod)
        self.btv.clicked.connect(self.vyhod)

    def vyhod(self):
        self.close()

    def perechod(self):
        self.window = vyber_urovnya()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение


class vyber_urovnya(QMainWindow, Ui_MainWindow_urovni):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_uroven1.clicked.connect(self.perechod_u_1)
        self.pushButton_uroven2.clicked.connect(self.perechod_u_2)
        self.pushButton_uroven3.clicked.connect(self.perechod_u_3)
        self.pushButton_uroven4.clicked.connect(self.perechod_u_4)
        self.pushButton_uroven5.clicked.connect(self.perechod_u_5)
        self.pushButton_uroven6.clicked.connect(self.perechod_u_6)
        self.pushButton_menu.clicked.connect(self.perechod_M)

    def perechod_u_1(self):
        self.window = uroven_1()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def perechod_u_2(self):
        self.window = uroven_2()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def perechod_u_3(self):
        self.window = uroven_3()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def perechod_u_4(self):
        self.window = uroven_4()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def perechod_u_5(self):
        self.window = uroven_5()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def perechod_u_6(self):
        self.window = uroven_6()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def perechod_M(self):
        self.window = opening()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()


class uroven_1(QMainWindow, Ui_MainWindow_uroven_1):
    def __init__(self):
        global nomera
        nomera = []
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_vosvrat.clicked.connect(self.vosvrat)

        self.a = 0

        for self.i in range(2):
            self.a = random.randint(1, 4)
            while self.a in nomera:
                self.a = random.randint(1, 4)
            nomera.append(self.a)

        if 1 in nomera:
            self.pushButton_y1_1.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 2 in nomera:
            self.pushButton_y1_2.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 3 in nomera:
            self.pushButton_y1_3.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 4 in nomera:
            self.pushButton_y1_4.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')

        self.timer = QtCore.QTimer()
        self.timer.start(5000)
        self.timer.timeout.connect(self.rab_1)

    def rab_1(self):
        self.timer.stop()
        self.window = uroven_1_r()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def vosvrat(self):
        self.timer.stop()
        self.window = vyber_urovnya()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение


class uroven_1_r(QMainWindow, Ui_MainWindow_uroven_1):
    def __init__(self):
        global nomera, uroven
        uroven = 'u1'  # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_vosvrat.clicked.connect(self.vosvrat)
        self.pushButton_y1_1.clicked.connect(self.puch_y1_1)
        self.pushButton_y1_2.clicked.connect(self.puch_y1_2)
        self.pushButton_y1_3.clicked.connect(self.puch_y1_3)
        self.pushButton_y1_4.clicked.connect(self.puch_y1_4)

    def puch_y1_1(self):
        if 1 in nomera:
            self.pushButton_y1_1.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(1)]
        elif 1 not in nomera:
            self.proigrash_1()
        if len(nomera) == 0:
            self.perechod_u_2()

    def puch_y1_2(self):
        if 2 in nomera:
            self.pushButton_y1_2.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(2)]
        elif 2 not in nomera:
            self.proigrash_1()
        if len(nomera) == 0:
            self.perechod_u_2()

    def puch_y1_3(self):
        if 3 in nomera:
            self.pushButton_y1_3.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(3)]
        elif 3 not in nomera:
            self.proigrash_1()
        if len(nomera) == 0:
            self.perechod_u_2()

    def puch_y1_4(self):
        if 4 in nomera:
            self.pushButton_y1_4.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(4)]
        elif 4 not in nomera:
            self.proigrash_1()
        if len(nomera) == 0:
            self.perechod_u_2()

    def perechod_u_2(self):
        self.window = uroven_2()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def vosvrat(self):

        self.window = vyber_urovnya()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def proigrash_1(self):
        self.window = proigrash()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()


class proigrash(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 250, 200, 200)
        self.setWindowTitle("Проигрыш!")
        self.setWindowIcon(QtGui.QIcon('иконка.png'))

        self.btn = QPushButton('Вы проиграли!', self)
        self.btn.resize(200, 200)
        self.btn.setStyleSheet('QPushButton {background-color: #FFE4C4;}')

        self.btn.clicked.connect(self.pereshod)

    def pereshod(self):
        if uroven == 'u1':
            self.window = uroven_1()  # Создаём объект класса ExampleApp
        if uroven == 'u2':
            self.window = uroven_2()  # Создаём объект класса ExampleApp
        if uroven == 'u3':
            self.window = uroven_3()  # Создаём объект класса ExampleApp
        if uroven == 'u4':
            self.window = uroven_4()  # Создаём объект класса ExampleApp
        if uroven == 'u5':
            self.window = uroven_5()  # Создаём объект класса ExampleApp
        if uroven == 'u6':
            self.window = uroven_6()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение


class uroven_2(QMainWindow, Ui_MainWindow_uroven_2):

    def __init__(self):
        global nomera
        nomera = []
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_vosvrat.clicked.connect(self.vosvrat)

        self.a = 0

        for self.i in range(4):
            self.a = random.randint(1, 9)
            while self.a in nomera:
                self.a = random.randint(1, 9)
            nomera.append(self.a)

        if 1 in nomera:
            self.pushButton_y2_1.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 2 in nomera:
            self.pushButton_y2_2.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 3 in nomera:
            self.pushButton_y2_3.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 4 in nomera:
            self.pushButton_y2_4.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 5 in nomera:
            self.pushButton_y2_5.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 6 in nomera:
            self.pushButton_y2_6.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 7 in nomera:
            self.pushButton_y2_7.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 8 in nomera:
            self.pushButton_y2_8.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 9 in nomera:
            self.pushButton_y2_9.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')

        self.timer = QtCore.QTimer()
        self.timer.start(5000)
        self.timer.timeout.connect(self.rab_2)

    def rab_2(self):
        self.timer.stop()
        self.window = uroven_2_r()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def vosvrat(self):
        self.timer.stop()
        self.window = vyber_urovnya()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение


class uroven_2_r(QMainWindow, Ui_MainWindow_uroven_2):
    def __init__(self):
        global nomera, uroven
        uroven = 'u2'
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_vosvrat.clicked.connect(self.vosvrat)
        self.pushButton_y2_1.clicked.connect(self.puch_y2_1)
        self.pushButton_y2_2.clicked.connect(self.puch_y2_2)
        self.pushButton_y2_3.clicked.connect(self.puch_y2_3)
        self.pushButton_y2_4.clicked.connect(self.puch_y2_4)
        self.pushButton_y2_5.clicked.connect(self.puch_y2_5)
        self.pushButton_y2_6.clicked.connect(self.puch_y2_6)
        self.pushButton_y2_7.clicked.connect(self.puch_y2_7)
        self.pushButton_y2_8.clicked.connect(self.puch_y2_8)
        self.pushButton_y2_9.clicked.connect(self.puch_y2_9)

    def puch_y2_1(self):
        if 1 in nomera:
            self.pushButton_y2_1.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(1)]
        elif 1 not in nomera:
            self.proigrash_2()
        if len(nomera) == 0:
            self.perechod_u_3()

    def puch_y2_2(self):
        if 2 in nomera:
            self.pushButton_y2_2.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(2)]
        elif 2 not in nomera:
            self.proigrash_2()
        if len(nomera) == 0:
            self.perechod_u_3()

    def puch_y2_3(self):
        if 3 in nomera:
            self.pushButton_y2_3.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(3)]
        elif 3 not in nomera:
            self.proigrash_2()
        if len(nomera) == 0:
            self.perechod_u_3()

    def puch_y2_4(self):
        if 4 in nomera:
            self.pushButton_y2_4.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(4)]
        elif 4 not in nomera:
            self.proigrash_2()
        if len(nomera) == 0:
            self.perechod_u_3()

    def puch_y2_5(self):
        if 5 in nomera:
            self.pushButton_y2_5.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(5)]
        elif 5 not in nomera:
            self.proigrash_2()
        if len(nomera) == 0:
            self.perechod_u_3()

    def puch_y2_6(self):
        if 6 in nomera:
            self.pushButton_y2_6.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(6)]
        elif 6 not in nomera:
            self.proigrash_2()
        if len(nomera) == 0:
            self.perechod_u_3()

    def puch_y2_7(self):
        if 7 in nomera:
            self.pushButton_y2_7.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(7)]
        elif 7 not in nomera:
            self.proigrash_2()
        if len(nomera) == 0:
            self.perechod_u_3()

    def puch_y2_8(self):
        if 8 in nomera:
            self.pushButton_y2_8.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(8)]
        elif 8 not in nomera:
            self.proigrash_2()
        if len(nomera) == 0:
            self.perechod_u_3()

    def puch_y2_9(self):
        if 9 in nomera:
            self.pushButton_y2_9.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(9)]
        elif 9 not in nomera:
            self.proigrash_2()
        if len(nomera) == 0:
            self.perechod_u_3()

    def perechod_u_3(self):
        self.window = uroven_3()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def vosvrat(self):
        self.window = vyber_urovnya()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def proigrash_2(self):
        self.window = proigrash()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()


class uroven_3(QMainWindow, Ui_MainWindow_uroven_3):
    def __init__(self):
        global nomera, uroven
        nomera = []

        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_vosvrat.clicked.connect(self.vosvrat)

        self.a = 0

        for self.i in range(8):
            self.a = random.randint(1, 16)
            while self.a in nomera:
                self.a = random.randint(1, 16)
            nomera.append(self.a)

        if 1 in nomera:
            self.pushButton_y3_1.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 2 in nomera:
            self.pushButton_y3_2.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 3 in nomera:
            self.pushButton_y3_3.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 4 in nomera:
            self.pushButton_y3_4.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 5 in nomera:
            self.pushButton_y3_5.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 6 in nomera:
            self.pushButton_y3_6.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 7 in nomera:
            self.pushButton_y3_7.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 8 in nomera:
            self.pushButton_y3_8.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 9 in nomera:
            self.pushButton_y3_9.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 10 in nomera:
            self.pushButton_y3_10.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 11 in nomera:
            self.pushButton_y3_11.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 12 in nomera:
            self.pushButton_y3_12.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 13 in nomera:
            self.pushButton_y3_13.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 14 in nomera:
            self.pushButton_y3_14.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 15 in nomera:
            self.pushButton_y3_15.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 16 in nomera:
            self.pushButton_y3_16.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')

        self.timer = QtCore.QTimer()
        self.timer.start(5000)
        self.timer.timeout.connect(self.rab_3)

    def rab_3(self):
        self.timer.stop()
        self.window = uroven_3_r()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def vosvrat(self):
        self.timer.stop()
        self.window = vyber_urovnya()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение


class uroven_3_r(QMainWindow, Ui_MainWindow_uroven_3):
    def __init__(self):
        global nomera, uroven
        uroven = 'u3'
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_vosvrat.clicked.connect(self.vosvrat)
        self.pushButton_y3_1.clicked.connect(self.puch_y3_1)
        self.pushButton_y3_2.clicked.connect(self.puch_y3_2)
        self.pushButton_y3_3.clicked.connect(self.puch_y3_3)
        self.pushButton_y3_4.clicked.connect(self.puch_y3_4)
        self.pushButton_y3_5.clicked.connect(self.puch_y3_5)
        self.pushButton_y3_6.clicked.connect(self.puch_y3_6)
        self.pushButton_y3_7.clicked.connect(self.puch_y3_7)
        self.pushButton_y3_8.clicked.connect(self.puch_y3_8)
        self.pushButton_y3_9.clicked.connect(self.puch_y3_9)
        self.pushButton_y3_10.clicked.connect(self.puch_y3_10)
        self.pushButton_y3_11.clicked.connect(self.puch_y3_11)
        self.pushButton_y3_12.clicked.connect(self.puch_y3_12)
        self.pushButton_y3_13.clicked.connect(self.puch_y3_13)
        self.pushButton_y3_14.clicked.connect(self.puch_y3_14)
        self.pushButton_y3_15.clicked.connect(self.puch_y3_15)
        self.pushButton_y3_16.clicked.connect(self.puch_y3_16)

    def puch_y3_1(self):
        if 1 in nomera:
            self.pushButton_y3_1.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(1)]
        elif 1 not in nomera:
            self.proigrash_3()
        if len(nomera) == 0:
            self.perechod_u_4()

    def puch_y3_2(self):
        if 2 in nomera:
            self.pushButton_y3_2.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(2)]
        elif 2 not in nomera:
            self.proigrash_3()
        if len(nomera) == 0:
            self.perechod_u_4()

    def puch_y3_3(self):
        if 3 in nomera:
            self.pushButton_y3_3.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(3)]
        elif 3 not in nomera:
            self.proigrash_3()
        if len(nomera) == 0:
            self.perechod_u_4()

    def puch_y3_4(self):
        if 4 in nomera:
            self.pushButton_y3_4.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(4)]
        elif 4 not in nomera:
            self.proigrash_3()
        if len(nomera) == 0:
            self.perechod_u_4()

    def puch_y3_5(self):
        if 5 in nomera:
            self.pushButton_y3_5.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(5)]
        elif 5 not in nomera:
            self.proigrash_3()
        if len(nomera) == 0:
            self.perechod_u_4()

    def puch_y3_6(self):
        if 6 in nomera:
            self.pushButton_y3_6.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(6)]
        elif 6 not in nomera:
            self.proigrash_3()
        if len(nomera) == 0:
            self.perechod_u_4()

    def puch_y3_7(self):
        if 7 in nomera:
            self.pushButton_y3_7.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(7)]
        elif 7 not in nomera:
            self.proigrash_3()
        if len(nomera) == 0:
            self.perechod_u_4()

    def puch_y3_8(self):
        if 8 in nomera:
            self.pushButton_y3_8.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(8)]
        elif 8 not in nomera:
            self.proigrash_3()
        if len(nomera) == 0:
            self.perechod_u_4()

    def puch_y3_9(self):
        if 9 in nomera:
            self.pushButton_y3_9.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(9)]
        elif 9 not in nomera:
            self.proigrash_3()
        if len(nomera) == 0:
            self.perechod_u_4()

    def puch_y3_10(self):
        if 10 in nomera:
            self.pushButton_y3_10.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(10)]
        elif 10 not in nomera:
            self.proigrash_3()
        if len(nomera) == 0:
            self.perechod_u_4()

    def puch_y3_11(self):
        if 11 in nomera:
            self.pushButton_y3_11.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(11)]
        elif 11 not in nomera:
            self.proigrash_3()
        if len(nomera) == 0:
            self.perechod_u_4()

    def puch_y3_12(self):
        if 12 in nomera:
            self.pushButton_y3_12.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(12)]
        elif 12 not in nomera:
            self.proigrash_3()
        if len(nomera) == 0:
            self.perechod_u_4()

    def puch_y3_13(self):
        if 13 in nomera:
            self.pushButton_y3_13.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(13)]
        elif 13 not in nomera:
            self.proigrash_3()
        if len(nomera) == 0:
            self.perechod_u_4()

    def puch_y3_14(self):
        if 14 in nomera:
            self.pushButton_y3_14.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(14)]
        elif 14 not in nomera:
            self.proigrash_3()
        if len(nomera) == 0:
            self.perechod_u_4()

    def puch_y3_15(self):
        if 15 in nomera:
            self.pushButton_y3_15.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(15)]
        elif 15 not in nomera:
            self.proigrash_3()
        if len(nomera) == 0:
            self.perechod_u_4()

    def puch_y3_16(self):
        if 16 in nomera:
            self.pushButton_y3_16.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(16)]
        elif 16 not in nomera:
            self.proigrash_3()
        if len(nomera) == 0:
            self.perechod_u_4()

    def perechod_u_4(self):
        self.window = uroven_4()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def vosvrat(self):
        self.window = vyber_urovnya()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def proigrash_3(self):
        self.window = proigrash()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()


class uroven_4(QMainWindow, Ui_MainWindow_uroven_4):
    def __init__(self):
        global nomera
        nomera = []
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_vosvrat.clicked.connect(self.vosvrat)

        self.a = 0

        for self.i in range(12):
            self.a = random.randint(1, 25)
            while self.a in nomera:
                self.a = random.randint(1, 25)
            nomera.append(self.a)

        if 1 in nomera:
            self.pushButton_y4_1.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 2 in nomera:
            self.pushButton_y4_2.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 3 in nomera:
            self.pushButton_y4_3.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 4 in nomera:
            self.pushButton_y4_4.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 5 in nomera:
            self.pushButton_y4_5.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 6 in nomera:
            self.pushButton_y4_6.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 7 in nomera:
            self.pushButton_y4_7.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 8 in nomera:
            self.pushButton_y4_8.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 9 in nomera:
            self.pushButton_y4_9.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 10 in nomera:
            self.pushButton_y4_10.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 11 in nomera:
            self.pushButton_y4_11.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 12 in nomera:
            self.pushButton_y4_12.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 13 in nomera:
            self.pushButton_y4_13.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 14 in nomera:
            self.pushButton_y4_14.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 15 in nomera:
            self.pushButton_y4_15.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 16 in nomera:
            self.pushButton_y4_16.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 17 in nomera:
            self.pushButton_y4_17.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 18 in nomera:
            self.pushButton_y4_18.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 19 in nomera:
            self.pushButton_y4_19.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 20 in nomera:
            self.pushButton_y4_20.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 21 in nomera:
            self.pushButton_y4_21.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 22 in nomera:
            self.pushButton_y4_22.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 23 in nomera:
            self.pushButton_y4_23.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 24 in nomera:
            self.pushButton_y4_24.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 25 in nomera:
            self.pushButton_y4_25.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')

        self.timer = QtCore.QTimer()
        self.timer.start(5000)
        self.timer.timeout.connect(self.rab_4)

    def rab_4(self):
        self.timer.stop()
        self.window = uroven_4_r()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def vosvrat(self):
        self.timer.stop()
        self.window = vyber_urovnya()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение


class uroven_5(QMainWindow, Ui_MainWindow_uroven_5):
    def __init__(self):
        global nomera
        nomera = []
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_vosvrat.clicked.connect(self.vosvrat)

        self.a = 0

        for self.i in range(18):
            self.a = random.randint(1, 36)
            while self.a in nomera:
                self.a = random.randint(1, 36)
            nomera.append(self.a)

        if 1 in nomera:
            self.pushButton_y5_1.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 2 in nomera:
            self.pushButton_y5_2.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 3 in nomera:
            self.pushButton_y5_3.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 4 in nomera:
            self.pushButton_y5_4.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 5 in nomera:
            self.pushButton_y5_5.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 6 in nomera:
            self.pushButton_y5_6.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 7 in nomera:
            self.pushButton_y5_7.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 8 in nomera:
            self.pushButton_y5_8.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 9 in nomera:
            self.pushButton_y5_9.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 10 in nomera:
            self.pushButton_y5_10.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 11 in nomera:
            self.pushButton_y5_11.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 12 in nomera:
            self.pushButton_y5_12.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 13 in nomera:
            self.pushButton_y5_13.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 14 in nomera:
            self.pushButton_y5_14.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 15 in nomera:
            self.pushButton_y5_15.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 16 in nomera:
            self.pushButton_y5_16.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 17 in nomera:
            self.pushButton_y5_17.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 18 in nomera:
            self.pushButton_y5_18.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 19 in nomera:
            self.pushButton_y5_19.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 20 in nomera:
            self.pushButton_y5_20.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 21 in nomera:
            self.pushButton_y5_21.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 22 in nomera:
            self.pushButton_y5_22.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 23 in nomera:
            self.pushButton_y5_23.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 24 in nomera:
            self.pushButton_y5_24.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 25 in nomera:
            self.pushButton_y5_25.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 26 in nomera:
            self.pushButton_y5_26.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 27 in nomera:
            self.pushButton_y5_27.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 28 in nomera:
            self.pushButton_y5_28.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 29 in nomera:
            self.pushButton_y5_29.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 30 in nomera:
            self.pushButton_y5_30.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 31 in nomera:
            self.pushButton_y5_31.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 32 in nomera:
            self.pushButton_y5_32.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 33 in nomera:
            self.pushButton_y5_33.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 34 in nomera:
            self.pushButton_y5_34.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 35 in nomera:
            self.pushButton_y5_35.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 36 in nomera:
            self.pushButton_y5_36.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')

        self.timer = QtCore.QTimer()
        self.timer.start(5000)
        self.timer.timeout.connect(self.rab_5)

    def rab_5(self):
        self.timer.stop()
        self.window = uroven_5_r()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def vosvrat(self):
        self.timer.stop()
        self.window = vyber_urovnya()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение


class uroven_6(QMainWindow, Ui_MainWindow_uroven_6):
    def __init__(self):
        global nomera
        nomera = []
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_vosvrat.clicked.connect(self.vosvrat)

        self.a = 0

        for self.i in range(24):
            self.a = random.randint(1, 49)
            while self.a in nomera:
                self.a = random.randint(1, 49)
            nomera.append(self.a)

        if 1 in nomera:
            self.pushButton_y6_1.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 2 in nomera:
            self.pushButton_y6_2.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 3 in nomera:
            self.pushButton_y6_3.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 4 in nomera:
            self.pushButton_y6_4.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 5 in nomera:
            self.pushButton_y6_5.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 6 in nomera:
            self.pushButton_y6_6.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 7 in nomera:
            self.pushButton_y6_7.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 8 in nomera:
            self.pushButton_y6_8.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 9 in nomera:
            self.pushButton_y6_9.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 10 in nomera:
            self.pushButton_y6_10.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 11 in nomera:
            self.pushButton_y6_11.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 12 in nomera:
            self.pushButton_y6_12.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 13 in nomera:
            self.pushButton_y6_13.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 14 in nomera:
            self.pushButton_y6_14.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 15 in nomera:
            self.pushButton_y6_15.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 16 in nomera:
            self.pushButton_y6_16.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 17 in nomera:
            self.pushButton_y6_17.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 18 in nomera:
            self.pushButton_y6_18.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 19 in nomera:
            self.pushButton_y6_19.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 20 in nomera:
            self.pushButton_y6_20.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 21 in nomera:
            self.pushButton_y6_21.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 22 in nomera:
            self.pushButton_y6_22.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 23 in nomera:
            self.pushButton_y6_23.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 24 in nomera:
            self.pushButton_y6_24.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 25 in nomera:
            self.pushButton_y6_25.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 26 in nomera:
            self.pushButton_y6_26.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 27 in nomera:
            self.pushButton_y6_27.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 28 in nomera:
            self.pushButton_y6_28.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 29 in nomera:
            self.pushButton_y6_29.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 30 in nomera:
            self.pushButton_y6_30.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 31 in nomera:
            self.pushButton_y6_31.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 32 in nomera:
            self.pushButton_y6_32.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 33 in nomera:
            self.pushButton_y6_33.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 34 in nomera:
            self.pushButton_y6_34.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 35 in nomera:
            self.pushButton_y6_35.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 36 in nomera:
            self.pushButton_y6_36.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 37 in nomera:
            self.pushButton_y6_37.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 38 in nomera:
            self.pushButton_y6_38.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 39 in nomera:
            self.pushButton_y6_39.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 40 in nomera:
            self.pushButton_y6_40.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 41 in nomera:
            self.pushButton_y6_41.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 42 in nomera:
            self.pushButton_y6_42.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 43 in nomera:
            self.pushButton_y6_43.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 44 in nomera:
            self.pushButton_y6_44.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 45 in nomera:
            self.pushButton_y6_45.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 46 in nomera:
            self.pushButton_y6_46.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 47 in nomera:
            self.pushButton_y6_47.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 48 in nomera:
            self.pushButton_y6_48.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')
        if 49 in nomera:
            self.pushButton_y6_49.setStyleSheet(
                'QPushButton {background-color: #A3C1DA; color: red; border-radius: 15px}')

        self.timer = QtCore.QTimer()
        self.timer.start(5000)
        self.timer.timeout.connect(self.rab_6)

    def rab_6(self):
        self.timer.stop()
        self.window = uroven_6_r()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def vosvrat(self):
        self.timer.stop()
        self.window = vyber_urovnya()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение


class uroven_4_r(QMainWindow, Ui_MainWindow_uroven_4):
    def __init__(self):
        global nomera, uroven
        uroven = 'u4'
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_vosvrat.clicked.connect(self.vosvrat)
        self.pushButton_y4_1.clicked.connect(self.puch_y4_1)
        self.pushButton_y4_2.clicked.connect(self.puch_y4_2)
        self.pushButton_y4_3.clicked.connect(self.puch_y4_3)
        self.pushButton_y4_4.clicked.connect(self.puch_y4_4)
        self.pushButton_y4_5.clicked.connect(self.puch_y4_5)
        self.pushButton_y4_6.clicked.connect(self.puch_y4_6)
        self.pushButton_y4_7.clicked.connect(self.puch_y4_7)
        self.pushButton_y4_8.clicked.connect(self.puch_y4_8)
        self.pushButton_y4_9.clicked.connect(self.puch_y4_9)
        self.pushButton_y4_10.clicked.connect(self.puch_y4_10)
        self.pushButton_y4_11.clicked.connect(self.puch_y4_11)
        self.pushButton_y4_12.clicked.connect(self.puch_y4_12)
        self.pushButton_y4_13.clicked.connect(self.puch_y4_13)
        self.pushButton_y4_14.clicked.connect(self.puch_y4_14)
        self.pushButton_y4_15.clicked.connect(self.puch_y4_15)
        self.pushButton_y4_16.clicked.connect(self.puch_y4_16)
        self.pushButton_y4_17.clicked.connect(self.puch_y4_17)
        self.pushButton_y4_18.clicked.connect(self.puch_y4_18)
        self.pushButton_y4_19.clicked.connect(self.puch_y4_19)
        self.pushButton_y4_20.clicked.connect(self.puch_y4_20)
        self.pushButton_y4_21.clicked.connect(self.puch_y4_21)
        self.pushButton_y4_22.clicked.connect(self.puch_y4_22)
        self.pushButton_y4_23.clicked.connect(self.puch_y4_23)
        self.pushButton_y4_24.clicked.connect(self.puch_y4_24)
        self.pushButton_y4_25.clicked.connect(self.puch_y4_25)

    def puch_y4_1(self):
        if 1 in nomera:
            self.pushButton_y4_1.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(1)]
        elif 1 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_2(self):
        if 2 in nomera:
            self.pushButton_y4_2.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(2)]
        elif 2 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_3(self):
        if 3 in nomera:
            self.pushButton_y4_3.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(3)]
        elif 3 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_4(self):
        if 4 in nomera:
            self.pushButton_y4_4.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(4)]
        elif 4 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_5(self):
        if 5 in nomera:
            self.pushButton_y4_5.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(5)]
        elif 5 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_6(self):
        if 6 in nomera:
            self.pushButton_y4_6.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(6)]
        elif 6 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_7(self):
        if 7 in nomera:
            self.pushButton_y4_7.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(7)]
        elif 7 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_8(self):
        if 8 in nomera:
            self.pushButton_y4_8.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(8)]
        elif 8 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_9(self):
        if 9 in nomera:
            self.pushButton_y4_9.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(9)]
        elif 9 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_10(self):
        if 10 in nomera:
            self.pushButton_y4_10.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(10)]
        elif 10 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_11(self):
        if 11 in nomera:
            self.pushButton_y4_11.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(11)]
        elif 11 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_12(self):
        if 12 in nomera:
            self.pushButton_y4_12.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(12)]
        elif 12 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_13(self):
        if 13 in nomera:
            self.pushButton_y4_13.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(13)]
        elif 13 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_14(self):
        if 14 in nomera:
            self.pushButton_y4_14.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(14)]
        elif 14 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_15(self):
        if 15 in nomera:
            self.pushButton_y4_15.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(15)]
        elif 15 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_16(self):
        if 16 in nomera:
            self.pushButton_y4_16.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(16)]
        elif 16 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_17(self):
        if 17 in nomera:
            self.pushButton_y4_17.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(17)]
        elif 17 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_18(self):
        if 18 in nomera:
            self.pushButton_y4_18.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(18)]
        elif 18 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_19(self):
        if 19 in nomera:
            self.pushButton_y4_19.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(19)]
        elif 19 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_20(self):
        if 20 in nomera:
            self.pushButton_y4_20.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(20)]
        elif 20 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_21(self):
        if 21 in nomera:
            self.pushButton_y4_21.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(21)]
        elif 21 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_22(self):
        if 22 in nomera:
            self.pushButton_y4_22.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(22)]
        elif 22 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_23(self):
        if 23 in nomera:
            self.pushButton_y4_23.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(23)]
        elif 23 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_24(self):
        if 24 in nomera:
            self.pushButton_y4_24.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(24)]
        elif 24 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def puch_y4_25(self):
        if 25 in nomera:
            self.pushButton_y4_25.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(25)]
        elif 25 not in nomera:
            self.proigrash_4()
        if len(nomera) == 0:
            self.perechod_u_5()

    def vosvrat(self):
        self.window = vyber_urovnya()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def perechod_u_5(self):
        self.window = uroven_6()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def proigrash_4(self):
        self.window = proigrash()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()


class uroven_5_r(QMainWindow, Ui_MainWindow_uroven_5):
    def __init__(self):
        global nomera, uroven
        uroven = 'u5'
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_vosvrat.clicked.connect(self.vosvrat)
        self.pushButton_y5_1.clicked.connect(self.puch_y5_1)
        self.pushButton_y5_2.clicked.connect(self.puch_y5_2)
        self.pushButton_y5_3.clicked.connect(self.puch_y5_3)
        self.pushButton_y5_4.clicked.connect(self.puch_y5_4)
        self.pushButton_y5_5.clicked.connect(self.puch_y5_5)
        self.pushButton_y5_6.clicked.connect(self.puch_y5_6)
        self.pushButton_y5_7.clicked.connect(self.puch_y5_7)
        self.pushButton_y5_8.clicked.connect(self.puch_y5_8)
        self.pushButton_y5_9.clicked.connect(self.puch_y5_9)
        self.pushButton_y5_10.clicked.connect(self.puch_y5_10)
        self.pushButton_y5_11.clicked.connect(self.puch_y5_11)
        self.pushButton_y5_12.clicked.connect(self.puch_y5_12)
        self.pushButton_y5_13.clicked.connect(self.puch_y5_13)
        self.pushButton_y5_14.clicked.connect(self.puch_y5_14)
        self.pushButton_y5_15.clicked.connect(self.puch_y5_15)
        self.pushButton_y5_16.clicked.connect(self.puch_y5_16)

        self.pushButton_y5_17.clicked.connect(self.puch_y5_17)
        self.pushButton_y5_18.clicked.connect(self.puch_y5_18)
        self.pushButton_y5_19.clicked.connect(self.puch_y5_19)
        self.pushButton_y5_20.clicked.connect(self.puch_y5_20)
        self.pushButton_y5_21.clicked.connect(self.puch_y5_21)
        self.pushButton_y5_22.clicked.connect(self.puch_y5_22)
        self.pushButton_y5_23.clicked.connect(self.puch_y5_23)
        self.pushButton_y5_24.clicked.connect(self.puch_y5_24)
        self.pushButton_y5_25.clicked.connect(self.puch_y5_25)
        self.pushButton_y5_26.clicked.connect(self.puch_y5_26)
        self.pushButton_y5_27.clicked.connect(self.puch_y5_27)
        self.pushButton_y5_28.clicked.connect(self.puch_y5_28)
        self.pushButton_y5_29.clicked.connect(self.puch_y5_29)
        self.pushButton_y5_30.clicked.connect(self.puch_y5_30)
        self.pushButton_y5_31.clicked.connect(self.puch_y5_31)
        self.pushButton_y5_32.clicked.connect(self.puch_y5_32)

        self.pushButton_y5_33.clicked.connect(self.puch_y5_33)
        self.pushButton_y5_34.clicked.connect(self.puch_y5_34)
        self.pushButton_y5_35.clicked.connect(self.puch_y5_35)
        self.pushButton_y5_36.clicked.connect(self.puch_y5_36)

    def puch_y5_1(self):
        if 1 in nomera:
            self.pushButton_y5_1.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(1)]
        elif 1 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_2(self):
        if 2 in nomera:
            self.pushButton_y5_2.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(2)]
        elif 2 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_3(self):
        if 3 in nomera:
            self.pushButton_y5_3.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(3)]
        elif 3 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_4(self):
        if 4 in nomera:
            self.pushButton_y5_4.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(4)]
        elif 4 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_5(self):
        if 5 in nomera:
            self.pushButton_y5_5.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(5)]
        elif 5 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_6(self):
        if 6 in nomera:
            self.pushButton_y5_6.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(6)]
        elif 6 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_7(self):
        if 7 in nomera:
            self.pushButton_y5_7.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(7)]
        elif 7 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_8(self):
        if 8 in nomera:
            self.pushButton_y5_8.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(8)]
        elif 8 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_9(self):
        if 9 in nomera:
            self.pushButton_y5_9.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(9)]
        elif 9 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_10(self):
        if 10 in nomera:
            self.pushButton_y5_10.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(10)]
        elif 10 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_11(self):
        if 11 in nomera:
            self.pushButton_y5_11.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(11)]
        elif 11 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_12(self):
        if 12 in nomera:
            self.pushButton_y5_12.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(12)]
        elif 12 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_13(self):
        if 13 in nomera:
            self.pushButton_y5_13.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(13)]
        elif 13 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_14(self):
        if 14 in nomera:
            self.pushButton_y5_14.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(14)]
        elif 14 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_15(self):
        if 15 in nomera:
            self.pushButton_y5_15.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(15)]
        elif 15 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_16(self):
        if 16 in nomera:
            self.pushButton_y5_16.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(16)]
        elif 16 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_17(self):
        if 17 in nomera:
            self.pushButton_y5_17.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(17)]
        elif 17 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_18(self):
        if 18 in nomera:
            self.pushButton_y5_18.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(18)]
        elif 18 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_19(self):
        if 19 in nomera:
            self.pushButton_y5_19.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(19)]
        elif 19 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_20(self):
        if 20 in nomera:
            self.pushButton_y5_20.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(20)]
        elif 20 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_21(self):
        if 21 in nomera:
            self.pushButton_y5_21.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(21)]
        elif 21 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_22(self):
        if 22 in nomera:
            self.pushButton_y5_22.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(22)]
        elif 22 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_23(self):
        if 23 in nomera:
            self.pushButton_y5_23.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(23)]
        elif 23 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_24(self):
        if 24 in nomera:
            self.pushButton_y5_24.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(24)]
        elif 24 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_25(self):
        if 25 in nomera:
            self.pushButton_y5_25.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(25)]
        elif 25 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_26(self):
        if 26 in nomera:
            self.pushButton_y5_26.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(26)]
        elif 26 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_27(self):
        if 27 in nomera:
            self.pushButton_y5_27.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(27)]
        elif 27 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_28(self):
        if 28 in nomera:
            self.pushButton_y5_28.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(28)]
        elif 28 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_29(self):
        if 29 in nomera:
            self.pushButton_y5_29.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(29)]
        elif 29 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_30(self):
        if 30 in nomera:
            self.pushButton_y5_30.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(30)]
        elif 30 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_31(self):
        if 31 in nomera:
            self.pushButton_y5_31.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(31)]
        elif 31 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_32(self):
        if 32 in nomera:
            self.pushButton_y5_32.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(32)]
        elif 32 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_33(self):
        if 33 in nomera:
            self.pushButton_y5_33.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(33)]
        elif 33 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_34(self):
        if 34 in nomera:
            self.pushButton_y5_34.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(34)]
        elif 34 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_35(self):
        if 35 in nomera:
            self.pushButton_y5_35.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(35)]
        elif 35 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y5_36(self):
        if 36 in nomera:
            self.pushButton_y5_36.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(36)]
        elif 36 not in nomera:
            self.proigrash_5()
        if len(nomera) == 0:
            self.perechod_u_6()

    def vosvrat(self):
        self.window = vyber_urovnya()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def perechod_u_6(self):
        self.window = uroven_6()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def proigrash_5(self):
        self.window = proigrash()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()


class uroven_6_r(QMainWindow, Ui_MainWindow_uroven_6):
    def __init__(self):
        global nomera, uroven
        uroven = 'u6'
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_vosvrat.clicked.connect(self.vosvrat)
        self.pushButton_y6_1.clicked.connect(self.puch_y6_1)
        self.pushButton_y6_2.clicked.connect(self.puch_y6_2)
        self.pushButton_y6_3.clicked.connect(self.puch_y6_3)
        self.pushButton_y6_4.clicked.connect(self.puch_y6_4)
        self.pushButton_y6_5.clicked.connect(self.puch_y6_5)
        self.pushButton_y6_6.clicked.connect(self.puch_y6_6)
        self.pushButton_y6_7.clicked.connect(self.puch_y6_7)
        self.pushButton_y6_8.clicked.connect(self.puch_y6_8)
        self.pushButton_y6_9.clicked.connect(self.puch_y6_9)
        self.pushButton_y6_10.clicked.connect(self.puch_y6_10)
        self.pushButton_y6_11.clicked.connect(self.puch_y6_11)
        self.pushButton_y6_12.clicked.connect(self.puch_y6_12)
        self.pushButton_y6_13.clicked.connect(self.puch_y6_13)
        self.pushButton_y6_14.clicked.connect(self.puch_y6_14)
        self.pushButton_y6_15.clicked.connect(self.puch_y6_15)
        self.pushButton_y6_16.clicked.connect(self.puch_y6_16)

        self.pushButton_y6_17.clicked.connect(self.puch_y6_17)
        self.pushButton_y6_18.clicked.connect(self.puch_y6_18)
        self.pushButton_y6_19.clicked.connect(self.puch_y6_19)
        self.pushButton_y6_20.clicked.connect(self.puch_y6_20)
        self.pushButton_y6_21.clicked.connect(self.puch_y6_21)
        self.pushButton_y6_22.clicked.connect(self.puch_y6_22)
        self.pushButton_y6_23.clicked.connect(self.puch_y6_23)
        self.pushButton_y6_24.clicked.connect(self.puch_y6_24)
        self.pushButton_y6_25.clicked.connect(self.puch_y6_25)
        self.pushButton_y6_26.clicked.connect(self.puch_y6_26)
        self.pushButton_y6_27.clicked.connect(self.puch_y6_27)
        self.pushButton_y6_28.clicked.connect(self.puch_y6_28)
        self.pushButton_y6_29.clicked.connect(self.puch_y6_29)
        self.pushButton_y6_30.clicked.connect(self.puch_y6_30)
        self.pushButton_y6_31.clicked.connect(self.puch_y6_31)
        self.pushButton_y6_32.clicked.connect(self.puch_y6_32)

        self.pushButton_y6_33.clicked.connect(self.puch_y6_33)
        self.pushButton_y6_34.clicked.connect(self.puch_y6_34)
        self.pushButton_y6_35.clicked.connect(self.puch_y6_35)
        self.pushButton_y6_36.clicked.connect(self.puch_y6_36)
        self.pushButton_y6_37.clicked.connect(self.puch_y6_37)
        self.pushButton_y6_38.clicked.connect(self.puch_y6_38)
        self.pushButton_y6_39.clicked.connect(self.puch_y6_39)
        self.pushButton_y6_40.clicked.connect(self.puch_y6_40)
        self.pushButton_y6_41.clicked.connect(self.puch_y6_41)
        self.pushButton_y6_42.clicked.connect(self.puch_y6_42)
        self.pushButton_y6_43.clicked.connect(self.puch_y6_43)
        self.pushButton_y6_44.clicked.connect(self.puch_y6_44)
        self.pushButton_y6_45.clicked.connect(self.puch_y6_45)
        self.pushButton_y6_46.clicked.connect(self.puch_y6_46)
        self.pushButton_y6_47.clicked.connect(self.puch_y6_47)
        self.pushButton_y6_48.clicked.connect(self.puch_y6_48)
        self.pushButton_y6_49.clicked.connect(self.puch_y6_49)

    def puch_y6_1(self):
        if 1 in nomera:
            self.pushButton_y6_1.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(1)]
        elif 1 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_2(self):
        if 2 in nomera:
            self.pushButton_y6_2.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(2)]
        elif 2 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_3(self):
        if 3 in nomera:
            self.pushButton_y6_3.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(3)]
        elif 3 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_4(self):
        if 4 in nomera:
            self.pushButton_y6_4.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(4)]
        elif 4 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_5(self):
        if 5 in nomera:
            self.pushButton_y6_5.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(5)]
        elif 5 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_6(self):
        if 6 in nomera:
            self.pushButton_y6_6.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(6)]
        elif 6 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_7(self):
        if 7 in nomera:
            self.pushButton_y6_7.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(7)]
        elif 7 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_8(self):
        if 8 in nomera:
            self.pushButton_y6_8.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(8)]
        elif 8 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_9(self):
        if 9 in nomera:
            self.pushButton_y6_9.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(9)]
        elif 9 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_10(self):
        if 10 in nomera:
            self.pushButton_y6_10.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(10)]
        elif 10 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_11(self):
        if 11 in nomera:
            self.pushButton_y6_11.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(11)]
        elif 11 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_12(self):
        if 12 in nomera:
            self.pushButton_y6_12.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(12)]
        elif 12 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_13(self):
        if 13 in nomera:
            self.pushButton_y6_13.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(13)]
        elif 13 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_14(self):
        if 14 in nomera:
            self.pushButton_y6_14.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(14)]
        elif 14 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_15(self):
        if 15 in nomera:
            self.pushButton_y6_15.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(15)]
        elif 15 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_16(self):
        if 16 in nomera:
            self.pushButton_y6_16.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(16)]
        elif 16 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_17(self):
        if 17 in nomera:
            self.pushButton_y6_17.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(17)]
        elif 17 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_18(self):
        if 18 in nomera:
            self.pushButton_y6_18.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(18)]
        elif 18 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_19(self):
        if 19 in nomera:
            self.pushButton_y6_19.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(19)]
        elif 19 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_20(self):
        if 20 in nomera:
            self.pushButton_y6_20.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(20)]
        elif 20 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_21(self):
        if 21 in nomera:
            self.pushButton_y6_21.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(21)]
        elif 21 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_22(self):
        if 22 in nomera:
            self.pushButton_y6_22.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(22)]
        elif 22 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_23(self):
        if 23 in nomera:
            self.pushButton_y6_23.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(23)]
        elif 23 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_24(self):
        if 24 in nomera:
            self.pushButton_y6_24.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(24)]
        elif 24 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_25(self):
        if 25 in nomera:
            self.pushButton_y6_25.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(25)]
        elif 25 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_26(self):
        if 26 in nomera:
            self.pushButton_y6_26.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(26)]
        elif 26 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_27(self):
        if 27 in nomera:
            self.pushButton_y6_27.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(27)]
        elif 27 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_28(self):
        if 28 in nomera:
            self.pushButton_y6_28.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(28)]
        elif 28 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_29(self):
        if 29 in nomera:
            self.pushButton_y6_29.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(29)]
        elif 29 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_30(self):
        if 30 in nomera:
            self.pushButton_y6_30.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(30)]
        elif 30 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_31(self):
        if 31 in nomera:
            self.pushButton_y6_31.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(31)]
        elif 31 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_32(self):
        if 32 in nomera:
            self.pushButton_y6_32.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(32)]
        elif 32 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_33(self):
        if 33 in nomera:
            self.pushButton_y6_33.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(33)]
        elif 33 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_34(self):
        if 34 in nomera:
            self.pushButton_y6_34.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(34)]
        elif 34 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_35(self):
        if 35 in nomera:
            self.pushButton_y6_35.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(35)]
        elif 35 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_36(self):
        if 36 in nomera:
            self.pushButton_y6_36.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(36)]
        elif 36 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_37(self):
        if 37 in nomera:
            self.pushButton_y6_37.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(37)]
        elif 37 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_38(self):
        if 38 in nomera:
            self.pushButton_y6_38.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(38)]
        elif 38 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_39(self):
        if 39 in nomera:
            self.pushButton_y6_39.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(39)]
        elif 39 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_40(self):
        if 40 in nomera:
            self.pushButton_y6_40.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(40)]
        elif 40 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_41(self):
        if 41 in nomera:
            self.pushButton_y6_41.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(41)]
        elif 41 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_42(self):
        if 42 in nomera:
            self.pushButton_y6_42.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(42)]
        elif 42 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_43(self):
        if 43 in nomera:
            self.pushButton_y6_43.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(43)]
        elif 43 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_44(self):
        if 44 in nomera:
            self.pushButton_y6_44.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(44)]
        elif 44 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_45(self):
        if 45 in nomera:
            self.pushButton_y6_45.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(45)]
        elif 45 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_46(self):
        if 46 in nomera:
            self.pushButton_y6_46.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(46)]
        elif 46 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_47(self):
        if 47 in nomera:
            self.pushButton_y6_47.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(47)]
        elif 47 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_48(self):
        if 48 in nomera:
            self.pushButton_y6_48.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(48)]
        elif 48 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def puch_y6_49(self):
        if 49 in nomera:
            self.pushButton_y6_49.setStyleSheet(
                'QPushButton {background-color: #800080; color: red; border-radius: 15px}')
            del nomera[nomera.index(49)]
        elif 49 not in nomera:
            self.proigrash_6()
        if len(nomera) == 0:
            self.perechod_u_6()

    def perechod_u_6(self):
        self.window = pobeda()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def vosvrat(self):
        self.window = vyber_urovnya()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение

    def proigrash_6(self):
        self.window = proigrash()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()


class pobeda(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 250, 200, 200)
        self.setWindowTitle("Выйгрыш!")
        self.setWindowIcon(QtGui.QIcon('иконка.png'))

        self.btn = QPushButton('Вы выйграли!\nПоздравляем у Вас отличная память!', self)
        self.btn.setStyleSheet('QPushButton {background-color: #9CEE90;}')
        self.btn.resize(200, 200)

        self.btn.clicked.connect(self.pereshod)

    def pereshod(self):
        self.window = vyber_urovnya()  # Создаём объект класса ExampleApp
        self.window.show()
        self.close()  # и запускаем приложение


def main():
    app = QApplication(sys.argv)  # Новый экземпляр QApplication
    window = opening()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окн
    sys.exit(app.exec_())  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
