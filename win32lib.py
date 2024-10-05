import os
import sys

from loguru import logger

from exceptions import UnsupportedOperationPlatformError
from globals import APP_NAME


class _W32LIB:

    @classmethod
    def raise_for_platform(cls):
        if not cls.is_supported_platform():
            raise UnsupportedOperationPlatformError("This operation is not supported on this platform.")

    @classmethod
    def is_supported_platform(cls):
        # Check if Windows platform
        return sys.platform.startswith('win')

    @classmethod
    def add_shortcut_to_startmenu(cls, file='', icon=''):
        cls.raise_for_platform()

        from win32com.client import Dispatch
        from win32com.client.dynamic import CDispatch

        try:
            if file == "":
                file_path = os.path.realpath(__file__)
            else:
                file_path = os.path.abspath(file)

            if icon == "":
                icon_path = file_path
            else:
                icon_path = os.path.abspath(icon)

            # Get Start Menu folder path
            appdata = os.getenv('APPDATA')
            if appdata is None:
                raise UnsupportedOperationPlatformError("APPDATA environment variable not found.")

            menu_folder = os.path.join(appdata, 'Microsoft', 'Windows', 'Start Menu', 'Programs')

            # Check if the menu folder exists
            if not os.path.exists(menu_folder):
                raise FileNotFoundError(f"The Start Menu Programs folder does not exist: {menu_folder}")

            name = os.path.splitext(os.path.basename(file_path))[0]  # Use file name as shortcut name
            shortcut_path = os.path.join(menu_folder, f'{name}.lnk')

            # Create shortcut
            shell: CDispatch = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(shortcut_path)
            shortcut.Targetpath = file_path
            shortcut.WorkingDirectory = os.path.dirname(file_path)
            shortcut.IconLocation = icon_path
            shortcut.save()
        except Exception as e:
            logger.error(f"Error creating Start Menu shortcut: {e}")

    @classmethod
    def add_shortcut(cls, file='', icon=''):
        cls.raise_for_platform()

        from win32com.client import Dispatch
        from win32com.client.dynamic import CDispatch

        try:
            if file == "":
                file_path = os.path.realpath(__file__)
            else:
                file_path = os.path.abspath(file)

            if icon == "":
                icon_path = file_path
            else:
                icon_path = os.path.abspath(icon)

            # Get Desktop folder path
            userprofile = os.getenv('USERPROFILE')
            if userprofile is None:
                raise UnsupportedOperationPlatformError("USERPROFILE environment variable not found.")

            desktop_folder = os.path.join(userprofile, 'Desktop')

            name = os.path.splitext(os.path.basename(file_path))[0]  # Use file name as shortcut name
            shortcut_path = os.path.join(desktop_folder, f'{name}.lnk')

            # Create shortcut
            shell: CDispatch = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(shortcut_path)
            shortcut.Targetpath = file_path
            shortcut.WorkingDirectory = os.path.dirname(file_path)
            shortcut.IconLocation = icon_path
            shortcut.save()
        except Exception as e:
            logger.error(f"Error creating Desktop shortcut: {e}")

    @classmethod
    def add_to_startup(cls, lnk_name: str, file_path: str, icon_path: str):
        cls.raise_for_platform()

        from win32com.client import Dispatch
        from win32com.client.dynamic import CDispatch

        if file_path == "":
            file_path = os.path.realpath(__file__)
        else:
            file_path = os.path.abspath(file_path)

        if icon_path == "":
            icon_path = file_path
        else:
            icon_path = os.path.abspath(icon_path)

        # Get Startup folder path
        appdata = os.getenv('APPDATA')
        if appdata is None:
            raise UnsupportedOperationPlatformError("APPDATA environment variable not found.")

        startup_folder = os.path.join(appdata, 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

        shortcut_path = os.path.join(startup_folder, lnk_name)

        # Create shortcut
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.Targetpath = file_path
        shortcut.WorkingDirectory = os.path.dirname(file_path)
        shortcut.IconLocation = icon_path
        shortcut.save()

    @classmethod
    def remove_from_startup(cls, lnk_name: str):
        cls.raise_for_platform()

        appdata = os.getenv('APPDATA')
        if appdata is None:
            raise UnsupportedOperationPlatformError("APPDATA environment variable not found.")

        startup_folder = os.path.join(appdata, 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        shortcut_path = os.path.join(startup_folder, lnk_name)

        if os.path.exists(shortcut_path):
            os.remove(shortcut_path)

            return True
        else:
            return False


win32lib = _W32LIB()
