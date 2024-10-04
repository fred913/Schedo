# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu-advance.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import ComboBox
from qfluentwidgets import SwitchButton
from qfluentwidgets import CardWidget
from qfluentwidgets import SmoothScrollArea
from qfluentwidgets import CalendarPicker
from qfluentwidgets import CaptionLabel
from qfluentwidgets import StrongBodyLabel
from qfluentwidgets import SubtitleLabel
from qfluentwidgets import TitleLabel
from qfluentwidgets import LineEdit
from qfluentwidgets import SpinBox


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(745, 1172)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 697, 1067))
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
        self.CardWidget_6.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_6 = QHBoxLayout(self.CardWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.StrongBodyLabel_6 = StrongBodyLabel(self.CardWidget_6)
        self.StrongBodyLabel_6.setObjectName(u"StrongBodyLabel_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_6.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_6.setSizePolicy(sizePolicy1)

        self.verticalLayout_10.addWidget(self.StrongBodyLabel_6)

        self.CaptionLabel_5 = CaptionLabel(self.CardWidget_6)
        self.CaptionLabel_5.setObjectName(u"CaptionLabel_5")

        self.verticalLayout_10.addWidget(self.CaptionLabel_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout_10)

        self.switch_enable_toast = SwitchButton(self.CardWidget_6)
        self.switch_enable_toast.setObjectName(u"switch_enable_toast")

        self.horizontalLayout_6.addWidget(self.switch_enable_toast)


        self.verticalLayout_5.addWidget(self.CardWidget_6)

        self.CardWidget_7 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_7.setObjectName(u"CardWidget_7")
        self.CardWidget_7.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_7 = QHBoxLayout(self.CardWidget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.StrongBodyLabel_7 = StrongBodyLabel(self.CardWidget_7)
        self.StrongBodyLabel_7.setObjectName(u"StrongBodyLabel_7")

        self.verticalLayout_11.addWidget(self.StrongBodyLabel_7)

        self.CaptionLabel_6 = CaptionLabel(self.CardWidget_7)
        self.CaptionLabel_6.setObjectName(u"CaptionLabel_6")

        self.verticalLayout_11.addWidget(self.CaptionLabel_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_11)

        self.offset_spin = SpinBox(self.CardWidget_7)
        self.offset_spin.setObjectName(u"offset_spin")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.offset_spin.sizePolicy().hasHeightForWidth())
        self.offset_spin.setSizePolicy(sizePolicy2)
        self.offset_spin.setMinimum(-99)

        self.horizontalLayout_7.addWidget(self.offset_spin)


        self.verticalLayout_5.addWidget(self.CardWidget_7)

        self.CardWidget_3 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_3.setObjectName(u"CardWidget_3")
        self.CardWidget_3.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_5 = QHBoxLayout(self.CardWidget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.StrongBodyLabel_5 = StrongBodyLabel(self.CardWidget_3)
        self.StrongBodyLabel_5.setObjectName(u"StrongBodyLabel_5")

        self.verticalLayout_6.addWidget(self.StrongBodyLabel_5)

        self.CaptionLabel_2 = CaptionLabel(self.CardWidget_3)
        self.CaptionLabel_2.setObjectName(u"CaptionLabel_2")

        self.verticalLayout_6.addWidget(self.CaptionLabel_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.conf_name = LineEdit(self.CardWidget_3)
        self.conf_name.setObjectName(u"conf_name")
        sizePolicy2.setHeightForWidth(self.conf_name.sizePolicy().hasHeightForWidth())
        self.conf_name.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.conf_name)

        self.conf_combo = ComboBox(self.CardWidget_3)
        self.conf_combo.setObjectName(u"conf_combo")
        sizePolicy2.setHeightForWidth(self.conf_combo.sizePolicy().hasHeightForWidth())
        self.conf_combo.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.conf_combo)


        self.verticalLayout_5.addWidget(self.CardWidget_3)

        self.CardWidget_8 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_8.setObjectName(u"CardWidget_8")
        self.CardWidget_8.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_8 = QHBoxLayout(self.CardWidget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.StrongBodyLabel_8 = StrongBodyLabel(self.CardWidget_8)
        self.StrongBodyLabel_8.setObjectName(u"StrongBodyLabel_8")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_8.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_8.setSizePolicy(sizePolicy1)

        self.verticalLayout_13.addWidget(self.StrongBodyLabel_8)

        self.CaptionLabel_8 = CaptionLabel(self.CardWidget_8)
        self.CaptionLabel_8.setObjectName(u"CaptionLabel_8")

        self.verticalLayout_13.addWidget(self.CaptionLabel_8)


        self.horizontalLayout_8.addLayout(self.verticalLayout_13)

        self.switch_enable_alt_schedule = SwitchButton(self.CardWidget_8)
        self.switch_enable_alt_schedule.setObjectName(u"switch_enable_alt_schedule")

        self.horizontalLayout_8.addWidget(self.switch_enable_alt_schedule)


        self.verticalLayout_5.addWidget(self.CardWidget_8)

        self.CardWidget_9 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_9.setObjectName(u"CardWidget_9")
        self.CardWidget_9.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_9 = QHBoxLayout(self.CardWidget_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.StrongBodyLabel_9 = StrongBodyLabel(self.CardWidget_9)
        self.StrongBodyLabel_9.setObjectName(u"StrongBodyLabel_9")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_9.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_9.setSizePolicy(sizePolicy1)

        self.verticalLayout_12.addWidget(self.StrongBodyLabel_9)

        self.CaptionLabel_7 = CaptionLabel(self.CardWidget_9)
        self.CaptionLabel_7.setObjectName(u"CaptionLabel_7")

        self.verticalLayout_12.addWidget(self.CaptionLabel_7)


        self.horizontalLayout_9.addLayout(self.verticalLayout_12)

        self.set_start_date = CalendarPicker(self.CardWidget_9)
        self.set_start_date.setObjectName(u"set_start_date")

        self.horizontalLayout_9.addWidget(self.set_start_date)


        self.verticalLayout_5.addWidget(self.CardWidget_9)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SubtitleLabel = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")

        self.verticalLayout.addWidget(self.SubtitleLabel)

        self.CardWidget = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget.setObjectName(u"CardWidget")
        self.CardWidget.setMinimumSize(QSize(0, 70))
        self.horizontalLayout = QHBoxLayout(self.CardWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.StrongBodyLabel_2 = StrongBodyLabel(self.CardWidget)
        self.StrongBodyLabel_2.setObjectName(u"StrongBodyLabel_2")

        self.verticalLayout_4.addWidget(self.StrongBodyLabel_2)

        self.CaptionLabel_3 = CaptionLabel(self.CardWidget)
        self.CaptionLabel_3.setObjectName(u"CaptionLabel_3")
        sizePolicy1.setHeightForWidth(self.CaptionLabel_3.sizePolicy().hasHeightForWidth())
        self.CaptionLabel_3.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.CaptionLabel_3)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.switch_pin_button = SwitchButton(self.CardWidget)
        self.switch_pin_button.setObjectName(u"switch_pin_button")

        self.horizontalLayout.addWidget(self.switch_pin_button)


        self.verticalLayout.addWidget(self.CardWidget)

        self.CardWidget_2 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_2.setObjectName(u"CardWidget_2")
        self.CardWidget_2.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_2 = QHBoxLayout(self.CardWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.StrongBodyLabel = StrongBodyLabel(self.CardWidget_2)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")

        self.verticalLayout_3.addWidget(self.StrongBodyLabel)

        self.CaptionLabel = CaptionLabel(self.CardWidget_2)
        self.CaptionLabel.setObjectName(u"CaptionLabel")

        self.verticalLayout_3.addWidget(self.CaptionLabel)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.margin_spin = SpinBox(self.CardWidget_2)
        self.margin_spin.setObjectName(u"margin_spin")
        sizePolicy2.setHeightForWidth(self.margin_spin.sizePolicy().hasHeightForWidth())
        self.margin_spin.setSizePolicy(sizePolicy2)
        self.margin_spin.setMinimum(-15)

        self.horizontalLayout_2.addWidget(self.margin_spin)


        self.verticalLayout.addWidget(self.CardWidget_2)

        self.CardWidget_5 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_5.setObjectName(u"CardWidget_5")
        self.CardWidget_5.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_4 = QHBoxLayout(self.CardWidget_5)
        self.horizontalLayout_4.setSpacing(16)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.StrongBodyLabel_4 = StrongBodyLabel(self.CardWidget_5)
        self.StrongBodyLabel_4.setObjectName(u"StrongBodyLabel_4")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_4.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_4.setSizePolicy(sizePolicy1)

        self.verticalLayout_8.addWidget(self.StrongBodyLabel_4)

        self.CaptionLabel_4 = CaptionLabel(self.CardWidget_5)
        self.CaptionLabel_4.setObjectName(u"CaptionLabel_4")

        self.verticalLayout_8.addWidget(self.CaptionLabel_4)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.switch_auto_hide = SwitchButton(self.CardWidget_5)
        self.switch_auto_hide.setObjectName(u"switch_auto_hide")

        self.horizontalLayout_4.addWidget(self.switch_auto_hide)


        self.verticalLayout.addWidget(self.CardWidget_5)


        self.verticalLayout_9.addLayout(self.verticalLayout)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.SubtitleLabel_2 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_2.setObjectName(u"SubtitleLabel_2")

        self.verticalLayout_7.addWidget(self.SubtitleLabel_2)

        self.CardWidget_4 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_4.setObjectName(u"CardWidget_4")
        self.CardWidget_4.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_3 = QHBoxLayout(self.CardWidget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(16, 16, 16, 16)
        self.StrongBodyLabel_3 = StrongBodyLabel(self.CardWidget_4)
        self.StrongBodyLabel_3.setObjectName(u"StrongBodyLabel_3")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_3.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.StrongBodyLabel_3)

        self.switch_startup = SwitchButton(self.CardWidget_4)
        self.switch_startup.setObjectName(u"switch_startup")

        self.horizontalLayout_3.addWidget(self.switch_startup)


        self.verticalLayout_7.addWidget(self.CardWidget_4)


        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.SubtitleLabel_4 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_4.setObjectName(u"SubtitleLabel_4")

        self.verticalLayout_14.addWidget(self.SubtitleLabel_4)

        self.CardWidget_10 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_10.setObjectName(u"CardWidget_10")
        self.CardWidget_10.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_10 = QHBoxLayout(self.CardWidget_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.StrongBodyLabel_10 = StrongBodyLabel(self.CardWidget_10)
        self.StrongBodyLabel_10.setObjectName(u"StrongBodyLabel_10")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_10.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_10.setSizePolicy(sizePolicy1)

        self.verticalLayout_15.addWidget(self.StrongBodyLabel_10)

        self.CaptionLabel_9 = CaptionLabel(self.CardWidget_10)
        self.CaptionLabel_9.setObjectName(u"CaptionLabel_9")

        self.verticalLayout_15.addWidget(self.CaptionLabel_9)


        self.horizontalLayout_10.addLayout(self.verticalLayout_15)

        self.switch_multiple_programs = SwitchButton(self.CardWidget_10)
        self.switch_multiple_programs.setObjectName(u"switch_multiple_programs")

        self.horizontalLayout_10.addWidget(self.switch_multiple_programs)


        self.verticalLayout_14.addWidget(self.CardWidget_10)


        self.verticalLayout_9.addLayout(self.verticalLayout_14)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.SmoothScrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u9ad8\u7ea7\u9009\u9879", None))
        self.SubtitleLabel_3.setText(QCoreApplication.translate("Form", u"\u8bfe\u7a0b", None))
        self.StrongBodyLabel_6.setText(QCoreApplication.translate("Form", u"\u542f\u7528\u4e0a\u4e0b\u8bfe\u63d0\u9192", None))
        self.CaptionLabel_5.setText(QCoreApplication.translate("Form", u"\u542f\u7528\u540e\u5c06\u5728\u4e0a\u4e0b\u8bfe\u65f6\u7f6e\u9876\u5f39\u7a97\u4e14\u53d1\u51fa\u63d0\u793a\u97f3\u63d0\u9192", None))
        self.switch_enable_toast.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.switch_enable_toast.setOffText(QCoreApplication.translate("Form", u"\u7981\u7528", None))
        self.StrongBodyLabel_7.setText(QCoreApplication.translate("Form", u"\u65f6\u5dee\u504f\u79fb", None))
        self.CaptionLabel_6.setText(QCoreApplication.translate("Form", u"\u4fee\u6b63\u7cfb\u7edf\u65f6\u95f4\u4e0e\u5b66\u6821\u94c3\u58f0\u7684\u65f6\u5dee", None))
        self.StrongBodyLabel_5.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u8bfe\u7a0b\u8868\u914d\u7f6e", None))
        self.CaptionLabel_2.setText(QCoreApplication.translate("Form", u"\u8bfe\u7a0b\u8868\u914d\u7f6e\u5c06\u5b58\u50a8\u4e8e \u672c\u8f6f\u4ef6\u6839\u76ee\u5f55\\config\\schedule \u4e0b", None))
        self.StrongBodyLabel_8.setText(QCoreApplication.translate("Form", u"\u542f\u7528 \u5355/\u53cc \u5468\u8bfe\u8868", None))
        self.CaptionLabel_8.setText(QCoreApplication.translate("Form", u"\u82e5\u8981\u542f\u7528\u6b64\u9009\u9879\uff0c\u9700\u8bbe\u5b9a\u5f00\u5b66\u65e5\u671f\u4ee5\u8ba1\u7b97", None))
        self.switch_enable_alt_schedule.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.switch_enable_alt_schedule.setOffText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
        self.StrongBodyLabel_9.setText(QCoreApplication.translate("Form", u"\u9009\u53d6\u5f00\u5b66\u65e5\u671f", None))
        self.CaptionLabel_7.setText(QCoreApplication.translate("Form", u"\u5c06\u7528\u4e8e\u8ba1\u7b97\u5355/\u53cc\u5468\uff0c\u5f00\u5b66\u65e5\u671f\u9700\u8bbe\u7f6e\u4e3a\u5f00\u5b66\u7b2c\u4e00\u5929\uff08\u5373\u5468\u4e00\uff09", None))
        self.set_start_date.setText(QCoreApplication.translate("Form", u"\u9009\u53d6\u5f00\u5b66\u65e5\u671f", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", u"\u5916\u89c2", None))
        self.StrongBodyLabel_2.setText(QCoreApplication.translate("Form", u"\u7f6e\u9876\u5c0f\u7ec4\u4ef6", None))
        self.CaptionLabel_3.setText(QCoreApplication.translate("Form", u"\u91cd\u542f\u540e\u751f\u6548", None))
        self.switch_pin_button.setOnText(QCoreApplication.translate("Form", u"\u7f6e\u9876", None))
        self.switch_pin_button.setOffText(QCoreApplication.translate("Form", u"\u4e0d\u7f6e\u9876", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Form", u"\u8fb9\u8ddd\u5927\u5c0f", None))
        self.CaptionLabel.setText(QCoreApplication.translate("Form", u"\u8bbe\u5b9a\u684c\u9762\u7ec4\u4ef6\u79bb\u5c4f\u5e55\u8fb9\u7f18\u7684\u5927\u5c0f\uff08\u5355\u4f4d\uff1apx\uff09", None))
        self.StrongBodyLabel_4.setText(QCoreApplication.translate("Form", u"\u4e0a\u8bfe\u65f6\u81ea\u52a8\u9690\u85cf", None))
        self.CaptionLabel_4.setText(QCoreApplication.translate("Form", u"\u5f53\u4e0a\u8bfe\u65f6\u81ea\u52a8\u6536\u8d77\u5c0f\u7ec4\u4ef6\uff0c\u4e0b\u8bfe\u540e\u5c55\u5f00    *\u5c06\u7981\u7528\u201c\u5355\u51fb\u81ea\u52a8\u9690\u85cf\u201d", None))
        self.switch_auto_hide.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.switch_auto_hide.setOffText(QCoreApplication.translate("Form", u"\u7981\u7528", None))
        self.SubtitleLabel_2.setText(QCoreApplication.translate("Form", u"\u542f\u52a8", None))
        self.StrongBodyLabel_3.setText(QCoreApplication.translate("Form", u"\u5f00\u673a\u81ea\u542f\u52a8", None))
        self.switch_startup.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.switch_startup.setOffText(QCoreApplication.translate("Form", u"\u7981\u7528", None))
        self.SubtitleLabel_4.setText(QCoreApplication.translate("Form", u"\u5176\u4ed6", None))
        self.StrongBodyLabel_10.setText(QCoreApplication.translate("Form", u"\u5141\u8bb8\u7a0b\u5e8f\u591a\u5f00", None))
        self.CaptionLabel_9.setText(QCoreApplication.translate("Form", u"\u7a0b\u5e8f\u591a\u5f00\u540e\u53ef\u80fd\u51fa\u73b0\u672a\u77e5\u7684\u95ee\u9898\uff0c\u8bf7\u8c28\u614e\u4f7f\u7528\u3002", None))
        self.switch_multiple_programs.setText(QCoreApplication.translate("Form", u"\u4e0d\u5141\u8bb8", None))
        self.switch_multiple_programs.setOnText(QCoreApplication.translate("Form", u"\u5141\u8bb8", None))
        self.switch_multiple_programs.setOffText(QCoreApplication.translate("Form", u"\u4e0d\u5141\u8bb8", None))
    # retranslateUi

