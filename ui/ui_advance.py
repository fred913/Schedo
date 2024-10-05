# -*- coding: utf-8 -*-

from PySide2.QtCore import QCoreApplication, QMetaObject, QRect, QSize
from PySide2.QtWidgets import QHBoxLayout, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget
from qfluentwidgets import (CalendarPicker, CaptionLabel, CardWidget, ComboBox, LineEdit, SmoothScrollArea, SpinBox, StrongBodyLabel, SubtitleLabel,
                            SwitchButton, TitleLabel)


class Ui_Advance(object):

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(745, 1172)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 697, 1067))
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
        self.CardWidget_6.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_6 = QHBoxLayout(self.CardWidget_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.StrongBodyLabel_6 = StrongBodyLabel(self.CardWidget_6)
        self.StrongBodyLabel_6.setObjectName("StrongBodyLabel_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_6.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_6.setSizePolicy(sizePolicy1)

        self.verticalLayout_10.addWidget(self.StrongBodyLabel_6)

        self.CaptionLabel_5 = CaptionLabel(self.CardWidget_6)
        self.CaptionLabel_5.setObjectName("CaptionLabel_5")

        self.verticalLayout_10.addWidget(self.CaptionLabel_5)

        self.horizontalLayout_6.addLayout(self.verticalLayout_10)

        self.switch_enable_toast = SwitchButton(self.CardWidget_6)
        self.switch_enable_toast.setObjectName("switch_enable_toast")

        self.horizontalLayout_6.addWidget(self.switch_enable_toast)

        self.verticalLayout_5.addWidget(self.CardWidget_6)

        self.CardWidget_7 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_7.setObjectName("CardWidget_7")
        self.CardWidget_7.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_7 = QHBoxLayout(self.CardWidget_7)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.StrongBodyLabel_7 = StrongBodyLabel(self.CardWidget_7)
        self.StrongBodyLabel_7.setObjectName("StrongBodyLabel_7")

        self.verticalLayout_11.addWidget(self.StrongBodyLabel_7)

        self.CaptionLabel_6 = CaptionLabel(self.CardWidget_7)
        self.CaptionLabel_6.setObjectName("CaptionLabel_6")

        self.verticalLayout_11.addWidget(self.CaptionLabel_6)

        self.horizontalLayout_7.addLayout(self.verticalLayout_11)

        self.offset_spin = SpinBox(self.CardWidget_7)
        self.offset_spin.setObjectName("offset_spin")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.offset_spin.sizePolicy().hasHeightForWidth())
        self.offset_spin.setSizePolicy(sizePolicy2)
        self.offset_spin.setMinimum(-99)

        self.horizontalLayout_7.addWidget(self.offset_spin)

        self.verticalLayout_5.addWidget(self.CardWidget_7)

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

        self.conf_name = LineEdit(self.CardWidget_3)
        self.conf_name.setObjectName("conf_name")
        sizePolicy2.setHeightForWidth(self.conf_name.sizePolicy().hasHeightForWidth())
        self.conf_name.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.conf_name)

        self.conf_combo = ComboBox(self.CardWidget_3)
        self.conf_combo.setObjectName("conf_combo")
        sizePolicy2.setHeightForWidth(self.conf_combo.sizePolicy().hasHeightForWidth())
        self.conf_combo.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.conf_combo)

        self.verticalLayout_5.addWidget(self.CardWidget_3)

        self.CardWidget_8 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_8.setObjectName("CardWidget_8")
        self.CardWidget_8.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_8 = QHBoxLayout(self.CardWidget_8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.StrongBodyLabel_8 = StrongBodyLabel(self.CardWidget_8)
        self.StrongBodyLabel_8.setObjectName("StrongBodyLabel_8")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_8.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_8.setSizePolicy(sizePolicy1)

        self.verticalLayout_13.addWidget(self.StrongBodyLabel_8)

        self.CaptionLabel_8 = CaptionLabel(self.CardWidget_8)
        self.CaptionLabel_8.setObjectName("CaptionLabel_8")

        self.verticalLayout_13.addWidget(self.CaptionLabel_8)

        self.horizontalLayout_8.addLayout(self.verticalLayout_13)

        self.switch_enable_alt_schedule = SwitchButton(self.CardWidget_8)
        self.switch_enable_alt_schedule.setObjectName("switch_enable_alt_schedule")

        self.horizontalLayout_8.addWidget(self.switch_enable_alt_schedule)

        self.verticalLayout_5.addWidget(self.CardWidget_8)

        self.CardWidget_9 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_9.setObjectName("CardWidget_9")
        self.CardWidget_9.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_9 = QHBoxLayout(self.CardWidget_9)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.StrongBodyLabel_9 = StrongBodyLabel(self.CardWidget_9)
        self.StrongBodyLabel_9.setObjectName("StrongBodyLabel_9")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_9.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_9.setSizePolicy(sizePolicy1)

        self.verticalLayout_12.addWidget(self.StrongBodyLabel_9)

        self.CaptionLabel_7 = CaptionLabel(self.CardWidget_9)
        self.CaptionLabel_7.setObjectName("CaptionLabel_7")

        self.verticalLayout_12.addWidget(self.CaptionLabel_7)

        self.horizontalLayout_9.addLayout(self.verticalLayout_12)

        self.set_start_date = CalendarPicker(self.CardWidget_9)
        self.set_start_date.setObjectName("set_start_date")

        self.horizontalLayout_9.addWidget(self.set_start_date)

        self.verticalLayout_5.addWidget(self.CardWidget_9)

        self.verticalLayout_9.addLayout(self.verticalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SubtitleLabel = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel.setObjectName("SubtitleLabel")

        self.verticalLayout.addWidget(self.SubtitleLabel)

        self.CardWidget = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget.setObjectName("CardWidget")
        self.CardWidget.setMinimumSize(QSize(0, 70))
        self.horizontalLayout = QHBoxLayout(self.CardWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.StrongBodyLabel_2 = StrongBodyLabel(self.CardWidget)
        self.StrongBodyLabel_2.setObjectName("StrongBodyLabel_2")

        self.verticalLayout_4.addWidget(self.StrongBodyLabel_2)

        self.CaptionLabel_3 = CaptionLabel(self.CardWidget)
        self.CaptionLabel_3.setObjectName("CaptionLabel_3")
        sizePolicy1.setHeightForWidth(self.CaptionLabel_3.sizePolicy().hasHeightForWidth())
        self.CaptionLabel_3.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.CaptionLabel_3)

        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.switch_pin_button = SwitchButton(self.CardWidget)
        self.switch_pin_button.setObjectName("switch_pin_button")

        self.horizontalLayout.addWidget(self.switch_pin_button)

        self.verticalLayout.addWidget(self.CardWidget)

        self.CardWidget_2 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_2.setObjectName("CardWidget_2")
        self.CardWidget_2.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_2 = QHBoxLayout(self.CardWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.StrongBodyLabel = StrongBodyLabel(self.CardWidget_2)
        self.StrongBodyLabel.setObjectName("StrongBodyLabel")

        self.verticalLayout_3.addWidget(self.StrongBodyLabel)

        self.CaptionLabel = CaptionLabel(self.CardWidget_2)
        self.CaptionLabel.setObjectName("CaptionLabel")

        self.verticalLayout_3.addWidget(self.CaptionLabel)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.margin_spin = SpinBox(self.CardWidget_2)
        self.margin_spin.setObjectName("margin_spin")
        sizePolicy2.setHeightForWidth(self.margin_spin.sizePolicy().hasHeightForWidth())
        self.margin_spin.setSizePolicy(sizePolicy2)
        self.margin_spin.setMinimum(-15)

        self.horizontalLayout_2.addWidget(self.margin_spin)

        self.verticalLayout.addWidget(self.CardWidget_2)

        self.CardWidget_5 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_5.setObjectName("CardWidget_5")
        self.CardWidget_5.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_4 = QHBoxLayout(self.CardWidget_5)
        self.horizontalLayout_4.setSpacing(16)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.StrongBodyLabel_4 = StrongBodyLabel(self.CardWidget_5)
        self.StrongBodyLabel_4.setObjectName("StrongBodyLabel_4")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_4.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_4.setSizePolicy(sizePolicy1)

        self.verticalLayout_8.addWidget(self.StrongBodyLabel_4)

        self.CaptionLabel_4 = CaptionLabel(self.CardWidget_5)
        self.CaptionLabel_4.setObjectName("CaptionLabel_4")

        self.verticalLayout_8.addWidget(self.CaptionLabel_4)

        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.switch_auto_hide = SwitchButton(self.CardWidget_5)
        self.switch_auto_hide.setObjectName("switch_auto_hide")

        self.horizontalLayout_4.addWidget(self.switch_auto_hide)

        self.verticalLayout.addWidget(self.CardWidget_5)

        self.verticalLayout_9.addLayout(self.verticalLayout)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.SubtitleLabel_2 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_2.setObjectName("SubtitleLabel_2")

        self.verticalLayout_7.addWidget(self.SubtitleLabel_2)

        self.CardWidget_4 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_4.setObjectName("CardWidget_4")
        self.CardWidget_4.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_3 = QHBoxLayout(self.CardWidget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(16, 16, 16, 16)
        self.StrongBodyLabel_3 = StrongBodyLabel(self.CardWidget_4)
        self.StrongBodyLabel_3.setObjectName("StrongBodyLabel_3")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_3.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.StrongBodyLabel_3)

        self.switch_startup = SwitchButton(self.CardWidget_4)
        self.switch_startup.setObjectName("switch_startup")

        self.horizontalLayout_3.addWidget(self.switch_startup)

        self.verticalLayout_7.addWidget(self.CardWidget_4)

        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.SubtitleLabel_4 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_4.setObjectName("SubtitleLabel_4")

        self.verticalLayout_14.addWidget(self.SubtitleLabel_4)

        self.CardWidget_10 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_10.setObjectName("CardWidget_10")
        self.CardWidget_10.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_10 = QHBoxLayout(self.CardWidget_10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.StrongBodyLabel_10 = StrongBodyLabel(self.CardWidget_10)
        self.StrongBodyLabel_10.setObjectName("StrongBodyLabel_10")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel_10.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel_10.setSizePolicy(sizePolicy1)

        self.verticalLayout_15.addWidget(self.StrongBodyLabel_10)

        self.CaptionLabel_9 = CaptionLabel(self.CardWidget_10)
        self.CaptionLabel_9.setObjectName("CaptionLabel_9")

        self.verticalLayout_15.addWidget(self.CaptionLabel_9)

        self.horizontalLayout_10.addLayout(self.verticalLayout_15)

        self.switch_multiple_programs = SwitchButton(self.CardWidget_10)
        self.switch_multiple_programs.setObjectName("switch_multiple_programs")

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
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form"))
        self.TitleLabel.setText(QCoreApplication.translate("Form", "高级选项"))
        self.SubtitleLabel_3.setText(QCoreApplication.translate("Form", "课程"))
        self.StrongBodyLabel_6.setText(QCoreApplication.translate("Form", "启用上下课提醒"))
        self.CaptionLabel_5.setText(QCoreApplication.translate("Form", "启用后将在上下课时置顶弹窗且发出提示音提醒"))
        self.switch_enable_toast.setOnText(QCoreApplication.translate("Form", "启用"))
        self.switch_enable_toast.setOffText(QCoreApplication.translate("Form", "禁用"))
        self.StrongBodyLabel_7.setText(QCoreApplication.translate("Form", "时差偏移"))
        self.CaptionLabel_6.setText(QCoreApplication.translate("Form", "修正系统时间与学校铃声的时差"))
        self.StrongBodyLabel_5.setText(QCoreApplication.translate("Form", "选择课程表配置"))
        self.CaptionLabel_2.setText(QCoreApplication.translate("Form", "课程表配置将存储于 本软件根目录\\config\\schedule 下"))
        self.StrongBodyLabel_8.setText(QCoreApplication.translate("Form", "启用 单/双 周课表"))
        self.CaptionLabel_8.setText(QCoreApplication.translate("Form", "若要启用此选项，需设定开学日期以计算"))
        self.switch_enable_alt_schedule.setOnText(QCoreApplication.translate("Form", "启用"))
        self.switch_enable_alt_schedule.setOffText(QCoreApplication.translate("Form", "关闭"))
        self.StrongBodyLabel_9.setText(QCoreApplication.translate("Form", "选取开学日期"))
        self.CaptionLabel_7.setText(QCoreApplication.translate("Form", "将用于计算单/双周，开学日期需设置为开学第一天（即周一）"))
        self.set_start_date.setText(QCoreApplication.translate("Form", "选取开学日期"))
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", "外观"))
        self.StrongBodyLabel_2.setText(QCoreApplication.translate("Form", "置顶小组件"))
        self.CaptionLabel_3.setText(QCoreApplication.translate("Form", "重启后生效"))
        self.switch_pin_button.setOnText(QCoreApplication.translate("Form", "置顶"))
        self.switch_pin_button.setOffText(QCoreApplication.translate("Form", "不置顶"))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Form", "边距大小"))
        self.CaptionLabel.setText(QCoreApplication.translate("Form", "设定桌面组件离屏幕边缘的大小（单位：px）"))
        self.StrongBodyLabel_4.setText(QCoreApplication.translate("Form", "上课时自动隐藏"))
        self.CaptionLabel_4.setText(QCoreApplication.translate("Form", "当上课时自动收起小组件，下课后展开    *将禁用“单击自动隐藏”"))
        self.switch_auto_hide.setOnText(QCoreApplication.translate("Form", "启用"))
        self.switch_auto_hide.setOffText(QCoreApplication.translate("Form", "禁用"))
        self.SubtitleLabel_2.setText(QCoreApplication.translate("Form", "启动"))
        self.StrongBodyLabel_3.setText(QCoreApplication.translate("Form", "开机自启动"))
        self.switch_startup.setOnText(QCoreApplication.translate("Form", "启用"))
        self.switch_startup.setOffText(QCoreApplication.translate("Form", "禁用"))
        self.SubtitleLabel_4.setText(QCoreApplication.translate("Form", "其他"))
        self.StrongBodyLabel_10.setText(QCoreApplication.translate("Form", "允许程序多开"))
        self.CaptionLabel_9.setText(QCoreApplication.translate("Form", "程序多开后可能出现未知的问题，请谨慎使用。"))
        self.switch_multiple_programs.setText(QCoreApplication.translate("Form", "不允许"))
        self.switch_multiple_programs.setOnText(QCoreApplication.translate("Form", "允许"))
        self.switch_multiple_programs.setOffText(QCoreApplication.translate("Form", "不允许"))

    # retranslateUi
