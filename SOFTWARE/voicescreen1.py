# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import pyglet
from gtts import gTTS
import os
import time

#Pantalla Inicio
class Ui_Inicio(object):
    def setupUi(self, Inicio):
        Inicio.setObjectName("Inicio")
        Inicio.resize(1122, 700)
        Inicio.setMaximumSize(QtCore.QSize(1122, 16777215))
        Inicio.setStyleSheet("background-color: rgb(71, 72, 72);")
        self.label = QtWidgets.QLabel(Inicio)
        self.label.setGeometry(QtCore.QRect(690, 120, 275, 206))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Inicio)
        self.label_2.setGeometry(QtCore.QRect(330, 490, 151, 181))
        self.label_2.setStyleSheet("border-image: url(:/cct/human.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(Inicio)
        self.line_2.setGeometry(QtCore.QRect(490, 570, 631, 81))
        self.line_2.setMidLineWidth(44)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Inicio)
        self.line_3.setGeometry(QtCore.QRect(0, 570, 331, 81))
        self.line_3.setMidLineWidth(44)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_3 = QtWidgets.QLabel(Inicio)
        self.label_3.setGeometry(QtCore.QRect(130, 70, 481, 421))
        self.label_3.setStyleSheet("border-image: url(:/cct/logo.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Inicio)
        self.pushButton.setGeometry(QtCore.QRect(670, 430, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 157, 0);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Inicio)
        QtCore.QMetaObject.connectSlotsByName(Inicio)
        self.pushButton.clicked.connect(self.menu)

    def retranslateUi(self, Inicio):
        _translate = QtCore.QCoreApplication.translate
        Inicio.setWindowTitle(_translate("Inicio", "Form"))
        self.label.setText(_translate("Inicio", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#e7e7e7;\">Voice</span></p><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#e7e7e7;\">Screen</span></p></body></html>"))
        self.pushButton.setText(_translate("Inicio", "Iniciar"))


    def menu(self):
        click = pyglet.media.load("click.mp3", streaming=False)
        click.play()
        time.sleep(1)
        self.menu = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.menu)
        self.menu.show()
import human_rc

#menu de opciones
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1122, 720)
        MainWindow.setMaximumSize(QtCore.QSize(1122, 16777215))
        MainWindow.setStyleSheet("background-color: rgb(71, 72, 72);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.informacion = QtWidgets.QPushButton(self.centralwidget)
        self.informacion.setGeometry(QtCore.QRect(40, 20, 321, 301))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.informacion.setFont(font)
        self.informacion.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.informacion.setStyleSheet("QPushButton{\n"
"background-color: rgb(234, 201, 158);\n"
"border-radius: 30px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n")
        self.informacion.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("venv/qtdesigner/information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.informacion.setIcon(icon)
        self.informacion.setIconSize(QtCore.QSize(167, 172))
        self.informacion.setObjectName("informacion")
        self.Frases = QtWidgets.QPushButton(self.centralwidget)
        self.Frases.setGeometry(QtCore.QRect(400, 20, 321, 301))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Frases.setFont(font)
        self.Frases.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.Frases.setStyleSheet("QPushButton{\n"
"background-color: rgb(234, 201, 158);\n"
"border-radius: 30px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n")
        self.Frases.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("venv/qtdesigner/happy (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Frases.setIcon(icon1)
        self.Frases.setIconSize(QtCore.QSize(167, 172))
        self.Frases.setObjectName("Frases")
        self.Alerta = QtWidgets.QPushButton(self.centralwidget)
        self.Alerta.setGeometry(QtCore.QRect(750, 210, 321, 301))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Alerta.setFont(font)
        self.Alerta.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.Alerta.setStyleSheet("QPushButton{\n"
"background-color: rgb(234, 201, 158);\n"
"border-radius: 30px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n")
        self.Alerta.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("venv/qtdesigner/warning.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Alerta.setIcon(icon2)
        self.Alerta.setIconSize(QtCore.QSize(167, 172))
        self.Alerta.setObjectName("Alerta")
        self.Teclado = QtWidgets.QPushButton(self.centralwidget)
        self.Teclado.setGeometry(QtCore.QRect(220, 340, 321, 301))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Teclado.setFont(font)
        self.Teclado.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.Teclado.setStyleSheet("QPushButton{\n"
"background-color: rgb(234, 201, 158);\n"
"border-radius: 30px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n")
        self.Teclado.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("venv/qtdesigner/smart-keyboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Teclado.setIcon(icon3)
        self.Teclado.setIconSize(QtCore.QSize(167, 172))
        self.Teclado.setObjectName("Teclado")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.Teclado.clicked.connect(self.teclado)
        self.Frases.clicked.connect(self.frases)
        self.informacion.clicked.connect(self.Info)
        self.Alerta.clicked.connect(self.alerta)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def teclado(self):
        click = pyglet.media.load("click.mp3", streaming=False)
        click.play()
        time.sleep(1)
        self.teclado = QtWidgets.QMainWindow()
        self.ui = Ui_Teclado()
        self.ui.setupUi(self.teclado)
        self.teclado.show()
    def frases(self):
        click = pyglet.media.load("click.mp3", streaming=False)
        click.play()
        time.sleep(1)
        self.frases = QtWidgets.QMainWindow()
        self.ui = Ui_Frases()
        self.ui.setupUi(self.frases)
        self.frases.show()

    def Info(self):
        click = pyglet.media.load("click.mp3", streaming=False)
        click.play()
        time.sleep(1)
        self.Info = QtWidgets.QMainWindow()
        self.ui = Ui_Informacion()
        self.ui.setupUi(self.Info)
        self.Info.show()

    def alerta(self):
        click = pyglet.media.load("alerta.mp3", streaming=False)
        click.play()
        time.sleep(1)

#Pantalla frases
class Ui_Frases(object):
    def setupUi(self, Frases):
        Frases.setObjectName("Frases")
        Frases.resize(1122, 720)
        Frases.setStyleSheet("background-color: rgb(71, 72, 72);")
        self.push_thambre = QtWidgets.QPushButton(Frases)
        self.push_thambre.setGeometry(QtCore.QRect(100, 50, 251, 71))
        font = QtGui.QFont()
        font.setFamily("HP Simplified Jpan")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_thambre.setFont(font)
        self.push_thambre.setStyleSheet("QPushButton{\n"
"font: 16pt \"HP Simplified Jpan\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(234, 201, 158);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(127, 88, 21);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.push_thambre.setObjectName("push_thambre")
        self.push_casa = QtWidgets.QPushButton(Frases)
        self.push_casa.setGeometry(QtCore.QRect(520, 610, 71, 71))
        self.push_casa.setStyleSheet("QPushButton{\n"
"background-color: rgb(234, 201, 158);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(127, 88, 21);\n"
"}")
        self.push_casa.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("venv/qtdesigner/house.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.push_casa.setIcon(icon)
        self.push_casa.setIconSize(QtCore.QSize(52, 47))
        self.push_casa.setObjectName("push_casa")
        self.push_tsed = QtWidgets.QPushButton(Frases)
        self.push_tsed.setGeometry(QtCore.QRect(100, 140, 251, 71))
        font = QtGui.QFont()
        font.setFamily("HP Simplified Jpan")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_tsed.setFont(font)
        self.push_tsed.setStyleSheet("QPushButton{\n"
"font: 16pt \"HP Simplified Jpan\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(234, 201, 158);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(127, 88, 21);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.push_tsed.setObjectName("push_tsed")
        self.push_tfrio = QtWidgets.QPushButton(Frases)
        self.push_tfrio.setGeometry(QtCore.QRect(100, 230, 251, 71))
        font = QtGui.QFont()
        font.setFamily("HP Simplified Jpan")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_tfrio.setFont(font)
        self.push_tfrio.setStyleSheet("QPushButton{\n"
"font: 16pt \"HP Simplified Jpan\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(234, 201, 158);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(127, 88, 21);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.push_tfrio.setObjectName("push_tfrio")
        self.push_tcalor = QtWidgets.QPushButton(Frases)
        self.push_tcalor.setGeometry(QtCore.QRect(100, 320, 251, 71))
        font = QtGui.QFont()
        font.setFamily("HP Simplified Jpan")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_tcalor.setFont(font)
        self.push_tcalor.setStyleSheet("QPushButton{\n"
"font: 16pt \"HP Simplified Jpan\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(234, 201, 158);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(127, 88, 21);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.push_tcalor.setObjectName("push_tcalor")
        self.push_tmiedo = QtWidgets.QPushButton(Frases)
        self.push_tmiedo.setGeometry(QtCore.QRect(100, 410, 251, 71))
        font = QtGui.QFont()
        font.setFamily("HP Simplified Jpan")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_tmiedo.setFont(font)
        self.push_tmiedo.setStyleSheet("QPushButton{\n"
"font: 16pt \"HP Simplified Jpan\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(234, 201, 158);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(127, 88, 21);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.push_tmiedo.setObjectName("push_tmiedo")
        self.push_tsueno = QtWidgets.QPushButton(Frases)
        self.push_tsueno.setGeometry(QtCore.QRect(100, 500, 251, 71))
        font = QtGui.QFont()
        font.setFamily("HP Simplified Jpan")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_tsueno.setFont(font)
        self.push_tsueno.setStyleSheet("QPushButton{\n"
"font: 16pt \"HP Simplified Jpan\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(234, 201, 158);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(127, 88, 21);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.push_tsueno.setObjectName("push_tsueno")
        self.push_efeliz = QtWidgets.QPushButton(Frases)
        self.push_efeliz.setGeometry(QtCore.QRect(440, 50, 251, 71))
        font = QtGui.QFont()
        font.setFamily("HP Simplified Jpan")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_efeliz.setFont(font)
        self.push_efeliz.setStyleSheet("QPushButton{\n"
"font: 16pt \"HP Simplified Jpan\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(234, 201, 158);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(127, 88, 21);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.push_efeliz.setObjectName("push_efeliz")
        self.push_eemocionado = QtWidgets.QPushButton(Frases)
        self.push_eemocionado.setGeometry(QtCore.QRect(440, 140, 251, 71))
        font = QtGui.QFont()
        font.setFamily("HP Simplified Jpan")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_eemocionado.setFont(font)
        self.push_eemocionado.setStyleSheet("QPushButton{\n"
"font: 16pt \"HP Simplified Jpan\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(234, 201, 158);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(127, 88, 21);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.push_eemocionado.setObjectName("push_eemocionado")
        self.push_etriste = QtWidgets.QPushButton(Frases)
        self.push_etriste.setGeometry(QtCore.QRect(440, 320, 251, 71))
        font = QtGui.QFont()
        font.setFamily("HP Simplified Jpan")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_etriste.setFont(font)
        self.push_etriste.setStyleSheet("QPushButton{\n"
"font: 16pt \"HP Simplified Jpan\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(234, 201, 158);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(127, 88, 21);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.push_etriste.setObjectName("push_etriste")
        self.push_esorprendido = QtWidgets.QPushButton(Frases)
        self.push_esorprendido.setGeometry(QtCore.QRect(440, 410, 251, 71))
        font = QtGui.QFont()
        font.setFamily("HP Simplified Jpan")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_esorprendido.setFont(font)
        self.push_esorprendido.setStyleSheet("QPushButton{\n"
"font: 16pt \"HP Simplified Jpan\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(234, 201, 158);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(127, 88, 21);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.push_esorprendido.setObjectName("push_esorprendido")
        self.push_eenojado = QtWidgets.QPushButton(Frases)
        self.push_eenojado.setGeometry(QtCore.QRect(440, 500, 251, 71))
        font = QtGui.QFont()
        font.setFamily("HP Simplified Jpan")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_eenojado.setFont(font)
        self.push_eenojado.setStyleSheet("QPushButton{\n"
"font: 16pt \"HP Simplified Jpan\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(234, 201, 158);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(127, 88, 21);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.push_eenojado.setObjectName("push_eenojado")
        self.push_eaburrido = QtWidgets.QPushButton(Frases)
        self.push_eaburrido.setGeometry(QtCore.QRect(440, 230, 251, 71))
        font = QtGui.QFont()
        font.setFamily("HP Simplified Jpan")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_eaburrido.setFont(font)
        self.push_eaburrido.setStyleSheet("QPushButton{\n"
"font: 16pt \"HP Simplified Jpan\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(234, 201, 158);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(127, 88, 21);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.push_eaburrido.setObjectName("push_eaburrido")
        self.push_spotify = QtWidgets.QPushButton(Frases)
        self.push_spotify.setGeometry(QtCore.QRect(790, 230, 251, 71))
        font = QtGui.QFont()
        font.setFamily("HP Simplified Jpan")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_spotify.setFont(font)
        self.push_spotify.setStyleSheet("QPushButton{\n"
"font: 14pt \"HP Simplified Jpan\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(234, 201, 158);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(127, 88, 21);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.push_spotify.setObjectName("push_spotify")
        self.push_siri = QtWidgets.QPushButton(Frases)
        self.push_siri.setGeometry(QtCore.QRect(790, 50, 251, 71))
        font = QtGui.QFont()
        font.setFamily("HP Simplified Jpan")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_siri.setFont(font)
        self.push_siri.setStyleSheet("QPushButton{\n"
"font: 16pt \"HP Simplified Jpan\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(234, 201, 158);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(127, 88, 21);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.push_siri.setObjectName("push_siri")
        self.push_google = QtWidgets.QPushButton(Frases)
        self.push_google.setGeometry(QtCore.QRect(790, 140, 251, 71))
        font = QtGui.QFont()
        font.setFamily("HP Simplified Jpan")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_google.setFont(font)
        self.push_google.setStyleSheet("QPushButton{\n"
"font: 16pt \"HP Simplified Jpan\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(234, 201, 158);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(127, 88, 21);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.push_google.setObjectName("push_google")
        self.push_youtube = QtWidgets.QPushButton(Frases)
        self.push_youtube.setGeometry(QtCore.QRect(790, 320, 251, 71))
        font = QtGui.QFont()
        font.setFamily("HP Simplified Jpan")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_youtube.setFont(font)
        self.push_youtube.setStyleSheet("QPushButton{\n"
"font: 14pt \"HP Simplified Jpan\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(234, 201, 158);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(127, 88, 21);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.push_youtube.setObjectName("push_youtube")

        self.retranslateUi(Frases)
        QtCore.QMetaObject.connectSlotsByName(Frases)
        self.push_thambre.clicked.connect(self.method_thambre)
        self.push_tsueno.clicked.connect(self.method_tsueno)
        self.push_tcalor.clicked.connect(self.method_tcalor)
        self.push_tmiedo.clicked.connect(self.method_tmiedo)
        self.push_tsed.clicked.connect(self.method_tsed)
        self.push_tfrio.clicked.connect(self.method_tfrio)
        self.push_efeliz.clicked.connect(self.method_efeliz)
        self.push_etriste.clicked.connect(self.method_etriste)
        self.push_eenojado.clicked.connect(self.method_eenojado)
        self.push_eaburrido.clicked.connect(self.method_eaburrido)
        self.push_esorprendido.clicked.connect(self.method_esorprendido)
        self.push_siri.clicked.connect(self.method_siri)
        self.push_google.clicked.connect(self.method_google)
        self.push_eemocionado.clicked.connect(self.method_eemocionado)
        self.push_casa.clicked.connect(self.method_casa)

    def method_thambre(self):
            thambre = pyglet.media.load("tengohambre.mp3", streaming=False)
            thambre.play()
            time.sleep(1)

    def method_siri(self):
            siri = pyglet.media.load("oyesiri.mp3", streaming=False)
            siri.play()
            time.sleep(1)

    def method_google(self):
            google = pyglet.media.load("okgoogle.mp3", streaming=False)
            google.play()
            time.sleep(1)

    def method_tsed(self):
            tsed = pyglet.media.load("tengosed.mp3", streaming=False)
            tsed.play()
            time.sleep(1)

    def method_tfrio(self):
            tfrio = pyglet.media.load("tengofrio.mp3", streaming=False)
            tfrio.play()
            time.sleep(1)

    def method_eaburrido(self):
            eaburrido = pyglet.media.load("estoyaburrido.mp3", streaming=False)
            eaburrido.play()
            time.sleep(1)

    def method_efeliz(self):
            efeliz = pyglet.media.load("estoyfeliz.mp3", streaming=False)
            efeliz.play()
            time.sleep(1)

    def method_eemocionado(self):
            emocionado = pyglet.media.load("estoyemocionado.mp3", streaming=False)
            emocionado.play()
            time.sleep(1)

    def method_casa(self):
            click = pyglet.media.load("click.mp3", streaming=False)
            click.play()
            time.sleep(1)
            self.method_casa = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.method_casa)
            self.method_casa.show()

    def method_tsueno(self):
        sueno = pyglet.media.load("tengosueno.mp3", streaming=False)
        sueno.play()
        time.sleep(1)

    def method_tcalor(self):
        calor = pyglet.media.load("tengocalor.mp3", streaming=False)
        calor.play()
        time.sleep(1)

    def method_tmiedo(self):
        miedo = pyglet.media.load("tengomiedo.mp3", streaming=False)
        miedo.play()
        time.sleep(1)

    def method_etriste(self):
        triste = pyglet.media.load("estoytriste.mp3", streaming=False)
        triste.play()
        time.sleep(1)

    def method_eenojado(self):
        enojado = pyglet.media.load("estoyenojado.mp3", streaming=False)
        enojado.play()
        time.sleep(1)

    def method_esorprendido(self):
        sorprendido = pyglet.media.load("estoysorprendido.mp3", streaming=False)
        sorprendido.play()
        time.sleep(1)

    def retranslateUi(self, Frases):
        _translate = QtCore.QCoreApplication.translate
        Frases.setWindowTitle(_translate("Frases", "Frases predeterminadas"))
        self.push_thambre.setText(_translate("Frases", "Tengo hambre"))
        self.push_tsed.setText(_translate("Frases", "Tengo sed"))
        self.push_tfrio.setText(_translate("Frases", "Tengo frio"))
        self.push_tcalor.setText(_translate("Frases", "Tengo calor"))
        self.push_tmiedo.setText(_translate("Frases", "Tengo miedo"))
        self.push_tsueno.setText(_translate("Frases", "Tengo sue??o"))
        self.push_efeliz.setText(_translate("Frases", "Estoy feliz"))
        self.push_eemocionado.setText(_translate("Frases", "Estoy emocionado"))
        self.push_etriste.setText(_translate("Frases", "Estoy triste"))
        self.push_esorprendido.setText(_translate("Frases", "Estoy sorprendido"))
        self.push_eenojado.setText(_translate("Frases", "Estoy enojado"))
        self.push_eaburrido.setText(_translate("Frases", "Estoy aburrido"))
        self.push_spotify.setText(_translate("Frases", "Reproduce en Spotify ..."))
        self.push_siri.setText(_translate("Frases", "Oye Siri,"))
        self.push_google.setText(_translate("Frases", "OK Google"))
        self.push_youtube.setText(_translate("Frases", "Reproduce en Youtube ..."))


#Pantalla teclado
class Ui_Teclado(object):
    def setupUi(self, Teclado):
        Teclado.setObjectName("Teclado")
        Teclado.resize(1122, 720)
        Teclado.setStyleSheet("background-color: rgb(71, 72, 72);")
        self.push_Q = QtWidgets.QPushButton(Teclado)
        self.push_Q.setGeometry(QtCore.QRect(30, 280, 71, 71))
        self.push_Q.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_Q.setObjectName("push_Q")
        self.label = QtWidgets.QLabel(Teclado)
        self.label.setGeometry(QtCore.QRect(40, 80, 1041, 161))
        font = QtGui.QFont()
        font.setFamily("HP Simplified Jpan")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(211, 211, 211);\n"
                                 "border-radius:15px\n"
                                 "")
        self.label.setText("")
        self.label.setObjectName("label")
        self.push_W = QtWidgets.QPushButton(Teclado)
        self.push_W.setGeometry(QtCore.QRect(120, 280, 71, 71))
        self.push_W.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_W.setObjectName("push_W")
        self.push_E = QtWidgets.QPushButton(Teclado)
        self.push_E.setGeometry(QtCore.QRect(210, 280, 71, 71))
        self.push_E.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_E.setObjectName("push_E")
        self.push_R = QtWidgets.QPushButton(Teclado)
        self.push_R.setGeometry(QtCore.QRect(300, 280, 71, 71))
        self.push_R.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_R.setObjectName("push_R")
        self.push_T = QtWidgets.QPushButton(Teclado)
        self.push_T.setGeometry(QtCore.QRect(390, 280, 71, 71))
        self.push_T.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_T.setObjectName("push_T")
        self.push_Y = QtWidgets.QPushButton(Teclado)
        self.push_Y.setGeometry(QtCore.QRect(480, 280, 71, 71))
        self.push_Y.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_Y.setObjectName("push_Y")
        self.push_U = QtWidgets.QPushButton(Teclado)
        self.push_U.setGeometry(QtCore.QRect(570, 280, 71, 71))
        self.push_U.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_U.setObjectName("push_U")
        self.push_I = QtWidgets.QPushButton(Teclado)
        self.push_I.setGeometry(QtCore.QRect(660, 280, 71, 71))
        self.push_I.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_I.setObjectName("push_I")
        self.push_O = QtWidgets.QPushButton(Teclado)
        self.push_O.setGeometry(QtCore.QRect(750, 280, 71, 71))
        self.push_O.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_O.setObjectName("push_O")
        self.push_P = QtWidgets.QPushButton(Teclado)
        self.push_P.setGeometry(QtCore.QRect(840, 280, 71, 71))
        self.push_P.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_P.setObjectName("push_P")
        self.push_J = QtWidgets.QPushButton(Teclado)
        self.push_J.setGeometry(QtCore.QRect(570, 380, 71, 71))
        self.push_J.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_J.setObjectName("push_J")
        self.push_D = QtWidgets.QPushButton(Teclado)
        self.push_D.setGeometry(QtCore.QRect(210, 380, 71, 71))
        self.push_D.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_D.setObjectName("push_D")
        self.push_F = QtWidgets.QPushButton(Teclado)
        self.push_F.setGeometry(QtCore.QRect(300, 380, 71, 71))
        self.push_F.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_F.setObjectName("push_F")
        self.push_A = QtWidgets.QPushButton(Teclado)
        self.push_A.setGeometry(QtCore.QRect(30, 380, 71, 71))
        self.push_A.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_A.setObjectName("push_A")
        self.push_S = QtWidgets.QPushButton(Teclado)
        self.push_S.setGeometry(QtCore.QRect(120, 380, 71, 71))
        self.push_S.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_S.setObjectName("push_S")
        self.push_K = QtWidgets.QPushButton(Teclado)
        self.push_K.setGeometry(QtCore.QRect(660, 380, 71, 71))
        self.push_K.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_K.setObjectName("push_K")
        self.push_NN = QtWidgets.QPushButton(Teclado)
        self.push_NN.setGeometry(QtCore.QRect(840, 380, 71, 71))
        self.push_NN.setStyleSheet("QPushButton{\n"
                                   "font: 24pt \"HP Simplified Jpan\";\n"
                                   "    color: rgb(0, 0, 0);\n"
                                   "    background-color: rgb(234, 201, 158);\n"
                                   "border-radius: 15px\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover{\n"
                                   "color: rgb(0, 0, 0);\n"
                                   "    background-color: rgb(255, 255, 255);\n"
                                   "}\n"
                                   "\n"
                                   "QPushBotton{\n"
                                   "background-color: rgb(127, 88, 21);\n"
                                   "    color: rgb(255, 255, 255);\n"
                                   "}")
        self.push_NN.setObjectName("push_NN")
        self.push_G = QtWidgets.QPushButton(Teclado)
        self.push_G.setGeometry(QtCore.QRect(390, 380, 71, 71))
        self.push_G.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_G.setObjectName("push_G")
        self.push_H = QtWidgets.QPushButton(Teclado)
        self.push_H.setGeometry(QtCore.QRect(480, 380, 71, 71))
        self.push_H.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_H.setObjectName("push_H")
        self.push_L = QtWidgets.QPushButton(Teclado)
        self.push_L.setGeometry(QtCore.QRect(750, 380, 71, 71))
        self.push_L.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_L.setObjectName("push_L")
        self.push_M = QtWidgets.QPushButton(Teclado)
        self.push_M.setGeometry(QtCore.QRect(570, 480, 71, 71))
        self.push_M.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_M.setObjectName("push_M")
        self.push_V = QtWidgets.QPushButton(Teclado)
        self.push_V.setGeometry(QtCore.QRect(300, 480, 71, 71))
        self.push_V.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_V.setObjectName("push_V")
        self.push_espacio = QtWidgets.QPushButton(Teclado)
        self.push_espacio.setGeometry(QtCore.QRect(660, 480, 251, 71))
        self.push_espacio.setStyleSheet("QPushButton{\n"
                                        "font: 24pt \"HP Simplified Jpan\";\n"
                                        "    color: rgb(0, 0, 0);\n"
                                        "    background-color: rgb(234, 201, 158);\n"
                                        "border-radius: 15px\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushBotton{\n"
                                        "background-color: rgb(127, 88, 21);\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}")
        self.push_espacio.setText("")
        self.push_espacio.setObjectName("push_espacio")
        self.push_B = QtWidgets.QPushButton(Teclado)
        self.push_B.setGeometry(QtCore.QRect(390, 480, 71, 71))
        self.push_B.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_B.setObjectName("push_B")
        self.push_X = QtWidgets.QPushButton(Teclado)
        self.push_X.setGeometry(QtCore.QRect(120, 480, 71, 71))
        self.push_X.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_X.setObjectName("push_X")
        self.push_Z = QtWidgets.QPushButton(Teclado)
        self.push_Z.setGeometry(QtCore.QRect(30, 480, 71, 71))
        self.push_Z.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_Z.setObjectName("push_Z")
        self.push_N = QtWidgets.QPushButton(Teclado)
        self.push_N.setGeometry(QtCore.QRect(480, 480, 71, 71))
        self.push_N.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_N.setObjectName("push_N")
        self.push_C = QtWidgets.QPushButton(Teclado)
        self.push_C.setGeometry(QtCore.QRect(210, 480, 71, 71))
        self.push_C.setStyleSheet("QPushButton{\n"
                                  "font: 24pt \"HP Simplified Jpan\";\n"
                                  "    color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(234, 201, 158);\n"
                                  "border-radius: 15px\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover{\n"
                                  "color: rgb(0, 0, 0);\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushBotton{\n"
                                  "background-color: rgb(127, 88, 21);\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "}")
        self.push_C.setObjectName("push_C")
        self.push_borrar = QtWidgets.QPushButton(Teclado)
        self.push_borrar.setGeometry(QtCore.QRect(930, 280, 81, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_borrar.sizePolicy().hasHeightForWidth())
        self.push_borrar.setSizePolicy(sizePolicy)
        self.push_borrar.setStyleSheet("QPushButton{\n"
                                       "background-color: rgb(234, 201, 158);\n"
                                       "border-radius: 15px\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "background-color: rgb(255, 255, 255);\n"
                                       "}\n"
                                       "\n"
                                       "QPushBotton{\n"
                                       "background-color: rgb(127, 88, 21);\n"
                                       "}")
        self.push_borrar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("venv/qtdesigner/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.push_borrar.setIcon(icon)
        self.push_borrar.setIconSize(QtCore.QSize(75, 51))
        self.push_borrar.setObjectName("push_borrar")
        self.push_audio = QtWidgets.QPushButton(Teclado)
        self.push_audio.setGeometry(QtCore.QRect(930, 377, 171, 171))
        self.push_audio.setStyleSheet("QPushButton{\n"
                                      "background-color: rgb(234, 201, 158);\n"
                                      "border-radius: 15px\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "\n"
                                      "QPushBotton{\n"
                                      "background-color: rgb(127, 88, 21);\n"
                                      "}")
        self.push_audio.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("venv/qtdesigner/audio-speaker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.push_audio.setIcon(icon1)
        self.push_audio.setIconSize(QtCore.QSize(81, 82))
        self.push_audio.setObjectName("push_audio")
        self.push_casa = QtWidgets.QPushButton(Teclado)
        self.push_casa.setGeometry(QtCore.QRect(540, 600, 71, 71))
        self.push_casa.setStyleSheet("QPushButton{\n"
                                     "background-color: rgb(234, 201, 158);\n"
                                     "border-radius: 15px\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover{\n"
                                     "background-color: rgb(255, 255, 255);\n"
                                     "}\n"
                                     "\n"
                                     "QPushBotton{\n"
                                     "background-color: rgb(127, 88, 21);\n"
                                     "}")
        self.push_casa.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("venv/qtdesigner/house.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.push_casa.setIcon(icon2)
        self.push_casa.setIconSize(QtCore.QSize(52, 47))
        self.push_casa.setObjectName("push_casa")
        self.push_borrartodo = QtWidgets.QPushButton(Teclado)
        self.push_borrartodo.setGeometry(QtCore.QRect(1020, 280, 81, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_borrartodo.sizePolicy().hasHeightForWidth())
        self.push_borrartodo.setSizePolicy(sizePolicy)
        self.push_borrartodo.setStyleSheet("QPushButton{\n"
                                           "background-color: rgb(234, 201, 158);\n"
                                           "border-radius: 15px\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover{\n"
                                           "background-color: rgb(255, 255, 255);\n"
                                           "}\n"
                                           "\n"
                                           "QPushBotton{\n"
                                           "background-color: rgb(127, 88, 21);\n"
                                           "}")
        self.push_borrartodo.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("venv/qtdesigner/delete-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.push_borrartodo.setIcon(icon3)
        self.push_borrartodo.setIconSize(QtCore.QSize(75, 45))
        self.push_borrartodo.setObjectName("push_borrartodo")

        self.retranslateUi(Teclado)
        QtCore.QMetaObject.connectSlotsByName(Teclado)

        self.push_A.clicked.connect(self.method_A)
        self.push_B.clicked.connect(self.method_B)
        self.push_C.clicked.connect(self.method_C)
        self.push_D.clicked.connect(self.method_D)
        self.push_E.clicked.connect(self.method_E)
        self.push_F.clicked.connect(self.method_F)
        self.push_G.clicked.connect(self.method_G)
        self.push_H.clicked.connect(self.method_H)
        self.push_I.clicked.connect(self.method_I)
        self.push_J.clicked.connect(self.method_J)
        self.push_K.clicked.connect(self.method_K)
        self.push_L.clicked.connect(self.method_L)
        self.push_M.clicked.connect(self.method_M)
        self.push_N.clicked.connect(self.method_N)
        self.push_NN.clicked.connect(self.method_NN)
        self.push_O.clicked.connect(self.method_O)
        self.push_P.clicked.connect(self.method_P)
        self.push_Q.clicked.connect(self.method_Q)
        self.push_R.clicked.connect(self.method_R)
        self.push_S.clicked.connect(self.method_S)
        self.push_T.clicked.connect(self.method_T)
        self.push_U.clicked.connect(self.method_U)
        self.push_V.clicked.connect(self.method_V)
        self.push_W.clicked.connect(self.method_W)
        self.push_X.clicked.connect(self.method_X)
        self.push_Y.clicked.connect(self.method_Y)
        self.push_Z.clicked.connect(self.method_Z)
        self.push_audio.clicked.connect(self.method_audio)
        self.push_espacio.clicked.connect(self.method_espacio)
        self.push_borrar.clicked.connect(self.method_borrar)
        self.push_casa.clicked.connect(self.method_casa)
        self.push_borrartodo.clicked.connect(self.method_borrart)

    def method_A(self):
        text = self.label.text()
        self.label.setText(text + "A")
        click = pyglet.media.load("click.mp3", streaming=False)
        click.play()
        time.sleep(1)

    def method_B(self):
        text = self.label.text()
        self.label.setText(text + "B")

    def method_C(self):
        text = self.label.text()
        self.label.setText(text + "C")

    def method_D(self):
        text = self.label.text()
        self.label.setText(text + "D")

    def method_E(self):
        text = self.label.text()
        self.label.setText(text + "E")

    def method_F(self):
        text = self.label.text()
        self.label.setText(text + "F")

    def method_G(self):
        text = self.label.text()
        self.label.setText(text + "G")

    def method_H(self):
        text = self.label.text()
        self.label.setText(text + "H")
        click = pyglet.media.load("click.mp3", streaming=False)
        click.play()
        time.sleep(1)

    def method_I(self):
        text = self.label.text()
        self.label.setText(text + "I")

    def method_J(self):
        text = self.label.text()
        self.label.setText(text + "J")

    def method_K(self):
        text = self.label.text()
        self.label.setText(text + "K")

    def method_L(self):
        text = self.label.text()
        self.label.setText(text + "L")
        click = pyglet.media.load("click.mp3", streaming=False)
        click.play()
        time.sleep(1)

    def method_M(self):
        text = self.label.text()
        self.label.setText(text + "M")

    def method_N(self):
        text = self.label.text()
        self.label.setText(text + "N")

    def method_NN(self):
        text = self.label.text()
        self.label.setText(text + "??")

    def method_O(self):
        text = self.label.text()
        self.label.setText(text + "O")
        click = pyglet.media.load("click.mp3", streaming=False)
        click.play()
        time.sleep(1)

    def method_P(self):
        text = self.label.text()
        self.label.setText(text + "P")

    def method_Q(self):
        text = self.label.text()
        self.label.setText(text + "Q")

    def method_R(self):
        text = self.label.text()
        self.label.setText(text + "R")

    def method_S(self):
        text = self.label.text()
        self.label.setText(text + "S")

    def method_T(self):
        text = self.label.text()
        self.label.setText(text + "T")

    def method_U(self):
        text = self.label.text()
        self.label.setText(text + "U")

    def method_V(self):
        text = self.label.text()
        self.label.setText(text + "V")

    def method_W(self):
        text = self.label.text()
        self.label.setText(text + "W")

    def method_X(self):
        text = self.label.text()
        self.label.setText(text + "X")

    def method_Y(self):
        text = self.label.text()
        self.label.setText(text + "Y")

    def method_Z(self):
        text = self.label.text()
        self.label.setText(text + "Z")

    def method_borrart(self):
        text = self.label.text()
        self.label.setText("")
        click = pyglet.media.load("borrar.mp3", streaming=False)
        click.play()
        time.sleep(1)

    def method_borrar(self):
        text = self.label.text()
        self.label.setText(text[:len(text) - 1])
        click = pyglet.media.load("borrar.mp3", streaming=False)
        click.play()
        time.sleep(1)

    def method_espacio(self):
        text = self.label.text()
        self.label.setText(text + "  ")
        click = pyglet.media.load("espacio.mp3", streaming=False)
        click.play()
        time.sleep(1)

    def method_casa(self):
        click = pyglet.media.load("click.mp3", streaming=False)
        click.play()
        time.sleep(1)
        self.method_casa = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.method_casa)
        self.method_casa.show()

    def method_audio(self):
        mitexto = self.label.text()
        language = "es"
        output = gTTS(text=mitexto, lang=language, slow=False)
        output.save("audio.mp3")
        """
        playsound.playsound("audio.mp3")

        """
        audio = pyglet.media.load("audio.mp3", streaming=False)
        audio.play()
        time.sleep(1)
        os.remove("audio.mp3")

    def retranslateUi(self, Teclado):
        _translate = QtCore.QCoreApplication.translate
        Teclado.setWindowTitle(_translate("Teclado", "Teclado"))
        self.push_Q.setText(_translate("Teclado", "Q"))
        self.push_W.setText(_translate("Teclado", "W"))
        self.push_E.setText(_translate("Teclado", "E"))
        self.push_R.setText(_translate("Teclado", "R"))
        self.push_T.setText(_translate("Teclado", "T"))
        self.push_Y.setText(_translate("Teclado", "Y"))
        self.push_U.setText(_translate("Teclado", "U"))
        self.push_I.setText(_translate("Teclado", "I"))
        self.push_O.setText(_translate("Teclado", "O"))
        self.push_P.setText(_translate("Teclado", "P"))
        self.push_J.setText(_translate("Teclado", "J"))
        self.push_D.setWhatsThis(_translate("Teclado",
                                            "<html><head/><body><p>QPushButton{</p><p>font: 24pt &quot;HP Simplified Jpan&quot;;</p><p>    color: rgb(0, 0, 0);</p><p>    background-color: rgb(234, 201, 158);</p><p>border-radius: 15px</p><p>}</p><p><br/></p><p>QPushButton:hover{</p><p>color: rgb(0, 0, 0);</p><p>    background-color: rgb(255, 255, 255);</p><p>}</p><p><br/></p><p>QPushBotton{</p><p>background-color: rgb(127, 88, 21);</p><p>    color: rgb(255, 255, 255);</p><p>}</p></body></html>"))
        self.push_D.setText(_translate("Teclado", "D"))
        self.push_F.setText(_translate("Teclado", "F"))
        self.push_A.setText(_translate("Teclado", "A"))
        self.push_S.setText(_translate("Teclado", "S"))
        self.push_K.setText(_translate("Teclado", "K"))
        self.push_NN.setText(_translate("Teclado", "??"))
        self.push_G.setText(_translate("Teclado", "G"))
        self.push_H.setText(_translate("Teclado", "H"))
        self.push_L.setText(_translate("Teclado", "L"))
        self.push_M.setText(_translate("Teclado", "M"))
        self.push_V.setText(_translate("Teclado", "V"))
        self.push_B.setText(_translate("Teclado", "B"))
        self.push_X.setText(_translate("Teclado", "X"))
        self.push_Z.setText(_translate("Teclado", "Z"))
        self.push_N.setText(_translate("Teclado", "N"))
        self.push_C.setText(_translate("Teclado", "C"))

#Informacion del dispositivo
class Ui_Informacion(object):
    def setupUi(self, Informacion):
        Informacion.setObjectName("Informacion")
        Informacion.resize(797, 500)
        Informacion.setStyleSheet("background-color: rgb(71, 72, 72);")
        self.textBrowser = QtWidgets.QTextBrowser(Informacion)
        self.textBrowser.setGeometry(QtCore.QRect(30, 100, 731, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("QTextBrowser{\n"
"background-color: rgb(234, 201, 158);\n"
"border-radius: 10px\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Informacion)
        self.label.setGeometry(QtCore.QRect(450, 160, 341, 241))
        self.label.setStyleSheet("border-image: url(:/info/biomedicos.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Informacion)
        self.label_2.setGeometry(QtCore.QRect(30, 170, 431, 301))
        self.label_2.setStyleSheet("border-image: url(:/info/funciones.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.line_3 = QtWidgets.QFrame(Informacion)
        self.line_3.setGeometry(QtCore.QRect(0, 10, 801, 81))
        self.line_3.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.line_3.setStyleSheet("color: rgb(185, 144, 91);")
        self.line_3.setMidLineWidth(44)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_3 = QtWidgets.QLabel(Informacion)
        self.label_3.setGeometry(QtCore.QRect(180, 30, 441, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(185, 144, 91);")
        self.label_3.setObjectName("label_3")
        self.push_casa = QtWidgets.QPushButton(Informacion)
        self.push_casa.setGeometry(QtCore.QRect(600, 420, 61, 61))
        self.push_casa.setStyleSheet("QPushButton{\n"
"background-color: rgb(234, 201, 158);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(127, 88, 21);\n"
"}")
        self.push_casa.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("venv/qtdesigner/house.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.push_casa.setIcon(icon)
        self.push_casa.setIconSize(QtCore.QSize(52, 47))
        self.push_casa.setObjectName("push_casa")
        self.push_casa.clicked.connect(self.casa)
        self.retranslateUi(Informacion)
        QtCore.QMetaObject.connectSlotsByName(Informacion)

    def casa(self):
        click = pyglet.media.load("click.mp3", streaming=False)
        click.play()
        time.sleep(1)
        self.method_casa = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.method_casa)
        self.method_casa.show()

    def retranslateUi(self, Informacion):
        _translate = QtCore.QCoreApplication.translate
        Informacion.setWindowTitle(_translate("Informacion", "Informacion del dispositivo"))
        self.textBrowser.setHtml(_translate("Informacion", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI Variable Display Semib\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:140%;\"><span style=\" font-family:\'YACgEUaXOJg 0,_fb_,36\'; font-size:8pt; font-weight:400; color:#000000;\">VoiceScreen es un dispositivo que permite la comunicaci??n de un paciente con ELA mediante una interfaz gr??fica y un altavoz que reproducir?? los mensajes.</span></p></body></html>"))
        self.label_3.setText(_translate("Informacion", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Informaci??n del dispositivo</span></p></body></html>"))

import informacion_rc



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Inicio()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())