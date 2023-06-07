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


_simple_logger_config = _LoggingConfig(
    logger_name="simple_logger",
    format="%(message)s",
    disable_existing_loggers=True,
    lvl=10,
)


_proffesional_logger_config = _LoggingConfig(
    logger_name="proffesional_logger",
    file_name="logs.log",
    format="%(asctime)20s | %(levelname)8s | %(filename)20s :%(lineno)4d | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
_default_logger_config = _LoggingConfig()

_LOGGERS = {
    "simple": _simple_logger_config,
    "proffesional": _proffesional_logger_config,
    "default": _default_logger_config,
}
