# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu-about.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import PushButton
from qfluentwidgets import CaptionLabel
from qfluentwidgets import BodyLabel
from qfluentwidgets import SubtitleLabel
from qfluentwidgets import TitleLabel


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(821, 651)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 24, 24, 24)
        self.TitleLabel = TitleLabel(Form)
        self.TitleLabel.setObjectName(u"TitleLabel")

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(48, 0, 48, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(128, 128))
        self.label.setStyleSheet(u"")
        self.label.setPixmap(QPixmap(u"img/Logo.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.SubtitleLabel = SubtitleLabel(Form)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")
        self.SubtitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.SubtitleLabel)

        self.version = BodyLabel(Form)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignCenter)
        self.version.setWordWrap(True)

        self.verticalLayout.addWidget(self.version)

        self.CaptionLabel_3 = CaptionLabel(Form)
        self.CaptionLabel_3.setObjectName(u"CaptionLabel_3")
        self.CaptionLabel_3.setAlignment(Qt.AlignCenter)
        self.CaptionLabel_3.setWordWrap(True)

        self.verticalLayout.addWidget(self.CaptionLabel_3)

        self.CaptionLabel = CaptionLabel(Form)
        self.CaptionLabel.setObjectName(u"CaptionLabel")
        self.CaptionLabel.setAlignment(Qt.AlignCenter)
        self.CaptionLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.CaptionLabel)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.button_github = PushButton(Form)
        self.button_github.setObjectName(u"button_github")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_github.sizePolicy().hasHeightForWidth())
        self.button_github.setSizePolicy(sizePolicy1)
        self.button_github.setMinimumSize(QSize(245, 0))
        self.button_github.setMaximumSize(QSize(360, 16777215))
        self.button_github.setProperty("hasIcon", False)

        self.horizontalLayout_2.addWidget(self.button_github)

        self.button_bilibili = PushButton(Form)
        self.button_bilibili.setObjectName(u"button_bilibili")
        sizePolicy1.setHeightForWidth(self.button_bilibili.sizePolicy().hasHeightForWidth())
        self.button_bilibili.setSizePolicy(sizePolicy1)
        self.button_bilibili.setMinimumSize(QSize(245, 0))
        self.button_bilibili.setMaximumSize(QSize(360, 16777215))

        self.horizontalLayout_2.addWidget(self.button_bilibili)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.CaptionLabel_2 = CaptionLabel(Form)
        self.CaptionLabel_2.setObjectName(u"CaptionLabel_2")
        self.CaptionLabel_2.setAlignment(Qt.AlignCenter)
        self.CaptionLabel_2.setProperty("lightColor", QColor(127, 127, 127))
        self.CaptionLabel_2.setProperty("darkColor", QColor(185, 185, 185))

        self.verticalLayout_2.addWidget(self.CaptionLabel_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u5173\u4e8e", None))
        self.label.setText("")
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", u"Class Widgets", None))
        self.version.setText(QCoreApplication.translate("Form", u"\u7248\u672c\uff1a1.1.5.6", None))
        self.CaptionLabel_3.setText(QCoreApplication.translate("Form", u"Class Widgets \u662f\u4e00\u6b3e\u80fd\u663e\u793a\u5f53\u524d\u8bfe\u7a0b\u7684\u684c\u9762\u7ec4\u4ef6App\u3002\u5176\u63d0\u4f9b\u4e86\u76f4\u89c2\u7684\u56fe\u5f62\u5316\u8bfe\u7a0b\u8868\u7f16\u8f91\u548c\u7f8e\u89c2\u7684\u684c\u9762\u7ec4\u4ef6\u3002", None))
        self.CaptionLabel.setText(QCoreApplication.translate("Form", u"\u6b64\u8f6f\u4ef6\u57fa\u4e8e PySide2 \u5f00\u53d1\uff0c\u5176\u4e2d\u7279\u522b\u5f15\u7528 QFluentWidget \u4f5c\u4e3a\u754c\u9762UI\uff0c\u6839\u636e\u534f\u8bae\u91c7\u7528 GPL-3.0 \u5f00\u6e90\u534f\u8bae\u3002\n"
"\u7531 RinLit \u5f00\u53d1", None))
        self.button_github.setText(QCoreApplication.translate("Form", u"\u6b64\u9879\u76ee\u7684 Github", None))
        self.button_bilibili.setText(QCoreApplication.translate("Form", u"\u6211\u7684 \u54d4\u54e9\u54d4\u54e9 \u4e3b\u9875", None))
        self.CaptionLabel_2.setText(QCoreApplication.translate("Form", u"Copyright \u00a9 2024 RinLit, All Rights Reversed.", None))
    # retranslateUi

