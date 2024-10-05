# -*- coding: utf-8 -*-

from PySide2.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide2.QtGui import QColor, QPixmap
from PySide2.QtWidgets import QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, QVBoxLayout
from qfluentwidgets import BodyLabel, CaptionLabel, PushButton, SubtitleLabel, TitleLabel


class Ui_About(object):

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(821, 651)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 24, 24, 24)
        self.TitleLabel = TitleLabel(Form)
        self.TitleLabel.setObjectName("TitleLabel")

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(48, 0, 48, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName("label")
        self.label.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(128, 128))
        self.label.setStyleSheet("")
        self.label.setPixmap(QPixmap("img/Logo.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.SubtitleLabel = SubtitleLabel(Form)
        self.SubtitleLabel.setObjectName("SubtitleLabel")
        self.SubtitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.SubtitleLabel)

        self.version = BodyLabel(Form)
        self.version.setObjectName("version")
        self.version.setAlignment(Qt.AlignCenter)
        self.version.setWordWrap(True)

        self.verticalLayout.addWidget(self.version)

        self.CaptionLabel_3 = CaptionLabel(Form)
        self.CaptionLabel_3.setObjectName("CaptionLabel_3")
        self.CaptionLabel_3.setAlignment(Qt.AlignCenter)
        self.CaptionLabel_3.setWordWrap(True)

        self.verticalLayout.addWidget(self.CaptionLabel_3)

        self.CaptionLabel = CaptionLabel(Form)
        self.CaptionLabel.setObjectName("CaptionLabel")
        self.CaptionLabel.setAlignment(Qt.AlignCenter)
        self.CaptionLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.CaptionLabel)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.button_github = PushButton(Form)
        self.button_github.setObjectName("button_github")
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
        self.button_bilibili.setObjectName("button_bilibili")
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
        self.CaptionLabel_2.setObjectName("CaptionLabel_2")
        self.CaptionLabel_2.setAlignment(Qt.AlignCenter)
        self.CaptionLabel_2.setProperty("lightColor", QColor(127, 127, 127))
        self.CaptionLabel_2.setProperty("darkColor", QColor(185, 185, 185))

        self.verticalLayout_2.addWidget(self.CaptionLabel_2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form"))
        self.TitleLabel.setText(QCoreApplication.translate("Form", "关于"))
        self.label.setText("")
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", "Class Widgets"))
        self.version.setText(QCoreApplication.translate("Form", "版本：1.1.5.6"))
        self.CaptionLabel_3.setText(QCoreApplication.translate("Form", "Class Widgets 是一款能显示当前课程的桌面组件App。其提供了直观的图形化课程表编辑和美观的桌面组件。"))
        self.CaptionLabel.setText(QCoreApplication.translate("Form", "此软件基于 PySide2 开发，其中特别引用 QFluentWidget 作为界面UI，根据协议采用 GPL-3.0 开源协议。\n由 RinLit 开发", None))
        self.button_github.setText(QCoreApplication.translate("Form", "此项目的 Github"))
        self.button_bilibili.setText(QCoreApplication.translate("Form", "我的 哔哩哔哩 主页"))
        self.CaptionLabel_2.setText(QCoreApplication.translate("Form", "Copyright © 2024 RinLit, All Rights Reversed."))

    # retranslateUi
