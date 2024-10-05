import datetime as dt
import signal
import sys
from pathlib import Path
from shutil import copy
from typing import Type
from xml.dom.minidom import Attr

import qfluentwidgets
from loguru import logger
from PySide2.QtCore import QByteArray, QDateTime, QEasingCurve, QPropertyAnimation, QRect, Qt, QTimer
from PySide2.QtGui import QFont, QFontDatabase, QIcon, QShowEvent
from PySide2.QtWidgets import (QApplication, QGraphicsBlurEffect, QGraphicsDropShadowEffect, QLabel, QMenu, QProgressBar, QPushButton, QSystemTrayIcon,
                               QVBoxLayout, QWidget)
from qfluentwidgets import Action, FluentTranslator, SystemTrayMenu, Theme, setTheme, setThemeColor
from typing_extensions import TypeVar

import conf
import exact_menu
import menu
import presets
import tip_toast
from assets import get_assets_dir, get_img_dir
from globals import APP_NAME, CONFIG_DIR
from utils import WeekType, calculate_countdown_from_config, create_from_ui, get_time_offset, get_week_type, is_temp_week, load_ui, read_schedule_config

today = dt.date.today()
filename = conf.CFG.general.schedule

# 存储窗口对象
windows = []

current_state = '课程表未加载'
current_time = dt.datetime.now().strftime('%H:%M:%S')
current_week = dt.datetime.now().weekday()
current_lessons = {}

timeline_data = {}
next_lessons = []

bkg_opacity = 165  # 模糊label的透明度(0~255)
time_offset = 0  # 时差偏移

logger.add("log/Schedo-{time}.log", rotation="10 MB", encoding="utf-8", retention="2 days")


# 获取课程上下午开始时间
def get_start_time():
    global morning_st, afternoon_st, timeline_data
    morning_st = None
    afternoon_st = None
    loaded_data = read_schedule_config(filename)
    if loaded_data is None:
        logger.error('加载课程表文件失败: 不符合 JSON 格式规范或文件不存在')
        return

    if not isinstance(loaded_data, dict):
        logger.error('课程表文件格式错误：JSON 根对象应当是一个字典')
        return

    timeline = loaded_data.get('timeline')

    if timeline is None:
        logger.error('课程表文件格式错误：缺少 timeline 字段')
        return

    for item_name, item_time in timeline.items():
        try:
            if item_name == 'start_time_m':
                if timeline[item_name]:
                    h, m = timeline[item_name]
                    morning_st = dt.datetime.combine(today, dt.time(h, m))
            elif item_name == 'start_time_a':
                if timeline[item_name]:
                    h, m = timeline[item_name]
                    afternoon_st = dt.datetime.combine(today, dt.time(h, m))
            else:
                timeline_data[item_name] = item_time
        except Exception as e:
            logger.error(f'加载课程表文件[起始时间]出错：{e}')


# 获取当前活动
def get_current_lessons():  # 获取今日课程
    global current_lessons
    loaded_data = read_schedule_config(filename)

    if loaded_data is None:
        logger.error('加载课程表文件失败: 不符合 JSON 格式规范或文件不存在')
        return

    if not isinstance(loaded_data, dict):
        logger.error('课程表文件格式错误：JSON 根对象应当是一个字典')
        return

    timeline = loaded_data.get('timeline')

    if timeline is None:
        logger.error('课程表文件格式错误：缺少 timeline 字段')
        return

    if not isinstance(timeline, dict):
        logger.error('课程表文件格式错误：timeline 字段应当是一个字典')
        return

    if conf.CFG.general.enable_alt_schedule:
        try:
            # if conf.get_week_type():
            if get_week_type() == WeekType.DOUBLE:
                schedule = loaded_data.get('schedule_even')
                if schedule is None:
                    logger.error('课程表文件格式错误：缺少 schedule_even 字段（双周）')
            else:
                schedule = loaded_data.get('schedule')
                if schedule is None:
                    logger.error('课程表文件格式错误：缺少 schedule 字段（单周）')
        except Exception as e:
            logger.error(f'加载课程表文件[单双周]出错：{e}')
            schedule = loaded_data.get('schedule')
            if schedule is None:
                logger.error('课程表文件格式错误：缺少 schedule 字段（单周）')
    else:
        # logger.debug('获取单周课程')
        schedule = loaded_data.get('schedule')
        if schedule is None:
            logger.error('课程表文件格式错误：缺少 schedule 字段（单周）')

    if schedule is None:
        raise RuntimeError('课程表文件格式错误：字段缺少或有误')

    class_count = 0
    for item_name, item_time in timeline.items():
        if item_name.startswith('am') or item_name.startswith('aa'):
            if schedule[str(current_week)]:
                try:
                    if schedule[str(current_week)][class_count] != '未添加':
                        current_lessons[item_name] = schedule[str(current_week)][class_count]
                    else:
                        current_lessons[item_name] = '暂无课程'
                except IndexError:
                    current_lessons[item_name] = '暂无课程'
                except Exception as e:
                    current_lessons[item_name] = '暂无课程'
                    logger.debug(f'加载课程表文件出错：{e}')
                class_count += 1
            else:
                current_lessons[item_name] = '暂无课程'
                class_count += 1


