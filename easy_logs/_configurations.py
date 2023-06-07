# Predefined loggers:
from dataclasses import dataclass
from typing import Union


@dataclass
class _LoggingConfig:
    logger_name: str = "miskibin"
    lvl: Union[int, str] = 20
    file_name: str = None
    format: str = "%(message)s (%(filename)s:%(lineno)d)"
    datefmt: str = "%H:%M:%S"
    disable_existing_loggers: bool = False
    colored: bool = True


class Configs:
    simple_logger_config = _LoggingConfig(
        logger_name="simple_logger",
        format="%(message)s",
        disable_existing_loggers=True,
        lvl=10,
    )

    profesionall_logger_config = _LoggingConfig(
        logger_name="proffesional_logger",
        file_name="logs.log",
        format="%(asctime)20s | %(levelname)8s | %(filename)20s :%(lineno)4d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    default_logger_config = _LoggingConfig()


_LOGGERS = {name.split("_")[0]: config for name, config in Configs.__dict__.items()}
