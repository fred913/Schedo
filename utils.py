import enum
import json
import os
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from loguru import logger
from PySide2.QtCore import QObject
from PySide2.QtWidgets import QWidget
from typing_extensions import TypeVar

import conf
import presets
import ui as ui_mod
import win32lib
from assets import get_img_dir
from conf import CFG

# def loadUi(ui_file: str, theme: str = "default", *, raw=False, base_instance: 'QObject | None' = None):
#     if not raw:
#         ui = uic.load_ui.loadUi(f"ui/{theme}/{ui_file}", baseinstance=base_instance)
#     else:
#         ui = uic.load_ui.loadUi(ui_file, baseinstance=base_instance)
#     assert ui is not None, f"Failed to load UI file: {ui_file}"
#     return ui

UI_MAPPING = {
    "exact_menu.ui": "Ui_ExactMenu",
    "menu-about.ui": "Ui_About",
    "menu-advance.ui": "Ui_Advance",
    "menu-configs.ui": "Ui_Configs",
    "menu-custom.ui": "Ui_Custom",
    "menu-preview.ui": "Ui_Preview",
    "menu-schedule_edit.ui": "Ui_ScheduleEdit",
    "menu-timeline_edit.ui": "Ui_TimelineEdit",
    "widget-countdown-custom.ui": "Ui_CountdownCustom",
    "widget-countdown.ui": "Ui_Countdown",
    "widget-current-activity.ui": "Ui_CurrentActivity",
    "widget-next-activity.ui": "Ui_NextActivity",
    "widget-time.ui": "Ui_Time",
    "widget-toast-bar.ui": "Ui_ToastBar",
    "widget-weather.ui": "Ui_Weather"
}


def load_ui(ui_file: str, theme: str = "default", *, raw=False, base_instance: 'QObject | None' = None):
    assert ui_mod is not None, f"UI package not compiled"
    assert ui_file in UI_MAPPING, f"UI file not found: {ui_file}"
    # ignore raw, theme, base_instance; import the python file from ui module, return <module>.Ui_Form(base_instance)
    ui_name = UI_MAPPING[ui_file]
    if ui_name.endswith('.py'):
        ui_name = ui_name[:-3]
    # mod = importlib(f"ui.{mod_name}", globals(), locals(), [f"ui.{theme}.{mod_name}.Ui_Form"], 0)
    # importlib
    ui = getattr(ui_mod, f"{ui_name}")
    return ui


def create_from_ui(ui_file: str, theme: str = "default", *, raw=False, parent: 'QObject | None' = None):
    assert ui_mod is not None, f"UI package not compiled"
    assert ui_file in UI_MAPPING, f"UI file not found: {ui_file}"
    # ignore raw, theme, base_instance; import the python file from ui module, return <module>.Ui_Form(base_instance)
    ui_name = UI_MAPPING[ui_file]
    if ui_name.endswith('.py'):
        ui_name = ui_name[:-3]
    # mod = importlib(f"ui.{mod_name}", globals(), locals(), [f"ui.{theme}.{mod_name}.Ui_Form"], 0)
    # importlib
    ui = getattr(ui_mod, f"{ui_name}")

    # try:
    #     ui = getattr(mod, f"Ui_Form")(base_instance)
    # except TypeError:
    #     ui = getattr(mod, f"Ui_Form")()
    # if hasattr(ui, "setupUi"):
    #     try:
    #         assert base_instance is not None
    #         ui.setupUi(base_instance)
    #     except (TypeError, AssertionError):
    #         ui.setupUi()
    class TargetWidgetWithUi(QWidget, ui):

        def __init__(self, parent=None):
            super().__init__(parent)
            self.setupUi(self)

    ui = TargetWidgetWithUi(parent)
    return ui


def read_schedule_config(filename: str) -> 'dict | None':
    """
    从 JSON 文件中加载数据。
    :param filename: 要加载的文件
    :return: 返回从文件中加载的数据字典
    """
    try:
        with open(f'config/schedule/{filename}', 'r', encoding='utf-8') as file:
            data = json.load(file)
            assert isinstance(data, dict), f"Invalid data type in schedule config file: {filename}, expected dict, got {type(data)}"
            return data
    except Exception as e:
        logger.exception(e)
        logger.error(f"Error reading schedule config file: {e}")
        return None