# 获取倒计时、弹窗提示
def get_countdown(toast=False):
    current_dt = dt.datetime.combine(today, dt.datetime.strptime(current_time, '%H:%M:%S').time())  # 当前时间
    return_text = []
    if afternoon_st is not None and current_dt > afternoon_st - dt.timedelta(minutes=30):
        c_time = afternoon_st + dt.timedelta(seconds=time_offset)  # 开始时间段
        if current_dt == c_time and toast:
            tip_toast.main(1)  # 上课
        if current_dt >= afternoon_st + dt.timedelta(seconds=time_offset):
            for item_name, item_time in timeline_data.items():
                if item_name.startswith('aa') or item_name.startswith('fa'):

                    add_time = int(item_time)
                    c_time += dt.timedelta(minutes=add_time)
                    # 判断时间是否上下课，发送通知
                    if current_dt == c_time and toast:
                        if item_name.startswith('fa'):
                            tip_toast.main(1)  # 上课
                        else:
                            tip_toast.main(0)  # 下课

                    if c_time >= current_dt:
                        # 根据所在时间段使用不同标语
                        if item_name.startswith('aa'):
                            return_text.append('当前活动结束还有')
                        else:
                            return_text.append('课间时长还有')
                        time_diff = c_time - current_dt
                        minute, sec = divmod(time_diff.seconds, 60)
                        return_text.append(f'{minute:02d}:{sec:02d}')
                        # 进度条
                        seconds = time_diff.seconds
                        return_text.append(int(100 - seconds / (int(item_time) * 60) * 100))
                        break
            if not return_text:
                return_text = ['今日课程已结束', f'00:00', 100]
        else:
            time_diff = c_time + dt.timedelta(seconds=time_offset) - current_dt
            minute, sec = divmod(time_diff.seconds, 60)
            return_text = ['距离上课还有', f'{minute:02d}:{sec:02d}', 100]
    # 上午
    elif morning_st is not None:
        c_time = morning_st + dt.timedelta(seconds=time_offset)  # 复制 morning_st 时间
        if current_dt == c_time + dt.timedelta(seconds=time_offset) and toast:
            tip_toast.main(1)  # 上课
        if current_dt >= morning_st + dt.timedelta(seconds=time_offset):
            for item_name, item_time in timeline_data.items():
                if item_name.startswith('am') or item_name.startswith('fm'):

                    add_time = int(item_time)
                    c_time += dt.timedelta(minutes=add_time)

                    # 判断时间是否上下课，发送通知
                    if current_dt == c_time and toast:
                        if item_name.startswith('fm'):
                            tip_toast.main(1)  # 上课
                        else:
                            tip_toast.main(0)  # 下课`
                    if c_time >= current_dt:
                        # 根据所在时间段使用不同标语
                        if item_name.startswith('am'):
                            return_text.append('当前活动结束还有')
                        else:
                            return_text.append('课间时长还有')
                        # 返回倒计时、进度条
                        time_diff = c_time - current_dt
                        minute, sec = divmod(time_diff.seconds, 60)
                        return_text.append(f'{minute:02d}:{sec:02d}')
                        # 进度条
                        seconds = time_diff.seconds
                        return_text.append(int(100 - seconds / (int(item_time) * 60) * 100))
                        break
            if not return_text:
                return_text = ['上午课程已结束', f'00:00', 100]
        else:
            time_diff = c_time + dt.timedelta(seconds=time_offset) - current_dt
            minute, sec = divmod(time_diff.seconds, 60)
            return_text = ['距离上课还有', f'{minute:02d}:{sec:02d}', 100]
    return return_text


