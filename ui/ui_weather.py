# -*- coding: utf-8 -*-

from PySide2.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QLabel


class Ui_Weather(object):

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(230, 125)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 65536))
        self.activity_countdown_title = QLabel(Form)
        self.activity_countdown_title.setObjectName("activity_countdown_title")
        self.activity_countdown_title.setGeometry(QRect(20, 20, 191, 31))
        font = QFont()
        font.setFamily("Microsoft YaHei UI")
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
        self.activity_countdown.setGeometry(QRect(100, 40, 111, 51))
        font1 = QFont()
        font1.setFamily("Microsoft YaHei UI")
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setWeight(75)
        self.activity_countdown.setFont(font1)
        self.activity_countdown.setStyleSheet("border: none;\n"
                                              "color: rgba(37, 37, 37, 255);\n"
                                              "font-weight: bold")
        self.activity_countdown.setTextFormat(Qt.PlainText)
        self.activity_countdown.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label = QLabel(Form)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(10, 10, 211, 91))
        self.label.setStyleSheet("background-color: rgba(242, 243, 245, 242);\n"
                                 "border-radius: 8px")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(50, 50, 31, 31))
        self.label.raise_()
        self.activity_countdown_title.raise_()
        self.activity_countdown.raise_()
        self.label_2.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form"))
        self.activity_countdown_title.setText(QCoreApplication.translate("Form", "当前城市"))
        self.activity_countdown.setText(QCoreApplication.translate("Form", "114℉"))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", "IMG"))

    # retranslateUi
