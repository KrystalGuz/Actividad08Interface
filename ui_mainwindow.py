# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
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
        MainWindow.resize(340, 368)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Id = QLabel(self.groupBox)
        self.Id.setObjectName(u"Id")

        self.gridLayout.addWidget(self.Id, 0, 0, 1, 1)

        self.OrigenX = QLabel(self.groupBox)
        self.OrigenX.setObjectName(u"OrigenX")

        self.gridLayout.addWidget(self.OrigenX, 1, 0, 1, 1)

        self.OrigenY = QLabel(self.groupBox)
        self.OrigenY.setObjectName(u"OrigenY")

        self.gridLayout.addWidget(self.OrigenY, 2, 0, 1, 1)

        self.DestinoX = QLabel(self.groupBox)
        self.DestinoX.setObjectName(u"DestinoX")

        self.gridLayout.addWidget(self.DestinoX, 3, 0, 1, 1)

        self.DestinoY = QLabel(self.groupBox)
        self.DestinoY.setObjectName(u"DestinoY")

        self.gridLayout.addWidget(self.DestinoY, 4, 0, 1, 1)

        self.Velocidad = QLabel(self.groupBox)
        self.Velocidad.setObjectName(u"Velocidad")

        self.gridLayout.addWidget(self.Velocidad, 5, 0, 1, 1)

        self.spinBox_6 = QSpinBox(self.groupBox)
        self.spinBox_6.setObjectName(u"spinBox_6")

        self.gridLayout.addWidget(self.spinBox_6, 5, 1, 1, 2)

        self.Color = QLabel(self.groupBox)
        self.Color.setObjectName(u"Color")

        self.gridLayout.addWidget(self.Color, 6, 0, 1, 1)

        self.Red = QLabel(self.groupBox)
        self.Red.setObjectName(u"Red")

        self.gridLayout.addWidget(self.Red, 7, 0, 1, 1)

        self.Green = QLabel(self.groupBox)
        self.Green.setObjectName(u"Green")

        self.gridLayout.addWidget(self.Green, 8, 0, 1, 1)

        self.Blue = QLabel(self.groupBox)
        self.Blue.setObjectName(u"Blue")

        self.gridLayout.addWidget(self.Blue, 9, 0, 1, 1)

        self.spinBox_9 = QSpinBox(self.groupBox)
        self.spinBox_9.setObjectName(u"spinBox_9")
        self.spinBox_9.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_9, 9, 1, 1, 2)

        self.Agregar = QPushButton(self.groupBox)
        self.Agregar.setObjectName(u"Agregar")

        self.gridLayout.addWidget(self.Agregar, 10, 0, 1, 3)

        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout.addWidget(self.spinBox, 0, 1, 1, 2)

        self.spinBox_2 = QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_2, 1, 1, 1, 2)

        self.spinBox_3 = QSpinBox(self.groupBox)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_3, 2, 1, 1, 2)

        self.spinBox_4 = QSpinBox(self.groupBox)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_4, 3, 1, 1, 2)

        self.spinBox_5 = QSpinBox(self.groupBox)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_5, 4, 1, 1, 2)

        self.spinBox_7 = QSpinBox(self.groupBox)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_7, 7, 1, 1, 2)

        self.spinBox_8 = QSpinBox(self.groupBox)
        self.spinBox_8.setObjectName(u"spinBox_8")
        self.spinBox_8.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_8, 8, 1, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 340, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.groupBox.setTitle("")
        self.Id.setText(QCoreApplication.translate("MainWindow", u"Id:", None))
        self.OrigenX.setText(QCoreApplication.translate("MainWindow", u"Origen en x:", None))
        self.OrigenY.setText(QCoreApplication.translate("MainWindow", u"Origen en y:", None))
        self.DestinoX.setText(QCoreApplication.translate("MainWindow", u"Destino en x:", None))
        self.DestinoY.setText(QCoreApplication.translate("MainWindow", u"Destino en y:", None))
        self.Velocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.Color.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.Red.setText(QCoreApplication.translate("MainWindow", u"Red:", None))
        self.Green.setText(QCoreApplication.translate("MainWindow", u"Green:", None))
        self.Blue.setText(QCoreApplication.translate("MainWindow", u"Blue:", None))
        self.Agregar.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
    # retranslateUi