# 获取将发生的活动
def get_next_lessons():
    global current_state
    global next_lessons
    next_lessons = []
    current_dt = dt.datetime.combine(today, dt.datetime.strptime(current_time, '%H:%M:%S').time())  # 当前时间

    if afternoon_st is not None and current_dt > afternoon_st - dt.timedelta(minutes=30):  # 提前30min获取下午课程
        c_time = afternoon_st  # 开始时间段
        for item_name, item_time in timeline_data.items():
            if item_name.startswith('aa') or item_name.startswith('fa'):
                if c_time > current_dt:
                    if item_name.startswith('aa'):
                        next_lessons.append(current_lessons[item_name])
                c_time += dt.timedelta(minutes=int(item_time))
    elif morning_st is not None:
        c_time = morning_st  # 开始时间段
        for item_name, item_time in timeline_data.items():
            if item_name.startswith('am') or item_name.startswith('fm'):
                if current_dt < c_time:
                    if item_name.startswith('am'):
                        next_lessons.append(current_lessons[item_name])
                c_time += dt.timedelta(minutes=int(item_time))


def get_next_lessons_text():
    if not next_lessons:
        cache_text = '当前暂无课程'
    else:
        cache_text = ''
        if len(next_lessons) >= 5:
            range_time = 5
        else:
            range_time = len(next_lessons)
        for i in range(range_time):
            if range_time > 2:
                if next_lessons[i] != '暂无课程':
                    cache_text += f'{presets.get_subject_abbreviation(next_lessons[i])}  '  # 获取课程简称
                else:
                    cache_text += f'无  '
            else:
                if next_lessons[i] != '暂无课程':
                    cache_text += f'{next_lessons[i]}  '
                else:
                    cache_text += f'暂无  '
    return cache_text


# 获取当前活动
def get_current_state():
    global current_state
    current_dt = dt.datetime.combine(today, dt.datetime.strptime(current_time, '%H:%M:%S').time())  # 当前时间
    is_changed = False
    # 下午
    if afternoon_st is not None and current_dt > afternoon_st - dt.timedelta(minutes=30):
        c_time = afternoon_st + dt.timedelta(seconds=time_offset)  # 开始时间段
        for item_name, item_time in timeline_data.items():
            if item_name.startswith('aa') or item_name.startswith('fa'):
                c_time += dt.timedelta(minutes=int(item_time))
                if c_time >= current_dt:
                    if item_name.startswith('aa'):
                        current_state = current_lessons[item_name]
                        is_changed = True
                    else:
                        current_state = '课间'
                        is_changed = True
                    break
    # 上午
    elif morning_st is not None and current_dt > morning_st:
        c_time = morning_st + dt.timedelta(seconds=time_offset)  # 复制 afternoon_st 时间
        for item_name, item_time in timeline_data.items():
            if item_name.startswith('am') or item_name.startswith('fm'):
                add_time = int(item_time)
                c_time += dt.timedelta(minutes=add_time)
                if c_time >= current_dt:
                    if item_name.startswith('am'):
                        current_state = current_lessons[item_name]
                        is_changed = True
                    else:
                        current_state = '课间'
                        is_changed = True
                    break
    if not is_changed:
        current_state = '暂无课程'


get_start_time()
get_current_lessons()
get_current_state()
get_next_lessons()

T = TypeVar("T")


