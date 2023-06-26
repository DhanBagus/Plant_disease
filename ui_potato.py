# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'potatoYCYXBS.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(458, 532)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnOpenFilePotato = QPushButton(self.centralwidget)
        self.btnOpenFilePotato.setObjectName(u"btnOpenFilePotato")
        self.btnOpenFilePotato.setGeometry(QRect(20, 10, 93, 28))
        self.containerIMG1 = QLabel(self.centralwidget)
        self.containerIMG1.setObjectName(u"containerIMG1")
        self.containerIMG1.setGeometry(QRect(20, 50, 200, 200))
        self.containerIMG1.setPixmap(QPixmap(u"Example Pictures/potatoleaf.jpg"))
        self.containerIMG1.setScaledContents(True)
        self.containerIMG2 = QLabel(self.centralwidget)
        self.containerIMG2.setObjectName(u"containerIMG2")
        self.containerIMG2.setGeometry(QRect(240, 50, 200, 200))
        self.containerIMG2.setPixmap(QPixmap(u"Example Pictures/potato.jpg"))
        self.containerIMG2.setScaledContents(True)
        self.labelhasilpotato = QLabel(self.centralwidget)
        self.labelhasilpotato.setObjectName(u"labelhasilpotato")
        self.labelhasilpotato.setGeometry(QRect(20, 260, 91, 20))
        font = QFont()
        font.setPointSize(10)
        self.labelhasilpotato.setFont(font)
        self.btnDeteksiPotato = QPushButton(self.centralwidget)
        self.btnDeteksiPotato.setObjectName(u"btnDeteksiPotato")
        self.btnDeteksiPotato.setGeometry(QRect(120, 10, 93, 28))
        self.hasilPotatoField = QPlainTextEdit(self.centralwidget)
        self.hasilPotatoField.setObjectName(u"hasilPotatoField")
        self.hasilPotatoField.setGeometry(QRect(20, 290, 421, 191))
        self.hasilPotatoField.setFrameShape(QFrame.Box)
        self.hasilPotatoField.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 458, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Potato", None))
        self.btnOpenFilePotato.setText(QCoreApplication.translate("MainWindow", u"Buka", None))
        self.containerIMG1.setText("")
        self.containerIMG2.setText("")
        self.labelhasilpotato.setText(QCoreApplication.translate("MainWindow", u"Hasil:", None))
        self.btnDeteksiPotato.setText(QCoreApplication.translate("MainWindow", u"Deteksi", None))
    # retranslateUi

