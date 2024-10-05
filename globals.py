from pathlib import Path
from typing import Any, List, Union

from typing_extensions import TypeAlias

AUDIO_DEFAULT_DIR = Path.cwd() / "audio"

CONFIG_DIR = Path.cwd() / "config"
CONFIG_PATH_INI = Path("config.ini")
CONFIG_PATH_JSON = Path("config.json")

APP_NAME = 'Schedo'

SupportsJson: TypeAlias = 'Union[str, int, float, bool, None, dict[str, Any], List[Any]]'
