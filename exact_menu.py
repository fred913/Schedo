import datetime as dt
import shutil
import sys
from typing import Type, cast

from loguru import logger
from PySide2.QtCore import Qt, SignalInstance
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication
from qfluentwidgets import ComboBox
from qfluentwidgets import FluentIcon as fIcon
from qfluentwidgets import (FluentWindow, Flyout, FlyoutAnimationType, HyperlinkButton, InfoBarIcon, LineEdit, ListWidget, PrimaryPushButton, Theme,
                            ToolButton, setTheme)
from typing_extensions import TypeVar

import conf
import menu
import presets
from assets import get_img_dir
from globals import APP_NAME, CONFIG_DIR
from utils import WeekType, create_from_ui, get_week_type, read_schedule_config

current_week = dt.datetime.today().weekday()
temp_schedule = {'schedule': {}, 'schedule_even': {}}

T = TypeVar('T')


class ExactMenu(FluentWindow):

    def findChild(self, arg__1: Type[T], arg__2: str = ...) -> T:
        return super().findChild(arg__1, arg__2)  # type: ignore

    def __init__(self):
        super().__init__()
        self.menu = None
        self.interface = create_from_ui('exact_menu.ui', parent=self)
        self.initUI()
        self.init_interface()

        self.filename: 'str | None' = None

    def init_interface(self):
        select_temp_week = self.findChild(ComboBox, 'select_temp_week')  # 选择替换日期
        select_temp_week.addItems(presets.week)
        select_temp_week.setCurrentIndex(current_week)
        cast(SignalInstance, select_temp_week.currentIndexChanged).connect(self.refresh_schedule_list)  # 日期选择变化

        tmp_schedule_list = self.findChild(ListWidget, 'schedule_list')  # 换课列表
        tmp_schedule_list.addItems(self.load_schedule())
        tmp_schedule_list.itemChanged.connect(self.upload_item)

        class_kind_combo = self.findChild(ComboBox, 'class_combo')  # 课程类型
        class_kind_combo.addItems(presets.class_kind)

        set_button = self.findChild(ToolButton, 'set_button')
        set_button.setIcon(fIcon.EDIT)
        set_button.clicked.connect(self.edit_item)

        save_temp_conf = self.findChild(PrimaryPushButton, 'save_temp_conf')  # 保存设置
        save_temp_conf.clicked.connect(self.save_temp_conf)

        redirect_to_settings = self.findChild(HyperlinkButton, 'redirect_to_settings')
        redirect_to_settings.clicked.connect(self.open_settings)

    def open_settings(self):
        if self.menu is None or not self.menu.isVisible():  # 防多开
            self.menu = menu.desktop_widget()
            self.menu.show()
        else:
            self.menu.raise_()
            self.menu.activateWindow()

    def load_schedule(self):
        if not conf.CFG.temp.temp_schedule:
            filename = conf.CFG.general.schedule
            if filename is None:
                raise FileNotFoundError(f"Failed to find schedule file {repr(filename)}")
        else:
            filename = 'backup.json'

        assert filename is not None
        self.filename = filename

        # data = conf.load_from_json(filename)
        data = read_schedule_config(filename)

        if data is None:
            # file not found / format error
            raise RuntimeError(f"Failed to load schedule file: {filename}")

        elif not isinstance(data, dict):
            # file format error
            raise ValueError(f"Invalid schedule file format: {filename}; excepted a dict, got {type(data)}")

        if get_week_type() == WeekType.DOUBLE:
            return data['schedule_even'][str(current_week)]
        else:
            return data['schedule'][str(current_week)]

    def save_temp_conf(self):
        assert self.filename is not None
        filename = self.filename
        try:
            temp_week = self.findChild(ComboBox, 'select_temp_week')
            if temp_schedule != {'schedule': {}, 'schedule_even': {}}:
                if conf.CFG.temp.temp_schedule:
                    shutil.copy(CONFIG_DIR / 'schedule' / filename, CONFIG_DIR / 'schedule' / 'backup.json')
                    logger.info(f'Made backup of schedule config: {filename} -> backup.json')
                conf.CFG.temp.temp_schedule = filename
                conf.save()

            conf.CFG.temp.set_week = str(temp_week.currentIndex())
            conf.save()
            Flyout.create(icon=InfoBarIcon.SUCCESS,
                          title='保存成功',
                          content=f"已保存至 ./config.ini \n重启后失效。",
                          target=self.findChild(PrimaryPushButton, 'save_temp_conf'),
                          parent=self,
                          isClosable=True,
                          aniType=FlyoutAnimationType.PULL_UP)
        except Exception as e:
            Flyout.create(icon=InfoBarIcon.ERROR,
                          title='保存失败',
                          content=f"错误信息：{e}",
                          target=self.findChild(PrimaryPushButton, 'save_temp_conf'),
                          parent=self,
                          isClosable=True,
                          aniType=FlyoutAnimationType.PULL_UP)

    def refresh_schedule_list(self):
        current_week = self.findChild(ComboBox, 'select_temp_week').currentIndex()
        tmp_schedule_list = self.findChild(ListWidget, 'schedule_list')  # 换课列表
        tmp_schedule_list.clear()

        assert self.filename is not None
        filename = self.filename

        # data = conf.load_from_json(filename)
        data = read_schedule_config(filename)
        if data is None:
            # file not found / format error
            raise RuntimeError(f"Failed to load schedule list file: {filename}")

        elif not isinstance(data, dict):
            # file format error
            raise ValueError(f"Invalid schedule file format: {filename}; excepted a dict, got {type(data)}")

        if get_week_type() == WeekType.DOUBLE:
            tmp_schedule_list.addItems(data['schedule_even'][str(current_week)])
        else:
            tmp_schedule_list.addItems(data['schedule'][str(current_week)])

    def upload_item(self):
        global temp_schedule
        se_schedule_list = self.findChild(ListWidget, 'schedule_list')
        cache_list = []
        for i in range(se_schedule_list.count()):  # 缓存ListWidget数据至列表
            it = se_schedule_list.item(i)
            if it is None:
                logger.warning(f"ListWidget item {i} is None; shouldn't happen")
                continue

            item_text = it.text()
            cache_list.append(item_text)

        if get_week_type():
            temp_schedule['schedule_even'][str(current_week)] = cache_list
        else:
            temp_schedule['schedule'][str(current_week)] = cache_list

    def edit_item(self):
        tmp_schedule_list = self.findChild(ListWidget, 'schedule_list')
        class_combo = self.findChild(ComboBox, 'class_combo')
        custom_class = self.findChild(LineEdit, 'custom_class')
        selected_items = tmp_schedule_list.selectedItems()

        if selected_items:
            selected_item = selected_items[0]
            if class_combo.currentIndex() != 0:
                selected_item.setText(class_combo.currentText())
            else:
                if custom_class.text() != '':
                    selected_item.setText(custom_class.text())

    def initUI(self):
        primary_screen = QApplication.primaryScreen()
        if primary_screen is None:
            raise RuntimeError("Failed to get primary screen")
        screen_geometry = primary_screen.geometry()
        screen_width = screen_geometry.width()

        # self.setWindowFlags(Qt.FramelessWindowHint)  # incompatible with PySide2-FluentWidgets
        setTheme(Theme.AUTO)

        self.resize(1000, 700)
        self.setWindowTitle(f'{APP_NAME} - 更多功能')
        self.setWindowIcon(QIcon(str(get_img_dir() / 'favicon.png')))
        self.move(int(screen_width / 2 - 500), 150)

        self.addSubInterface(self.interface, fIcon.INFO, '更多设置')

        self.interface.setStyleSheet("""QLabel { font: "Microsoft YaHei UI"; }""")

    def closeEvent(self, e):
        e.ignore()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    if sys.platform == 'win32' and sys.getwindowsversion().build >= 22000:
        # 修改在win11高版本阴影异常
        app.setStyle("fusion")
    ex = ExactMenu()
    ex.show()
    sys.exit(app.exec())
