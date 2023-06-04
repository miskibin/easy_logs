from __future__ import annotations
import logging.config
from logging import Logger, getLogger
from pathlib import Path
from typing import Union, Literal
from miskibin._logging_utils import ColoredFormatter, filter_log_record
from typing import Annotated
from dataclasses import dataclass


def get_logger(
    logger_name: str = "miskibin",
    lvl: Union[int, str] = 20,
    file_name: str = None,
    format: str = "%(message)s (%(filename)s:%(lineno)d)",
    datefmt: str = "%H:%M:%S",
    disable_existing_loggers: bool = False,
    predefined_configuration: Literal["simple", "proffesional", "default"] = None,
) -> Logger:
    """
    Get logger with colored logs and filter for ipynb cells.
    Args:
        logger_name:  name of the logger
        lvl: logging level. Default is 20 (info).
        file_name: file that logs will be saved to. If None, logs will not be saved to file.
        formatter: logging formatter.
        datefmt: date format for logging formatter. Define only if `(asctime)`
        in format Default is "%H:%M:%S".
        disable_existing_loggers: if True, disable existing loggers.
        predefined_configuration: Choose predefined configuration. Will override all other arguments.
        Available configurations:
            simple: simple logger that works like print() but with colors
            proffesional: saves logs to file, displays time, filename line number and lvl
            default: default logger configuration
    Returns:
        Logger with colored logs and filter for ipynb cells.
    """
    if predefined_configuration:
        try:
            config = _LOGGERS[predefined_configuration]
        except KeyError:
            raise FailedToLoadLoggingConfigException(
                f"Failed to load predefined configuration: {predefined_configuration}"
            )
        predefined_configuration = None
        return get_logger(**config.__dict__)
    if disable_existing_loggers:
        logging.config.dictConfig(
            {
                "version": 1,
                "disable_existing_loggers": True,
            }
        )

    logger = getLogger(logger_name)
    if logger.handlers:
        logger.handlers.clear()
    logger.addFilter(filter_log_record)
    logger.setLevel(lvl)
    logger.addHandler(logging.StreamHandler())
    logger.handlers[0].setFormatter(ColoredFormatter(format, datefmt))
    if file_name:
        if Path(file_name).suffix != ".log":
            file_name += ".log"
        logger.addHandler(logging.FileHandler(file_name))
        file_formatter = logging.Formatter(format, datefmt)
        logger.handlers[1].setFormatter(file_formatter)
    return logger


# Predefined loggers:
@dataclass
class _LoggingConfig:
    logger_name: str = "miskibin"
    lvl: Union[int, str] = 20
    file_name: str = None
    format: str = "%(message)s (%(filename)s:%(lineno)d)"
    datefmt: str = "%H:%M:%S"
    disable_existing_loggers: bool = False


class FailedToLoadLoggingConfigException(Exception):
    pass


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
