import sys
from pathlib import Path

assets_dir_entries = [
    Path("assets"),
    Path(__file__).parent / "assets",
    Path(__file__).parent.parent / "assets",
    Path(__file__).parent.parent.parent / "assets",
]

if hasattr(sys, '_MEIPASS'):
    assets_dir_entries.append(Path(getattr(sys, '_MEIPASS')) / "assets")


def get_assets_dir() -> Path:
    for entry in assets_dir_entries:
        flagfile = entry / "_assets_dir_flag"
        if flagfile.exists():
            return entry
    raise FileNotFoundError("Could not find assets directory")


def get_img_dir() -> Path:
    return get_assets_dir() / "img"
