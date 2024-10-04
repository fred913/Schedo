# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget-weather.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(230, 125)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 65536))
        self.activity_countdown_title = QLabel(Form)
        self.activity_countdown_title.setObjectName(u"activity_countdown_title")
        self.activity_countdown_title.setGeometry(QRect(20, 20, 191, 31))
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.activity_countdown_title.setFont(font)
        self.activity_countdown_title.setStyleSheet(u"color: rgba(0, 0, 0, 90);\n"
"font-weight: bold;")
        self.activity_countdown_title.setTextFormat(Qt.PlainText)
        self.activity_countdown_title.setAlignment(Qt.AlignCenter)
        self.activity_countdown = QLabel(Form)
        self.activity_countdown.setObjectName(u"activity_countdown")
        self.activity_countdown.setGeometry(QRect(100, 40, 111, 51))
        font1 = QFont()
        font1.setFamily(u"Microsoft YaHei UI")
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setWeight(75)
        self.activity_countdown.setFont(font1)
        self.activity_countdown.setStyleSheet(u"border: none;\n"
"color: rgba(37, 37, 37, 255);\n"
"font-weight: bold")
        self.activity_countdown.setTextFormat(Qt.PlainText)
        self.activity_countdown.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 211, 91))
        self.label.setStyleSheet(u"background-color: rgba(242, 243, 245, 242);\n"
"border-radius: 8px")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 50, 31, 31))
        self.label.raise_()
        self.activity_countdown_title.raise_()
        self.activity_countdown.raise_()
        self.label_2.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.activity_countdown_title.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u57ce\u5e02", None))
        self.activity_countdown.setText(QCoreApplication.translate("Form", u"114\u2109", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"IMG", None))
    # retranslateUi

