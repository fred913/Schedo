# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu-custom.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import PushButton
from qfluentwidgets import PrimaryPushButton
from qfluentwidgets import SwitchButton
from qfluentwidgets import CardWidget
from qfluentwidgets import SmoothScrollArea
from qfluentwidgets import CalendarPicker
from qfluentwidgets import CaptionLabel
from qfluentwidgets import StrongBodyLabel
from qfluentwidgets import SubtitleLabel
from qfluentwidgets import TitleLabel
from qfluentwidgets import LineEdit
from qfluentwidgets import ListWidget


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(901, 750)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 24, 24, 24)
        self.TitleLabel = TitleLabel(Form)
        self.TitleLabel.setObjectName(u"TitleLabel")

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.SubtitleLabel = SubtitleLabel(Form)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")

        self.verticalLayout_2.addWidget(self.SubtitleLabel)

        self.widgets_preview = QHBoxLayout()
        self.widgets_preview.setSpacing(0)
        self.widgets_preview.setObjectName(u"widgets_preview")
        self.widgets_preview.setSizeConstraint(QLayout.SetFixedSize)

        self.verticalLayout_2.addLayout(self.widgets_preview)

        self.CaptionLabel_3 = CaptionLabel(Form)
        self.CaptionLabel_3.setObjectName(u"CaptionLabel_3")
        self.CaptionLabel_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.CaptionLabel_3)

        self.SmoothScrollArea = SmoothScrollArea(Form)
        self.SmoothScrollArea.setObjectName(u"SmoothScrollArea")
        self.SmoothScrollArea.setStyleSheet(u"background: transparent; border: none")
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 853, 491))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widgets_list = ListWidget(self.scrollAreaWidgetContents)
        self.widgets_list.setObjectName(u"widgets_list")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgets_list.sizePolicy().hasHeightForWidth())
        self.widgets_list.setSizePolicy(sizePolicy)
        self.widgets_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.widgets_list.setDragDropMode(QAbstractItemView.InternalMove)
        self.widgets_list.setDefaultDropAction(Qt.MoveAction)

        self.verticalLayout_9.addWidget(self.widgets_list)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.SubtitleLabel_3 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_3.setObjectName(u"SubtitleLabel_3")
        self.SubtitleLabel_3.setProperty("pixelFontSize", 18)

        self.verticalLayout_5.addWidget(self.SubtitleLabel_3)

        self.CardWidget_6 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_6.setObjectName(u"CardWidget_6")
        self.CardWidget_6.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_6 = QHBoxLayout(self.CardWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(16, 16, 16, 16)
        self.StrongBodyLabel_6 = StrongBodyLabel(self.CardWidget_6)
        self.StrongBodyLabel_6.setObjectName(u"StrongBodyLabel_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_6.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_6.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.StrongBodyLabel_6)

        self.switch_countdown_custom = SwitchButton(self.CardWidget_6)
        self.switch_countdown_custom.setObjectName(u"switch_countdown_custom")

        self.horizontalLayout_6.addWidget(self.switch_countdown_custom)


        self.verticalLayout_5.addWidget(self.CardWidget_6)

        self.CardWidget = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget.setObjectName(u"CardWidget")
        self.CardWidget.setMinimumSize(QSize(0, 70))
        self.horizontalLayout = QHBoxLayout(self.CardWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.StrongBodyLabel = StrongBodyLabel(self.CardWidget)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")

        self.verticalLayout.addWidget(self.StrongBodyLabel)

        self.CaptionLabel = CaptionLabel(self.CardWidget)
        self.CaptionLabel.setObjectName(u"CaptionLabel")

        self.verticalLayout.addWidget(self.CaptionLabel)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.set_wcc_title = LineEdit(self.CardWidget)
        self.set_wcc_title.setObjectName(u"set_wcc_title")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.set_wcc_title.sizePolicy().hasHeightForWidth())
        self.set_wcc_title.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.set_wcc_title)


        self.verticalLayout_5.addWidget(self.CardWidget)

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

        self.set_countdown_date = CalendarPicker(self.CardWidget_3)
        self.set_countdown_date.setObjectName(u"set_countdown_date")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.set_countdown_date.sizePolicy().hasHeightForWidth())
        self.set_countdown_date.setSizePolicy(sizePolicy3)
        self.set_countdown_date.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_5.addWidget(self.set_countdown_date)


        self.verticalLayout_5.addWidget(self.CardWidget_3)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.SmoothScrollArea)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.save_config = PrimaryPushButton(Form)
        self.save_config.setObjectName(u"save_config")
        sizePolicy2.setHeightForWidth(self.save_config.sizePolicy().hasHeightForWidth())
        self.save_config.setSizePolicy(sizePolicy2)
        self.save_config.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.save_config)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", u"\u5c0f\u7ec4\u4ef6", None))
        self.CaptionLabel_3.setText(QCoreApplication.translate("Form", u"*\u5bf9\u5c0f\u7ec4\u4ef6\u7684\u663e\u793a\u3001\u9690\u85cf\u548c\u62d6\u62fd\u64cd\u4f5c\u5c06\u5728\u91cd\u542f\u540e\u751f\u6548\u3002", None))
        self.SubtitleLabel_3.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u5012\u8ba1\u65f6", None))
        self.StrongBodyLabel_6.setText(QCoreApplication.translate("Form", u"\u662f\u5426\u663e\u793a", None))
        self.switch_countdown_custom.setOnText(QCoreApplication.translate("Form", u"\u663e\u793a", None))
        self.switch_countdown_custom.setOffText(QCoreApplication.translate("Form", u"\u9690\u85cf", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u6587\u672c", None))
        self.CaptionLabel.setText(QCoreApplication.translate("Form", u"\u5c06\u4f1a\u663e\u793a\uff08\u8ddd\u79bb \"\u4f60\u6240\u8f93\u5165\u7684\u6587\u672c\" \u8fd8\u6709 \uff09", None))
        self.set_wcc_title.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u5012\u8ba1\u65f6\u6807\u9898", None))
        self.StrongBodyLabel_5.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u65e5\u671f", None))
        self.CaptionLabel_2.setText(QCoreApplication.translate("Form", u"\u65e5\u671f\u5c06\u4f1a\u7528\u4e8e\u5012\u8ba1\u65f6", None))
        self.set_countdown_date.setText(QCoreApplication.translate("Form", u"\u9009\u5b9a\u4e00\u4e2a\u65e5\u671f", None))
        self.save_config.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u5e03\u5c40", None))
    # retranslateUi

