# -*- coding: utf-8 -*-

from PySide2.QtCore import QCoreApplication, QMetaObject, QRect, QSize
from PySide2.QtWidgets import QHBoxLayout, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget
from qfluentwidgets import CaptionLabel, CardWidget, PushButton, SmoothScrollArea, StrongBodyLabel, SubtitleLabel, TitleLabel


class Ui_Configs(object):

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(721, 814)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 24, 24, 24)
        self.TitleLabel = TitleLabel(Form)
        self.TitleLabel.setObjectName("TitleLabel")

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.SmoothScrollArea = SmoothScrollArea(Form)
        self.SmoothScrollArea.setObjectName("SmoothScrollArea")
        self.SmoothScrollArea.setStyleSheet("background: transparent; border: none")
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 673, 709))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.SubtitleLabel_3 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_3.setObjectName("SubtitleLabel_3")

        self.verticalLayout_5.addWidget(self.SubtitleLabel_3)

        self.CardWidget_6 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_6.setObjectName("CardWidget_6")
        self.CardWidget_6.setMinimumSize(QSize(0, 60))
        self.horizontalLayout_6 = QHBoxLayout(self.CardWidget_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.StrongBodyLabel_6 = StrongBodyLabel(self.CardWidget_6)
        self.StrongBodyLabel_6.setObjectName("StrongBodyLabel_6")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StrongBodyLabel_6.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_6.setSizePolicy(sizePolicy)

        self.verticalLayout_10.addWidget(self.StrongBodyLabel_6)

        self.CaptionLabel_5 = CaptionLabel(self.CardWidget_6)
        self.CaptionLabel_5.setObjectName("CaptionLabel_5")

        self.verticalLayout_10.addWidget(self.CaptionLabel_5)

        self.horizontalLayout_6.addLayout(self.verticalLayout_10)

        self.im_schedule = PushButton(self.CardWidget_6)
        self.im_schedule.setObjectName("im_schedule")

        self.horizontalLayout_6.addWidget(self.im_schedule)

        self.verticalLayout_5.addWidget(self.CardWidget_6)

        self.CardWidget_8 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_8.setObjectName("CardWidget_8")
        self.CardWidget_8.setMinimumSize(QSize(0, 60))
        self.horizontalLayout_8 = QHBoxLayout(self.CardWidget_8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.StrongBodyLabel_8 = StrongBodyLabel(self.CardWidget_8)
        self.StrongBodyLabel_8.setObjectName("StrongBodyLabel_8")
        sizePolicy.setHeightForWidth(self.StrongBodyLabel_8.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_8.setSizePolicy(sizePolicy)

        self.verticalLayout_13.addWidget(self.StrongBodyLabel_8)

        self.CaptionLabel_8 = CaptionLabel(self.CardWidget_8)
        self.CaptionLabel_8.setObjectName("CaptionLabel_8")

        self.verticalLayout_13.addWidget(self.CaptionLabel_8)

        self.horizontalLayout_8.addLayout(self.verticalLayout_13)

        self.ex_schedule = PushButton(self.CardWidget_8)
        self.ex_schedule.setObjectName("ex_schedule")

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
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form"))
        self.TitleLabel.setText(QCoreApplication.translate("Form", "配置文件"))
        self.SubtitleLabel_3.setText(QCoreApplication.translate("Form", "课程表"))
        self.StrongBodyLabel_6.setText(QCoreApplication.translate("Form", "导入 Class Widgets 课程表"))
        self.CaptionLabel_5.setText(QCoreApplication.translate("Form", "需导入从其他 Class Widgets 导出的课程表"))
        self.im_schedule.setText(QCoreApplication.translate("Form", "导入课程表"))
        self.StrongBodyLabel_8.setText(QCoreApplication.translate("Form", "导出 Class Widgets 课程表"))
        self.CaptionLabel_8.setText(QCoreApplication.translate("Form", "将当前使用的课程表文件 (.json) 导出"))
        self.ex_schedule.setText(QCoreApplication.translate("Form", "导出课程表"))

    # retranslateUi