class SystemTrayCard(QWidget):

    def __init__(self, parent: 'DesktopWidget'):
        super().__init__(parent=parent)

        self._parent = parent

        # Set widget size
        self.setFixedSize(300, 120)
        self.setContentsMargins(0, 0, 0, 0)

        # in widget:

        def get_font(size: int) -> QFont:
            font = QFont("Microsoft YaHei UI")
            font.setPixelSize(size)
            font.setWeight(QFont.Normal)
            return font

        self.countdown_data = QLabel(self)
        self.countdown_data.setGeometry(90, 29, 175, 47)
        self.countdown_data.setFont(get_font(33))
        self.countdown_data.setAlignment(Qt.AlignRight)
        self.countdown_data.setStyleSheet("color: #3d3d3d;")
        self.countdown_data.setText('00:00')

        self.countdown_label = QLabel(self)
        self.countdown_label.setGeometry(90, 10, 175, 33)
        self.countdown_label.setFont(get_font(14))
        self.countdown_label.setAlignment(Qt.AlignRight)
        self.countdown_label.setStyleSheet("color: #3d3d3d;")
        self.countdown_label.setText('距离上课还有')

        self.current_activity_progress = QProgressBar(self)
        self.current_activity_progress.setGeometry(5, 62, 120, 0)
        self.current_activity_progress.setStyleSheet("QProgressBar::chunk {background-color: #d8d8d8;border-radius: 5px;border: 1px solid #d8d8d8;}")
        self.current_activity_progress.setValue(30)

        self.current_activity_text = QLabel(self)
        self.current_activity_text.setGeometry(5, 6, 120, 60)
        self.current_activity_text.setFont(get_font(46))
        self.current_activity_text.setAlignment(Qt.AlignLeft)
        self.current_activity_text.setStyleSheet("color: #3d3d3d;")
        self.current_activity_text.setText('英语')

        self.software_name = QLabel(self)
        self.software_name.setGeometry(5, 84, 120, 34)
        self.software_name.setFont(get_font(20))
        self.software_name.setAlignment(Qt.AlignLeft)
        self.software_name.setStyleSheet("color: #bebebe;")
        self.software_name.setText(APP_NAME)

        self.current_time = QLabel(self)
        self.current_time.setGeometry(90, 83, 175, 22)
        self.current_time.setFont(get_font(20))
        self.current_time.setAlignment(Qt.AlignRight)
        self.current_time.setStyleSheet("color: #4d4d4d;")
        self.current_time.setText("00:00:00")

        self.setStyleSheet("QLabel { line-height: 1em; }")

        for wg in self.findChildren(QLabel):
            wg.setContentsMargins(0, 0, 0, 0)
            # move everything x by 15px
            # wg.setGeometry(wg.x() - 15, wg.y(), wg.width(), wg.height())

        self.update_data()

        self.tmr = QTimer(self)
        self.tmr.timeout.connect(self.update_data)
        self.tmr.start(1000)

    def destroy(self, destroyWindow: bool = ..., destroySubWindows: bool = ...) -> None:
        self.tmr.stop()
        return super().destroy(destroyWindow, destroySubWindows)

    def update_data(self):
        current_time = dt.datetime.now().strftime('%H:%M:%S')

        get_start_time()
        get_current_lessons()
        get_current_state()
        get_next_lessons()

        # 倒计时
        countdown_data = calculate_countdown_from_config()
        if countdown_data is not None:
            self.countdown_label.setText(f"距离 {countdown_data.label} 还有")
            self.countdown_data.setText(f"{countdown_data.days} 天")
        else:
            self.countdown_label.setText('未设置倒数日')
            self.countdown_data.setText('- 天')

        cd_data = get_countdown(toast=False)

        self.current_activity_progress.setValue(cd_data[2])

        # 当前活动
        self.current_activity_text.setText(current_state if current_state != '暂无课程' else '无课')

        # 软件名称
        self.software_name.setText(APP_NAME)

        # 当前时间
        self.current_time.setText(current_time)

        # 刷新
        self.repaint()


