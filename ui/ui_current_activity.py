# -*- coding: utf-8 -*-

from PySide2.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide2.QtGui import QFont, QIcon
from PySide2.QtWidgets import QLabel, QPushButton


class Ui_CurrentActivity(object):

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(360, 125)
        Form.setMinimumSize(QSize(0, 100))
        Form.setMaximumSize(QSize(16777215, 65536))
        self.subject = QPushButton(Form)
        self.subject.setObjectName("subject")
        self.subject.setGeometry(QRect(10, 0, 341, 131))
        font = QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.subject.setFont(font)
        self.subject.setStyleSheet("border: none;\n"
                                   "color: rgba(37, 37, 37, 255);\n"
                                   "font-weight: bold")
        icon = QIcon()
        icon.addFile("img/it.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.subject.setIcon(icon)
        self.subject.setIconSize(QSize(36, 26))
        self.blurEffect = QLabel(Form)
        self.blurEffect.setObjectName("blurEffect")
        self.blurEffect.setGeometry(QRect(155, 35, 45, 45))
        self.blurEffect.setStyleSheet("background-color: rgb(0, 255, 127);\n"
                                      "border-radius:20px")
        self.sub_title = QLabel(Form)
        self.sub_title.setObjectName("sub_title")
        self.sub_title.setGeometry(QRect(30, 0, 301, 71))
        font1 = QFont()
        font1.setFamily("Microsoft YaHei")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.sub_title.setFont(font1)
        self.sub_title.setStyleSheet("color: rgba(0, 0, 0, 90);\n"
                                     "font-weight: bold;")
        self.sub_title.setTextFormat(Qt.PlainText)
        self.sub_title.setAlignment(Qt.AlignCenter)
        self.label = QLabel(Form)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(10, 10, 341, 91))
        self.label.setStyleSheet("background-color: rgba(242, 243, 245, 242);\n"
                                 "border-radius: 8px")
        self.label.raise_()
        self.blurEffect.raise_()
        self.sub_title.raise_()
        self.subject.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form"))
        self.subject.setText(QCoreApplication.translate("Form", "  测试"))
        self.blurEffect.setText("")
        self.sub_title.setText(QCoreApplication.translate("Form", "当前活动"))
        self.label.setText("")

    # retranslateUi
