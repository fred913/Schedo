# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu-timeline_edit.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import ComboBox
from qfluentwidgets import PushButton
from qfluentwidgets import PrimaryPushButton
from qfluentwidgets import ToolButton
from qfluentwidgets import CardWidget
from qfluentwidgets import TimePicker
from qfluentwidgets import CaptionLabel
from qfluentwidgets import BodyLabel
from qfluentwidgets import StrongBodyLabel
from qfluentwidgets import SubtitleLabel
from qfluentwidgets import TitleLabel
from qfluentwidgets import SpinBox
from qfluentwidgets import ListWidget


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(715, 658)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 24, 24, 24)
        self.TitleLabel = TitleLabel(Form)
        self.TitleLabel.setObjectName(u"TitleLabel")

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.SubtitleLabel = SubtitleLabel(Form)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")

        self.horizontalLayout_5.addWidget(self.SubtitleLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CardWidget = CardWidget(Form)
        self.CardWidget.setObjectName(u"CardWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CardWidget.sizePolicy().hasHeightForWidth())
        self.CardWidget.setSizePolicy(sizePolicy)
        self.CardWidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.CardWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(16, 16, 16, 16)
        self.StrongBodyLabel = StrongBodyLabel(self.CardWidget)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")

        self.horizontalLayout_2.addWidget(self.StrongBodyLabel)

        self.morningStartTime = TimePicker(self.CardWidget)
        self.morningStartTime.setObjectName(u"morningStartTime")
        self.morningStartTime.setSecondVisible(False)

        self.horizontalLayout_2.addWidget(self.morningStartTime)


        self.verticalLayout.addWidget(self.CardWidget)

        self.CardWidget_2 = CardWidget(Form)
        self.CardWidget_2.setObjectName(u"CardWidget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.CardWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(16, 16, 16, 16)
        self.StrongBodyLabel_2 = StrongBodyLabel(self.CardWidget_2)
        self.StrongBodyLabel_2.setObjectName(u"StrongBodyLabel_2")

        self.horizontalLayout_3.addWidget(self.StrongBodyLabel_2)

        self.afternoonStartTime = TimePicker(self.CardWidget_2)
        self.afternoonStartTime.setObjectName(u"afternoonStartTime")

        self.horizontalLayout_3.addWidget(self.afternoonStartTime)


        self.verticalLayout.addWidget(self.CardWidget_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.tips = CaptionLabel(Form)
        self.tips.setObjectName(u"tips")
        self.tips.setStyleSheet(u"FluentLabelBase {\n"
"    color: black;\n"
"	opacity: 0.5;\n"
"}\n"
"\n"
"HyperlinkLabel {\n"
"    color: #009faa;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=true] {\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"HyperlinkLabel[underline=false] {\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"HyperlinkLabel:hover {\n"
"    color: #007780;\n"
"}\n"
"\n"
"HyperlinkLabel:pressed {\n"
"    color: #00a7b3;\n"
"}\n"
"FluentLabelBase{color:#ff000000}")
        self.tips.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.tips)

        self.timeline_list = ListWidget(Form)
        self.timeline_list.setObjectName(u"timeline_list")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.timeline_list.sizePolicy().hasHeightForWidth())
        self.timeline_list.setSizePolicy(sizePolicy1)
        self.timeline_list.setDragDropMode(QAbstractItemView.InternalMove)
        self.timeline_list.setDefaultDropAction(Qt.MoveAction)

        self.verticalLayout_2.addWidget(self.timeline_list)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BodyLabel_2 = BodyLabel(Form)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.BodyLabel_2.sizePolicy().hasHeightForWidth())
        self.BodyLabel_2.setSizePolicy(sizePolicy2)
        self.BodyLabel_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.BodyLabel_2)

        self.class_activity = ComboBox(Form)
        self.class_activity.setObjectName(u"class_activity")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.class_activity.sizePolicy().hasHeightForWidth())
        self.class_activity.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.class_activity)

        self.BodyLabel_3 = BodyLabel(Form)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")
        sizePolicy2.setHeightForWidth(self.BodyLabel_3.sizePolicy().hasHeightForWidth())
        self.BodyLabel_3.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.BodyLabel_3)

        self.time_period = ComboBox(Form)
        self.time_period.setObjectName(u"time_period")

        self.horizontalLayout.addWidget(self.time_period)

        self.BodyLabel = BodyLabel(Form)
        self.BodyLabel.setObjectName(u"BodyLabel")
        sizePolicy2.setHeightForWidth(self.BodyLabel.sizePolicy().hasHeightForWidth())
        self.BodyLabel.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.BodyLabel)

        self.spin_time = SpinBox(Form)
        self.spin_time.setObjectName(u"spin_time")
        self.spin_time.setMaximum(999)
        self.spin_time.setSingleStep(5)
        self.spin_time.setValue(40)

        self.horizontalLayout.addWidget(self.spin_time)

        self.add_button = ToolButton(Form)
        self.add_button.setObjectName(u"add_button")

        self.horizontalLayout.addWidget(self.add_button)

        self.edit_button = ToolButton(Form)
        self.edit_button.setObjectName(u"edit_button")

        self.horizontalLayout.addWidget(self.edit_button)

        self.delete_button = ToolButton(Form)
        self.delete_button.setObjectName(u"delete_button")

        self.horizontalLayout.addWidget(self.delete_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.save = PrimaryPushButton(Form)
        self.save.setObjectName(u"save")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.save.sizePolicy().hasHeightForWidth())
        self.save.setSizePolicy(sizePolicy4)
        self.save.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.save)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u65f6\u95f4\u7ebf\u7f16\u8f91", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", u"\u65f6\u95f4", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Form", u"\u4e0a\u5348\u8d77\u59cb\u65f6\u95f4", None))
        self.StrongBodyLabel_2.setText(QCoreApplication.translate("Form", u"\u4e0b\u5348\u8d77\u59cb\u65f6\u95f4", None))
        self.tips.setText(QCoreApplication.translate("Form", u"\u8fd8\u672a\u6dfb\u52a0\u4efb\u4f55\u65f6\u95f4\u7ebf", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Form", u"\u6d3b\u52a8\u7c7b\u578b", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"\u65f6\u6bb5", None))
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"\u65f6\u957f\uff08\u5206\u949f\uff09", None))
        self.save.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
    # retranslateUi