class DesktopWidget(QWidget):  # 主要小组件

    def __init__(self, path: str, pos: 'tuple[int, int]', enable_tray=False):
        super().__init__()
        init_config()

        # create_from_ui(path, theme, base_instance=self)
        self.ui = load_ui(path)()  # this gets the Ui_Xxxx class
        self.ui.setupUi(self)

        setTheme(Theme.LIGHT)
        setThemeColor('#36ABCF')
        self.menu = None
        self.exmenu = None

        # 设置窗口无边框和透明背景
        pin_on_top_cfg = conf.CFG.general.pin_on_top
        if pin_on_top_cfg is None or int(pin_on_top_cfg):  # 置顶
            self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool | Qt.WindowDoesNotAcceptFocus)
        else:
            self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

        # 添加阴影效果
        # shadow_effect = QGraphicsDropShadowEffect(self)
        # shadow_effect.setBlurRadius(22)
        # shadow_effect.setXOffset(0)
        # shadow_effect.setYOffset(7)
        # shadow_effect.setColor(QColor(0, 0, 0, 60))
        # self.setGraphicsEffect(shadow_effect)

        if enable_tray:  # 托盘图标
            self.tray_icon = QSystemTrayIcon(QIcon(str(get_img_dir() / "favicon.png")), self)
            self.tray_icon.setToolTip(APP_NAME)

            self.tray_menu = SystemTrayMenu()

            def increase_opacity():
                conf.CFG.general.transparent = 240
                conf.save()

            def decrease_opacity():
                conf.CFG.general.transparent = 185
                conf.save()

            self.tray_card = SystemTrayCard(self)
            self.tray_menu.addWidget(self.tray_card, selectable=False)

            self.tray_menu.addAction(Action('提高不透明度', self, triggered=increase_opacity))
            self.tray_menu.addAction(Action('降低不透明度', self, triggered=decrease_opacity))

            self.tray_menu.addAction(Action('设置', self, triggered=self.open_settings))
            self.tray_menu.addAction(Action('退出', self, triggered=_interrupt_handler))

            self.tray_icon.setContextMenu(self.tray_menu)

            # 显示托盘图标
            self.tray_icon.show()

        if path == 'widget-time.ui':  # 日期显示
            self.date_text = self.findChild(QLabel, 'date_text')
            self.date_text.setText(f'{today.year} 年 {today.month} 月')
            self.day_text = self.findChild(QLabel, 'day_text')
            self.day_text.setText(f'{today.day}日  {presets.week[today.weekday()]}')

        elif path == 'widget-countdown.ui':  # 活动倒计时
            self.countdown_progress_bar = self.findChild(QProgressBar, 'progressBar')
            self.activity_countdown = self.findChild(QLabel, 'activity_countdown')
            self.ac_title = self.findChild(QLabel, 'activity_countdown_title')

        elif path == 'widget-current-activity.ui':  # 当前活动
            self.current_state_text = self.findChild(QPushButton, 'subject')
            self.blur_effect_label = self.findChild(QLabel, 'blurEffect')
            # 模糊效果
            self.blur_effect = QGraphicsBlurEffect()
            button = self.findChild(QPushButton, 'subject')
            button.clicked.connect(self.open_exact_menu)

        elif path == 'widget-next-activity.ui':  # 接下来的活动
            self.nl_text = self.findChild(QLabel, 'next_lesson_text')

        elif path == 'widget-countdown-custom.ui':  # 自定义倒计时
            self.custom_title = self.findChild(QLabel, 'countdown_custom_title')
            self.custom_countdown = self.findChild(QLabel, 'custom_countdown')

        # 设置窗口位置
        self.anim_window_creation(pos)

        self.update_data(1)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(lambda: self.update_data(path=path))
        self.timer.start()

    def showEvent(self, event: QShowEvent) -> None:
        return super().showEvent(event)

    def findChild(self, arg__1: Type[T], arg__2: str = ...) -> T:
        return super().findChild(arg__1, arg__2)  # type: ignore

    def open_settings(self):
        if self.menu is None or not self.menu.isVisible():  # 防多开
            self.menu = menu.desktop_widget()
            self.menu.show()
        else:
            self.menu.raise_()
            self.menu.activateWindow()

    def open_exact_menu(self):
        if not conf.CFG.temp.hide:
            if self.exmenu is None or not self.exmenu.isVisible():  # 防多开
                self.exmenu = exact_menu.ExactMenu()
                self.exmenu.show()
            else:
                self.exmenu.raise_()
                self.exmenu.activateWindow()
        else:
            conf.CFG.temp.hide = False
            conf.save()
            broadcast_hide_show_state_change()

    def anim_window_creation(self, target_pos):  # 窗口动画！
        # 创建位置动画
        self.animation = QPropertyAnimation(self, QByteArray(b"geometry"))
        self.animation.setDuration(555)  # 持续时间
        self.animation.setStartValue(QRect(target_pos[0], -self.height(), self.width(), self.height()))
        self.animation.setEndValue(QRect(target_pos[0], target_pos[1], self.width(), self.height()))
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)  # 设置动画效果
        self.animation.start()

    def anim_window_hide(self):  # 隐藏窗口
        self.animation = QPropertyAnimation(self, QByteArray(b"geometry"))
        self.animation.setDuration(555)  # 持续时间
        self.animation.setStartValue(QRect(self.x(), self.y(), self.width(), self.height()))
        self.animation.setEndValue(QRect(self.x(), 40 - self.height(), self.width(), self.height()))
        self.animation.setEasingCurve(QEasingCurve.OutExpo)  # 设置动画效果
        self.animation.start()

    def anim_window_show(self):  # 显示窗口
        self.animation = QPropertyAnimation(self, QByteArray(b"geometry"))
        self.animation.setDuration(555)  # 持续时间
        self.animation.setStartValue(QRect(self.x(), self.y(), self.width(), self.height()))
        margin_cfg = conf.CFG.general.margin
        self.animation.setEndValue(QRect(self.x(), int(margin_cfg or "10"), self.width(), self.height()))
        self.animation.setEasingCurve(QEasingCurve.OutExpo)  # 设置动画效果
        self.animation.start()

    def update_data(self, first_setup=0, path=''):
        global current_time, current_week, filename, start_y, time_offset

        current_time = dt.datetime.now().strftime('%H:%M:%S')

        filename = conf.CFG.general.schedule
        time_offset = get_time_offset()

        get_start_time()
        get_current_lessons()
        get_current_state()
        get_next_lessons()

        if not first_setup:  # 如果不是初次启动
            self.update_hide_show_state()

        if is_temp_week():  # 调休日
            current_week = conf.CFG.temp.set_week
        else:
            current_week = dt.datetime.now().weekday()

        filename = conf.CFG.general.schedule

        transparent_cfg = conf.CFG.general.transparent
        bkg = self.findChild(QLabel, 'label')
        bkg.setStyleSheet(f'background-color: rgba(242, 243, 245, {int(transparent_cfg or "240")}); border-radius: 8px')  # 背景透明度

        if path != 'widget-current-activity.ui':  # 不是当前活动组件
            cd_list = get_countdown()
        else:
            cd_list = get_countdown(toast=True)

        # infer widget type from ui attributes
        if hasattr(self, 'day_text'):
            self.date_text.setText(f'{today.year} 年 {today.month} 月')
            self.day_text.setText(f'{today.day} 日 {presets.week[today.weekday()]}')

        if hasattr(self, 'current_state_text'):
            # 实时活动
            self.current_state_text.setText(f'  {current_state}')
            self.current_state_text.setIcon(QIcon(presets.get_subject_icon(current_state)))
            self.blur_effect.setBlurRadius(35)  # 模糊半径
            self.blur_effect_label.setStyleSheet(f'background-color: rgba{presets.subject_color(current_state)}, {bkg_opacity});')
            self.blur_effect_label.setGraphicsEffect(self.blur_effect)

        if hasattr(self, 'next_lesson_text'):
            self.nl_text.setText(get_next_lessons_text())

        if hasattr(self, 'activity_countdown'):
            if cd_list:
                self.activity_countdown.setText(cd_list[1])
                self.ac_title.setText(cd_list[0])
                self.countdown_progress_bar.setValue(cd_list[2])

        if hasattr(self, 'countdown_custom_title'):
            cd_data = calculate_countdown_from_config()
            if cd_data:
                self.custom_title.setText(f'距离 {cd_data.label} 还有')
                self.custom_countdown.setText(f"{cd_data.days} 天")
            else:
                self.custom_title.setText('未设置倒数日')
                self.custom_countdown.setText('-')

    def update_hide_show_state(self):
        if conf.CFG.general.auto_hide:
            if current_state == '课间' or current_state == '暂无课程':
                self.anim_window_show()
            else:
                self.anim_window_hide()
        else:
            if conf.CFG.temp.hide:
                self.anim_window_hide()
            else:
                self.anim_window_show()

    # 点击自动隐藏
    def mousePressEvent(self, event):
        conf.CFG.temp.hide = not conf.CFG.temp.hide
        conf.save()
        broadcast_hide_show_state_change()


