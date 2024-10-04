# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget-countdown-custom.ui'
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
        Form.resize(200, 125)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 65536))
        self.countdown_custom_title = QLabel(Form)
        self.countdown_custom_title.setObjectName(u"countdown_custom_title")
        self.countdown_custom_title.setGeometry(QRect(20, 20, 161, 31))
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.countdown_custom_title.setFont(font)
        self.countdown_custom_title.setStyleSheet(u"color: rgba(0, 0, 0, 90);\n"
"font-weight: bold;")
        self.countdown_custom_title.setTextFormat(Qt.PlainText)
        self.countdown_custom_title.setAlignment(Qt.AlignCenter)
        self.custom_countdown = QLabel(Form)
        self.custom_countdown.setObjectName(u"custom_countdown")
        self.custom_countdown.setGeometry(QRect(20, 30, 161, 71))
        font1 = QFont()
        font1.setFamily(u"Microsoft YaHei UI")
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setWeight(75)
        self.custom_countdown.setFont(font1)
        self.custom_countdown.setStyleSheet(u"border: none;\n"
"color: rgba(37, 37, 37, 255);\n"
"font-weight: bold")
        self.custom_countdown.setTextFormat(Qt.PlainText)
        self.custom_countdown.setAlignment(Qt.AlignCenter)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 181, 91))
        self.label.setStyleSheet(u"background-color: rgba(242, 243, 245, 242);\n"
"border-radius: 8px")
        self.label.raise_()
        self.countdown_custom_title.raise_()
        self.custom_countdown.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.countdown_custom_title.setText(QCoreApplication.translate("Form", u"\u8ddd\u79bb \u4e2d\u8003 \u8fd8\u6709", None))
        self.custom_countdown.setText(QCoreApplication.translate("Form", u"300 \u5929", None))
        self.label.setText("")
    # retranslateUi