def update_schedule_config(new_data: 'dict[str, Any]', filename: str):
    # 初始化 data_dict 为一个空字典
    data_dict = {}

    # 如果文件存在，先读取文件中的现有数据
    if os.path.exists(f'config/schedule/{filename}'):
        try:
            with open(f'config/schedule/{filename}', 'r', encoding='utf-8') as file:
                data_dict = json.load(file)
        except Exception as e:
            logger.error(f"读取现有数据时出错: {e}")

    # 更新 data_dict，添加或覆盖新的数据
    data_dict.update(new_data)

    # 将更新后的数据保存回文件
    try:
        with open(f'config/schedule/{filename}', 'w', encoding='utf-8') as file:
            json.dump(data_dict, file, ensure_ascii=False, indent=4)
        return f"数据已成功保存到 config/schedule/{filename}"
    except Exception as e:
        logger.error(f"保存数据时出错: {e}")


@dataclass
class CountdownData:
    days: int
    hours: int
    minutes: int
    seconds: int

    @property
    def expired(self) -> bool:
        return self.days == 0 and self.hours == 0 and self.minutes == 0 and self.seconds == 0

    label: str


def calculate_countdown_from_config() -> 'CountdownData | None':
    custom_countdown = CFG.date.countdown_date
    # logger.debug(f"Custom countdown processing, {custom_countdown=}")
    if custom_countdown is None or custom_countdown.strip() == '':
        return None
    else:
        label = CFG.date.cd_text_custom
        custom_countdown = datetime.strptime(custom_countdown, '%Y-%m-%d')
        if custom_countdown < datetime.now():
            # return 0
            return CountdownData(0, 0, 0, 0, label)
        else:
            cd_text = custom_countdown - datetime.now()
            # return cd_text.days
            return CountdownData(cd_text.days, cd_text.seconds // 3600, cd_text.seconds // 60 % 60, cd_text.seconds % 60, label)


class WeekType(enum.IntEnum):
    SINGLE = 0
    DOUBLE = 1


def get_week_type():  # 获取单双周
    start_date = CFG.date.start_date
    if start_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        today = datetime.now()
        week_num = (today - start_date).days // 7 + 1
        if week_num % 2 == 0:
            return WeekType.DOUBLE  # 双周
        else:
            return WeekType.SINGLE  # 单周
    else:
        return WeekType.SINGLE  # 默认单周


def check_if_widget_included(widget: str):
    widgets_list = presets.get_widget_config()
    if widget in widgets_list:
        return True
    else:
        return False


def update_widget_config(new_data: 'dict[str, Any]'):
    # TODO reimplement this function

    data_dict = {}

    if os.path.exists(f'config/widget.json'):
        # if possible, inherit from current widget config file
        try:
            with open(f'config/widget.json', 'r', encoding='utf-8') as file:
                data_dict = json.load(file)
        except Exception as e:
            logger.exception(e)
            logger.error(f"Error reading widget config file: {e}")
            return e

    data_dict.update(new_data)

    try:
        with open(f'config/widget.json', 'w', encoding='utf-8') as file:
            json.dump(data_dict, file, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        logger.exception(e)
        logger.error(f"Error saving widget config file: {e}")
        return e


def get_time_offset():  # 获取时差偏移
    time_offset = CFG.general.time_offset
    if time_offset is None or time_offset == '' or time_offset == '0':
        return 0
    else:
        return int(time_offset)


def is_temp_week():
    if CFG.temp.set_week is None or CFG.temp.set_week == '':
        return False
    else:
        return CFG.temp.set_week


def is_temp_schedule():
    temp_schedule = CFG.temp.temp_schedule
    if temp_schedule is None or temp_schedule == '':
        return False
    else:
        return temp_schedule


T = TypeVar("T")


def assert_not_none(x: 'T | None') -> T:
    assert x is not None, "Unexpected None value"
    return x


def refresh_startup():
    if conf.CFG.general.auto_startup:
        win32lib.win32lib.remove_from_startup('Schedo.lnk')

    win32lib.win32lib.add_to_startup('Schedo.lnk', 'Schedo.exe', str(get_img_dir() / 'favicon.ico'))