def broadcast_hide_show_state_change():
    for win in windows:
        win.update_hide_show_state()


def init_config():  # 重设配置文件
    conf.CFG.temp.set_week = ''
    conf.CFG.temp.hide = False
    conf.save()

    if conf.CFG.temp.temp_schedule:  # 修复换课重置
        # copy('config/schedule/backup.json', f'config/schedule/{filename}')
        copy(CONFIG_DIR / 'schedule' / 'backup.json', CONFIG_DIR / 'schedule' / f'{filename}')
        conf.CFG.temp.temp_schedule = ''
        conf.save()


def _interrupt_handler(*_, **__):
    logger.warning('Shutting down.')
    for application in windows:
        application.close()
    app.quit()


def load_font_get_family(font_file: 'str | Path'):
    fontDb = QFontDatabase()
    fontID = fontDb.addApplicationFont(str(font_file))
    fontFamilies = fontDb.applicationFontFamilies(fontID)
    assert len(fontFamilies) == 1
    return fontFamilies[0]


if __name__ == '__main__':
    # QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    # QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    # QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    translator = FluentTranslator()

    app = QApplication(sys.argv)

    # ff = load_font_get_family(get_assets_dir() / "MiSansVF.ttf")

    # def getFont(fontSize=14, weight=QFont.Normal):
    #     font = QFont()
    #     font.setFamilies([ff])
    #     font.setPixelSize(fontSize)
    #     font.setWeight(weight)
    #     return font

    # qfluentwidgets.common.font.getFont = getFont

    # app.setFont(QFont(ff))

    # app.setFont(QFont('Microsoft YaHei UI'))

    app.installTranslator(translator)

    # app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)

    if sys.platform == 'win32' and sys.getwindowsversion().build >= 22000:  # 修改在win11高版本阴影异常
        app.setStyle("Fusion")

    theme = 'default'

    # 获取屏幕横向分辨率
    primary_screen = app.primaryScreen()
    if primary_screen is None:
        raise RuntimeError('No primary screen available.')

    screen_geometry = primary_screen.availableGeometry()
    screen_width = screen_geometry.width()

    widgets = presets.get_widget_config()

    # 所有组件窗口的宽度
    spacing = -5
    total_width = sum((presets.widget_width[key] for key in widgets), spacing * (len(widgets) - 1))

    start_x = int((screen_width - total_width) / 2)
    margin_cfg = conf.CFG.general.margin
    start_y = int(margin_cfg or "10")

    def cal_start_width(num):
        width = 0
        for i in range(num):
            width += presets.widget_width[widgets[i]]
        return int(start_x + spacing * num + width)

    # TODO add an action in menu to add shortcut to startmenu/desktop, instead of creating shortcut automatically without user's consent
    # if conf.CFG.other.initialstartup == '1':  # 首次启动
    #     try:
    #         add_shortcut('ClassWidgets.exe', 'img/favicon.ico')

    #         try:
    #             add_shortcut_to_startmenu('ClassWidgets.exe', 'img/favicon.ico')
    #         except UnsupportedOperationPlatformError:
    #             # not win32 platform, unsupported
    #             logger.warning('Non-win32 platform detected, will not add shortcut to startmenu.')

    #         conf.CFG.other.initialstartup = ''
    #         conf.save()  # this is really bullshit design; wait for further restructuring
    #     except Exception as e:
    #         logger.error(f'添加快捷方式失败：{e}')

    for w in range(len(widgets)):
        # if w == 0:
        #     show_window(widgets[w], (cal_start_width(w), start_y), True)
        # else:
        #     show_window(widgets[w], (cal_start_width(w), start_y))
        wg = DesktopWidget(widgets[w], (cal_start_width(w), start_y), enable_tray=w == 0)
        windows.append(wg)  # 将窗口对象添加到列表

    for application in windows:  # 显示所有窗口
        logger.info(f'显示窗口：{application.windowTitle()}')
        application.show()
        app.processEvents()

    signal.signal(signal.SIGINT, _interrupt_handler)
    signal.signal(signal.SIGTERM, _interrupt_handler)

    try:
        sys.exit(app.exec())
    except AttributeError:
        try:
            sys.exit(app.exec_())
        except Exception as e:
            raise e from None
    finally:
        exit()
