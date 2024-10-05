# -*- coding: utf-8 -*-

from PySide2.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QLabel


class Ui_Time(object):

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(230, 125)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 65536))
        self.date_text = QLabel(Form)
        self.date_text.setObjectName("date_text")
        self.date_text.setGeometry(QRect(30, 20, 161, 31))
        font = QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.date_text.setFont(font)
        self.date_text.setStyleSheet("color: rgba(0, 0, 0, 90);\n"
                                     "font-weight: bold;")
        self.date_text.setTextFormat(Qt.PlainText)
        self.date_text.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.day_text = QLabel(Form)
        self.day_text.setObjectName("day_text")
        self.day_text.setGeometry(QRect(40, 40, 151, 51))
        font1 = QFont()
        font1.setFamily("Microsoft YaHei")
        font1.setPointSize(21)
        font1.setBold(True)
        font1.setWeight(75)
        self.day_text.setFont(font1)
        self.day_text.setStyleSheet("border: none;\n"
                                    "color: rgba(37, 37, 37, 255);\n"
                                    "font-weight: bold")
        self.day_text.setTextFormat(Qt.PlainText)
        self.day_text.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label = QLabel(Form)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(10, 10, 211, 91))
        self.label.setStyleSheet("background-color: rgba(242, 243, 245, 242);\n"
                                 "border-radius: 8px")
        self.label.raise_()
        self.date_text.raise_()
        self.day_text.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form"))
        self.date_text.setText(QCoreApplication.translate("Form", "2025 年  13 月"))
        self.day_text.setText(QCoreApplication.translate("Form", "32 日 周二"))
        self.label.setText("")

    # retranslateUi
