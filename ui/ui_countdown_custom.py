# -*- coding: utf-8 -*-

from PySide2.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QLabel


class Ui_CountdownCustom(object):

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(200, 125)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 65536))
        self.countdown_custom_title = QLabel(Form)
        self.countdown_custom_title.setObjectName("countdown_custom_title")
        self.countdown_custom_title.setGeometry(QRect(20, 20, 161, 31))
        font = QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.countdown_custom_title.setFont(font)
        self.countdown_custom_title.setStyleSheet("color: rgba(0, 0, 0, 90);\n"
                                                  "font-weight: bold;")
        self.countdown_custom_title.setTextFormat(Qt.PlainText)
        self.countdown_custom_title.setAlignment(Qt.AlignCenter)
        self.custom_countdown = QLabel(Form)
        self.custom_countdown.setObjectName("custom_countdown")
        self.custom_countdown.setGeometry(QRect(20, 30, 161, 71))
        font1 = QFont()
        font1.setFamily("Microsoft YaHei UI")
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setWeight(75)
        self.custom_countdown.setFont(font1)
        self.custom_countdown.setStyleSheet("border: none;\n"
                                            "color: rgba(37, 37, 37, 255);\n"
                                            "font-weight: bold")
        self.custom_countdown.setTextFormat(Qt.PlainText)
        self.custom_countdown.setAlignment(Qt.AlignCenter)
        self.label = QLabel(Form)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(10, 10, 181, 91))
        self.label.setStyleSheet("background-color: rgba(242, 243, 245, 242);\n"
                                 "border-radius: 8px")
        self.label.raise_()
        self.countdown_custom_title.raise_()
        self.custom_countdown.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form"))
        self.countdown_custom_title.setText(QCoreApplication.translate("Form", "距离 中考 还有"))
        self.custom_countdown.setText(QCoreApplication.translate("Form", "300 天"))
        self.label.setText("")

    # retranslateUi
