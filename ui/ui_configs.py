# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu-configs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import PushButton
from qfluentwidgets import CardWidget
from qfluentwidgets import SmoothScrollArea
from qfluentwidgets import CaptionLabel
from qfluentwidgets import StrongBodyLabel
from qfluentwidgets import SubtitleLabel
from qfluentwidgets import TitleLabel


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(721, 814)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 24, 24, 24)
        self.TitleLabel = TitleLabel(Form)
        self.TitleLabel.setObjectName(u"TitleLabel")

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.SmoothScrollArea = SmoothScrollArea(Form)
        self.SmoothScrollArea.setObjectName(u"SmoothScrollArea")
        self.SmoothScrollArea.setStyleSheet(u"background: transparent; border: none")
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 673, 709))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.SubtitleLabel_3 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_3.setObjectName(u"SubtitleLabel_3")

        self.verticalLayout_5.addWidget(self.SubtitleLabel_3)

        self.CardWidget_6 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_6.setObjectName(u"CardWidget_6")
        self.CardWidget_6.setMinimumSize(QSize(0, 60))
        self.horizontalLayout_6 = QHBoxLayout(self.CardWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.StrongBodyLabel_6 = StrongBodyLabel(self.CardWidget_6)
        self.StrongBodyLabel_6.setObjectName(u"StrongBodyLabel_6")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StrongBodyLabel_6.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_6.setSizePolicy(sizePolicy)

        self.verticalLayout_10.addWidget(self.StrongBodyLabel_6)

        self.CaptionLabel_5 = CaptionLabel(self.CardWidget_6)
        self.CaptionLabel_5.setObjectName(u"CaptionLabel_5")

        self.verticalLayout_10.addWidget(self.CaptionLabel_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout_10)

        self.im_schedule = PushButton(self.CardWidget_6)
        self.im_schedule.setObjectName(u"im_schedule")

        self.horizontalLayout_6.addWidget(self.im_schedule)


        self.verticalLayout_5.addWidget(self.CardWidget_6)

        self.CardWidget_8 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_8.setObjectName(u"CardWidget_8")
        self.CardWidget_8.setMinimumSize(QSize(0, 60))
        self.horizontalLayout_8 = QHBoxLayout(self.CardWidget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.StrongBodyLabel_8 = StrongBodyLabel(self.CardWidget_8)
        self.StrongBodyLabel_8.setObjectName(u"StrongBodyLabel_8")
        sizePolicy.setHeightForWidth(self.StrongBodyLabel_8.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_8.setSizePolicy(sizePolicy)

        self.verticalLayout_13.addWidget(self.StrongBodyLabel_8)

        self.CaptionLabel_8 = CaptionLabel(self.CardWidget_8)
        self.CaptionLabel_8.setObjectName(u"CaptionLabel_8")

        self.verticalLayout_13.addWidget(self.CaptionLabel_8)


        self.horizontalLayout_8.addLayout(self.verticalLayout_13)

        self.ex_schedule = PushButton(self.CardWidget_8)
        self.ex_schedule.setObjectName(u"ex_schedule")

        self.horizontalLayout_8.addWidget(self.ex_schedule)


        self.verticalLayout_5.addWidget(self.CardWidget_8)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.SmoothScrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u914d\u7f6e\u6587\u4ef6", None))
        self.SubtitleLabel_3.setText(QCoreApplication.translate("Form", u"\u8bfe\u7a0b\u8868", None))
        self.StrongBodyLabel_6.setText(QCoreApplication.translate("Form", u"\u5bfc\u5165 Class Widgets \u8bfe\u7a0b\u8868", None))
        self.CaptionLabel_5.setText(QCoreApplication.translate("Form", u"\u9700\u5bfc\u5165\u4ece\u5176\u4ed6 Class Widgets \u5bfc\u51fa\u7684\u8bfe\u7a0b\u8868", None))
        self.im_schedule.setText(QCoreApplication.translate("Form", u"\u5bfc\u5165\u8bfe\u7a0b\u8868", None))
        self.StrongBodyLabel_8.setText(QCoreApplication.translate("Form", u"\u5bfc\u51fa Class Widgets \u8bfe\u7a0b\u8868", None))
        self.CaptionLabel_8.setText(QCoreApplication.translate("Form", u"\u5c06\u5f53\u524d\u4f7f\u7528\u7684\u8bfe\u7a0b\u8868\u6587\u4ef6 (.json) \u5bfc\u51fa", None))
        self.ex_schedule.setText(QCoreApplication.translate("Form", u"\u5bfc\u51fa\u8bfe\u7a0b\u8868", None))
    # retranslateUi

