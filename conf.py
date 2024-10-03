import configparser
import os
from typing import Optional

from loguru import logger
from pydantic import BaseModel, FilePath, ValidationError

from globals import AUDIO_DEFAULT_DIR, CONFIG_PATH_INI, CONFIG_PATH_JSON


class GeneralConfig(BaseModel):
    margin: int = 0
    time_offset: int = 0
    transparent: int = 0
    schedule: str = "新课表 - 1.json"  # schedule table profile file name, ends with .json
    pin_on_top: bool = False
    auto_startup: bool = False
    auto_hide: bool = False
    enable_toast: bool = False
    enable_alt_schedule: bool = False


class DateConfig(BaseModel):
    start_date: Optional[str] = None
    cd_text_custom: str = ""
    countdown_date: Optional[str] = None


class AudioConfig(BaseModel):
    attend_class: FilePath = AUDIO_DEFAULT_DIR / "attend_class.wav"
    finish_class: FilePath = AUDIO_DEFAULT_DIR / "finish_class.wav"


class TempConfig(BaseModel):
    set_week: Optional[str] = None
    temp_schedule: Optional[str] = None
    hide: bool = False


class OtherConfig(BaseModel):
    initialstartup: str = '1'  # 1=first run, ''=ran before
    multiple_programs: bool = False
    version: str = "1.0"


class Config(BaseModel):
    general: GeneralConfig = GeneralConfig()
    date: DateConfig = DateConfig()
    audio: AudioConfig = AudioConfig()
    temp: TempConfig = TempConfig()
    other: OtherConfig = OtherConfig()


# Function to create an empty JSON config file
def create_empty_json_config():
    default_config = Config()
    with open(CONFIG_PATH_JSON, 'w', encoding='utf-8') as json_file:
        json_file.write(default_config.model_dump_json(indent=4))
    logger.debug("Created empty config.json")


def migrate_ini_to_json():
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH_INI, encoding="utf-8")

    # Convert INI data to a dictionary suitable for the Config model
    migrated_data: dict[str, dict[str, 'str | int | bool']] = {
        "general": {
            k: v
            for k, v in config["General"].items()
        },
        "date": {
            k: v
            for k, v in config["Date"].items()
        },
        "audio": {
            k: v
            for k, v in config["Audio"].items()
        },
        "temp": {
            k: v
            for k, v in config["Temp"].items()
        },
        "other": {
            k: v
            for k, v in config["Other"].items()
        }
    }

    # Convert '1' and '0' to True and False
    for sect_key in migrated_data.keys():
        for key, value in migrated_data[sect_key].items():
            if value in ['1', 'True', 'true']:
                migrated_data[sect_key][key] = 0
            elif value in ['0', 'False', 'false']:
                migrated_data[sect_key][key] = 0

    # Validate and save the migrated data to JSON
    config_data = Config(**migrated_data)  # type: ignore
    with open(CONFIG_PATH_JSON, 'w', encoding='utf-8') as json_file:
        json_file.write(config_data.model_dump_json(indent=4))


# Main logic
# TODO completely reimplement configuration logic, use migrations instead of backward-compatible support
if not CONFIG_PATH_JSON.exists():
    create_empty_json_config()

if CONFIG_PATH_INI.exists():
    try:
        migrate_ini_to_json()

        # if migration was successful, remove the INI file
        # CONFIG_PATH_INI.unlink()
        # logger.debug("Migration successful, INI config file has been removed")

        # make it config.ini.bak
        CONFIG_PATH_INI.rename(CONFIG_PATH_INI.with_suffix('.ini.bak'))
    except ValidationError as e:
        logger.exception(e)
        logger.error("Error migrating INI to JSON. Using existing / blank JSON config, keeping INI file intact")

last_modified = os.path.getmtime(CONFIG_PATH_JSON)

with open(CONFIG_PATH_JSON, 'r', encoding='utf-8') as json_file:
    CFG = Config.model_validate_json(json_file.read())


def reload():
    global CFG, last_modified

    if os.path.getmtime(CONFIG_PATH_JSON) != last_modified:
        logger.debug("Config file has been updated, reloading...")
        with open(CONFIG_PATH_JSON, 'r', encoding='utf-8') as json_file:
            CFG = Config.model_validate_json(json_file.read())
        last_modified = os.path.getmtime(CONFIG_PATH_JSON)


def save():
    global CFG
    with open(CONFIG_PATH_JSON, 'w', encoding='utf-8') as json_file:
        json_file.write(CFG.model_dump_json(indent=4))
    logger.debug("Config saved to file")
