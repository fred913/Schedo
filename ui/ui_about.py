# -*- coding: utf-8 -*-

from PySide2.QtCore import QCoreApplication, QObject, QSize, Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QHBoxLayout, QSizePolicy, QVBoxLayout, QWidget
from qfluentwidgets import BodyLabel, PushButton, SubtitleLabel, TitleLabel

from assets import get_img_dir


class MarkupParagraph:

    def __init__(self, txt: str):
        self.txt = txt


class MarkupTitle:

    def __init__(self, txt: str):
        self.txt = txt


class MarkupSubtitle:

    def __init__(self, txt: str):
        self.txt = txt


class MarkupImage:

    def __init__(self, img_path: str):
        self.img_path = img_path


class MarkupButton:

    def __init__(self, text: str, callback):
        self.text = text
        self.callback = callback


class Ui_About(object):

    def __init__(self):
        self.content = []  # 存储文档树

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")

        Form.resize(800, 600)

        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 24, 24, 24)

        self.version = BodyLabel(Form)
        self.version.setObjectName("version")
        self.version.setAlignment(Qt.AlignCenter)
        self.version.setWordWrap(True)

        # Render the page initially
        self.render_page()

    def render_page(self):
        # Clear existing layout items
        while self.verticalLayout_2.count():
            item = self.verticalLayout_2.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        QCoreApplication.processEvents()

        self.content = [
            MarkupTitle(QCoreApplication.translate("Form", "关于")),
            MarkupSubtitle(QCoreApplication.translate("Form", "Schedo")),
            MarkupImage(str(get_img_dir() / "favicon.png")),
            MarkupParagraph(QCoreApplication.translate("Form", "版本：0.1.1")), self.version,
            MarkupParagraph(QCoreApplication.translate("Form", "Schedo 是一款开源的大屏课程表显示软件，基于 Python 3.8.10 和 PySide2 开发。")),
            MarkupParagraph(QCoreApplication.translate("Form", "此软件基于 PySide2 开发，使用 QFluentWidget 作为界面UI，采用 GPL-3.0 协议开源。")),
            MarkupParagraph(
                QCoreApplication.translate(
                    "Form",
                    "Schedo 原先是 Class-Widgets 的一个分支，后来由于 Schedo 开发者 (Sheng Fan, @fred913) 认为原作者的代码风格过于冗杂，现在 Schedo 以用户体验为根本，以全面、易用为目标，正逐步发展成为一个独立软件。")),
            MarkupParagraph(QCoreApplication.translate("Form", "Copyright © 2024, Sheng Fan. All rights reserved."))
        ]

        # Render each item in the content list
        for item in self.content:
            if isinstance(item, MarkupTitle):
                label = TitleLabel(item.txt)
                label.setAlignment(Qt.AlignCenter)
                self.verticalLayout_2.addWidget(label)

            elif isinstance(item, MarkupSubtitle):
                label = SubtitleLabel(item.txt)
                label.setAlignment(Qt.AlignCenter)
                self.verticalLayout_2.addWidget(label)

            elif isinstance(item, MarkupImage):
                wg = QWidget()
                layout = QHBoxLayout(wg)
                layout.setContentsMargins(0, 0, 0, 0)
                layout.setSpacing(0)

                label = BodyLabel()

                sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())

                pixmap = QPixmap(item.img_path)
                label.setPixmap(pixmap)
                label.setScaledContents(True)
                label.setAlignment(Qt.AlignCenter)
                label.setSizePolicy(sizePolicy)
                label.setMaximumSize(QSize(128, 128))
                label.setStyleSheet("")
                label.setWordWrap(True)

                layout.addWidget(label)
                self.verticalLayout_2.addWidget(wg)

            elif isinstance(item, MarkupParagraph):
                label = BodyLabel(item.txt)
                label.setAlignment(Qt.AlignCenter)
                label.setWordWrap(True)
                self.verticalLayout_2.addWidget(label)

            elif isinstance(item, MarkupButton):
                button = PushButton(item.text)
                button.clicked.connect(item.callback)
                self.verticalLayout_2.addWidget(button)

            elif isinstance(item, QObject):
                self.verticalLayout_2.addWidget(item)

    def open_github(self):
        # Open GitHub link
        print("Open GitHub link")  # Replace with actual logic to open GitHub

    def open_bilibili(self):
        # Open Bilibili link
        print("Open Bilibili link")  # Replace with actual logic to open Bilibili
