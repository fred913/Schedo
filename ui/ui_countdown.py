# -*- coding: utf-8 -*-

from PySide2.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QLabel
from qfluentwidgets import ProgressBar


class Ui_Countdown(object):

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(200, 125)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 65536))
        self.progressBar = ProgressBar(Form)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setGeometry(QRect(20, 90, 161, 5))
        self.progressBar.setMinimumSize(QSize(0, 5))
        self.progressBar.setMaximumSize(QSize(16777215, 6))
        self.progressBar.setStyleSheet("")
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setUseAni(True)
        self.progressBar.setVal(0.000000000000000)
        self.activity_countdown_title = QLabel(Form)
        self.activity_countdown_title.setObjectName("activity_countdown_title")
        self.activity_countdown_title.setGeometry(QRect(20, 20, 161, 31))
        font = QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.activity_countdown_title.setFont(font)
        self.activity_countdown_title.setStyleSheet("color: rgba(0, 0, 0, 90);\n"
                                                    "font-weight: bold;")
        self.activity_countdown_title.setTextFormat(Qt.PlainText)
        self.activity_countdown_title.setAlignment(Qt.AlignCenter)
        self.activity_countdown = QLabel(Form)
        self.activity_countdown.setObjectName("activity_countdown")
        self.activity_countdown.setGeometry(QRect(20, 40, 161, 51))
        font1 = QFont()
        font1.setFamily("Microsoft YaHei")
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setWeight(75)
        self.activity_countdown.setFont(font1)
        self.activity_countdown.setStyleSheet("border: none;\n"
                                              "color: rgba(37, 37, 37, 255);\n"
                                              "font-weight: bold")
        self.activity_countdown.setTextFormat(Qt.PlainText)
        self.activity_countdown.setAlignment(Qt.AlignCenter)
        self.label = QLabel(Form)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(10, 10, 181, 91))
        self.label.setStyleSheet("background-color: rgba(242, 243, 245, 242);\n"
                                 "border-radius: 8px")
        self.label.raise_()
        self.progressBar.raise_()
        self.activity_countdown_title.raise_()
        self.activity_countdown.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form"))
        self.activity_countdown_title.setText(QCoreApplication.translate("Form", "倒计时"))
        self.activity_countdown.setText(QCoreApplication.translate("Form", "00:00"))
        self.label.setText("")

    # retranslateUi
