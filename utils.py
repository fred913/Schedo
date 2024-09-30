from PyQt6 import uic
from PyQt6.QtCore import QObject


def loadUi(ui_file: str, theme: str = "default", *, raw=False, base_instance: QObject | None = None):
    if not raw:
        ui = uic.load_ui.loadUi(f"ui/{theme}/{ui_file}", baseinstance=base_instance)
    else:
        ui = uic.load_ui.loadUi(ui_file, baseinstance=base_instance)
    assert ui is not None, f"Failed to load UI file: {ui_file}"
    return ui
