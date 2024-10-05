# -*- coding: utf-8 -*-

from PySide2.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide2.QtWidgets import QAbstractItemView, QAbstractScrollArea, QHBoxLayout, QLayout, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget
from qfluentwidgets import (CalendarPicker, CaptionLabel, CardWidget, LineEdit, ListWidget, PrimaryPushButton, SmoothScrollArea, StrongBodyLabel,
                            SubtitleLabel, SwitchButton, TitleLabel)


class Ui_Custom(object):

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(901, 750)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 24, 24, 24)
        self.TitleLabel = TitleLabel(Form)
        self.TitleLabel.setObjectName("TitleLabel")

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.SubtitleLabel = SubtitleLabel(Form)
        self.SubtitleLabel.setObjectName("SubtitleLabel")

        self.verticalLayout_2.addWidget(self.SubtitleLabel)

        self.widgets_preview = QHBoxLayout()
        self.widgets_preview.setSpacing(0)
        self.widgets_preview.setObjectName("widgets_preview")
        self.widgets_preview.setSizeConstraint(QLayout.SetFixedSize)

        self.verticalLayout_2.addLayout(self.widgets_preview)

        self.CaptionLabel_3 = CaptionLabel(Form)
        self.CaptionLabel_3.setObjectName("CaptionLabel_3")
        self.CaptionLabel_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.CaptionLabel_3)

        self.SmoothScrollArea = SmoothScrollArea(Form)
        self.SmoothScrollArea.setObjectName("SmoothScrollArea")
        self.SmoothScrollArea.setStyleSheet("background: transparent; border: none")
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 853, 491))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widgets_list = ListWidget(self.scrollAreaWidgetContents)
        self.widgets_list.setObjectName("widgets_list")
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
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.SubtitleLabel_3 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_3.setObjectName("SubtitleLabel_3")
        self.SubtitleLabel_3.setProperty("pixelFontSize", 18)

        self.verticalLayout_5.addWidget(self.SubtitleLabel_3)

        self.CardWidget_6 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_6.setObjectName("CardWidget_6")
        self.CardWidget_6.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_6 = QHBoxLayout(self.CardWidget_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(16, 16, 16, 16)
        self.StrongBodyLabel_6 = StrongBodyLabel(self.CardWidget_6)
        self.StrongBodyLabel_6.setObjectName("StrongBodyLabel_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_6.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_6.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.StrongBodyLabel_6)

        self.switch_countdown_custom = SwitchButton(self.CardWidget_6)
        self.switch_countdown_custom.setObjectName("switch_countdown_custom")

        self.horizontalLayout_6.addWidget(self.switch_countdown_custom)

        self.verticalLayout_5.addWidget(self.CardWidget_6)

        self.CardWidget = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget.setObjectName("CardWidget")
        self.CardWidget.setMinimumSize(QSize(0, 70))
        self.horizontalLayout = QHBoxLayout(self.CardWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.StrongBodyLabel = StrongBodyLabel(self.CardWidget)
        self.StrongBodyLabel.setObjectName("StrongBodyLabel")

        self.verticalLayout.addWidget(self.StrongBodyLabel)

        self.CaptionLabel = CaptionLabel(self.CardWidget)
        self.CaptionLabel.setObjectName("CaptionLabel")

        self.verticalLayout.addWidget(self.CaptionLabel)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.set_wcc_title = LineEdit(self.CardWidget)
        self.set_wcc_title.setObjectName("set_wcc_title")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.set_wcc_title.sizePolicy().hasHeightForWidth())
        self.set_wcc_title.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.set_wcc_title)

        self.verticalLayout_5.addWidget(self.CardWidget)

        self.CardWidget_3 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_3.setObjectName("CardWidget_3")
        self.CardWidget_3.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_5 = QHBoxLayout(self.CardWidget_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.StrongBodyLabel_5 = StrongBodyLabel(self.CardWidget_3)
        self.StrongBodyLabel_5.setObjectName("StrongBodyLabel_5")

        self.verticalLayout_6.addWidget(self.StrongBodyLabel_5)

        self.CaptionLabel_2 = CaptionLabel(self.CardWidget_3)
        self.CaptionLabel_2.setObjectName("CaptionLabel_2")

        self.verticalLayout_6.addWidget(self.CaptionLabel_2)

        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.set_countdown_date = CalendarPicker(self.CardWidget_3)
        self.set_countdown_date.setObjectName("set_countdown_date")
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
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.save_config = PrimaryPushButton(Form)
        self.save_config.setObjectName("save_config")
        sizePolicy2.setHeightForWidth(self.save_config.sizePolicy().hasHeightForWidth())
        self.save_config.setSizePolicy(sizePolicy2)
        self.save_config.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.save_config)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form"))
        self.TitleLabel.setText(QCoreApplication.translate("Form", "自定义"))
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", "小组件"))
        self.CaptionLabel_3.setText(QCoreApplication.translate("Form", "*对小组件的显示、隐藏和拖拽操作将在重启后生效。"))
        self.SubtitleLabel_3.setText(QCoreApplication.translate("Form", "自定义倒计时"))
        self.StrongBodyLabel_6.setText(QCoreApplication.translate("Form", "是否显示"))
        self.switch_countdown_custom.setOnText(QCoreApplication.translate("Form", "显示"))
        self.switch_countdown_custom.setOffText(QCoreApplication.translate("Form", "隐藏"))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Form", "自定义文本"))
        self.CaptionLabel.setText(QCoreApplication.translate("Form", "将会显示（距离 \"你所输入的文本\" 还有 ）"))
        self.set_wcc_title.setPlaceholderText(QCoreApplication.translate("Form", "输入倒计时标题"))
        self.StrongBodyLabel_5.setText(QCoreApplication.translate("Form", "选择日期"))
        self.CaptionLabel_2.setText(QCoreApplication.translate("Form", "日期将会用于倒计时"))
        self.set_countdown_date.setText(QCoreApplication.translate("Form", "选定一个日期"))
        self.save_config.setText(QCoreApplication.translate("Form", "保存布局"))

    # retranslateUi
