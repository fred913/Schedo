# -*- coding: utf-8 -*-

from PySide2.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide2.QtGui import QFont, QPixmap
from PySide2.QtWidgets import QFrame, QHBoxLayout, QLabel, QSizePolicy, QSpacerItem


class Ui_ToastBar(object):

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(646, 125)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 65536))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 8, 8, 22)
        self.backgnd = QFrame(Form)
        self.backgnd.setObjectName("backgnd")
        self.backgnd.setStyleSheet(
            "border: none;\n"
            "color: rgba(255, 255, 255, 255); \n"
            "font-weight: bold; \n"
            "border-radius: 8px; \n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 200, 150, 255), stop:1 rgba(217, 147, 107, 255));")
        self.backgnd.setFrameShape(QFrame.StyledPanel)
        self.backgnd.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.backgnd)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(52)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(23)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.icon = QLabel(self.backgnd)
        self.icon.setObjectName("icon")
        self.icon.setStyleSheet("background: transparent")
        self.icon.setPixmap(QPixmap("img/attend_class.svg"))

        self.horizontalLayout_4.addWidget(self.icon)

        self.title = QLabel(self.backgnd)
        self.title.setObjectName("title")
        font = QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background: transparent")

        self.horizontalLayout_4.addWidget(self.title)

        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(16)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.subtitle = QLabel(self.backgnd)
        self.subtitle.setObjectName("subtitle")
        font1 = QFont()
        font1.setFamily("Microsoft YaHei UI")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.subtitle.setFont(font1)
        self.subtitle.setStyleSheet("background: transparent;\n"
                                    "font-weight: bold;\n"
                                    "color: rgba(255, 255, 255, 200);")

        self.horizontalLayout_5.addWidget(self.subtitle)

        self.lesson = QLabel(self.backgnd)
        self.lesson.setObjectName("lesson")
        font2 = QFont()
        font2.setFamily("Microsoft YaHei UI")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.lesson.setFont(font2)
        self.lesson.setStyleSheet("color: rgb(255, 255, 255);\n"
                                  "background: transparent")
        self.lesson.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

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
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form"))
        self.icon.setText("")
        self.title.setText(QCoreApplication.translate("Form", "上课"))
        self.subtitle.setText(QCoreApplication.translate("Form", "当前课程"))
        self.lesson.setText(QCoreApplication.translate("Form", "英语"))

    # retranslateUi
