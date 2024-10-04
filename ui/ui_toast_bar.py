# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget-toast-bar.ui'
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
        Form.resize(646, 125)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 65536))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 8, 8, 22)
        self.backgnd = QFrame(Form)
        self.backgnd.setObjectName(u"backgnd")
        self.backgnd.setStyleSheet(u"border: none;\n"
"color: rgba(255, 255, 255, 255); \n"
"font-weight: bold; \n"
"border-radius: 8px; \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 200, 150, 255), stop:1 rgba(217, 147, 107, 255));")
        self.backgnd.setFrameShape(QFrame.StyledPanel)
        self.backgnd.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.backgnd)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(52)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(23)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.icon = QLabel(self.backgnd)
        self.icon.setObjectName(u"icon")
        self.icon.setStyleSheet(u"background: transparent")
        self.icon.setPixmap(QPixmap(u"img/attend_class.svg"))

        self.horizontalLayout_4.addWidget(self.icon)

        self.title = QLabel(self.backgnd)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent")

        self.horizontalLayout_4.addWidget(self.title)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(16)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.subtitle = QLabel(self.backgnd)
        self.subtitle.setObjectName(u"subtitle")
        font1 = QFont()
        font1.setFamily(u"Microsoft YaHei UI")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.subtitle.setFont(font1)
        self.subtitle.setStyleSheet(u"background: transparent;\n"
"font-weight: bold;\n"
"color: rgba(255, 255, 255, 200);")

        self.horizontalLayout_5.addWidget(self.subtitle)

        self.lesson = QLabel(self.backgnd)
        self.lesson.setObjectName(u"lesson")
        font2 = QFont()
        font2.setFamily(u"Microsoft YaHei UI")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.lesson.setFont(font2)
        self.lesson.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: transparent")
        self.lesson.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lesson)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addWidget(self.backgnd)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.icon.setText("")
        self.title.setText(QCoreApplication.translate("Form", u"\u4e0a\u8bfe", None))
        self.subtitle.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u8bfe\u7a0b", None))
        self.lesson.setText(QCoreApplication.translate("Form", u"\u82f1\u8bed", None))
    # retranslateUi

