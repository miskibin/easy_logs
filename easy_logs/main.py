import logging.config
from logging import Logger, getLogger
from pathlib import Path
from typing import Union, Literal
from easy_logs._logging_utils import ColoredFormatter, filter_log_record
from easy_logs._configurations import _LOGGERS


class FailedToLoadLoggingConfigException(Exception):
    pass


def get_logger(
    logger_name: str = "miskibin",
    lvl: Union[int, str] = 20,
    file_name: str = None,
    format: str = "%(message)s (%(filename)s:%(lineno)d)",
    datefmt: str = "%H:%M:%S",
    disable_existing_loggers: bool = False,
    colored: bool = True,
    predefined: Literal[
        "simple", "litteral", "profesionall"
    ] = None,  # for future versions [*(str(name) for name in _LOGGERS.keys())]
) -> Logger:
    """
    Get a logger with colored logs and filtering for IPython/Jupyter Notebook cells.
    Args:
         logger_name: The name of the logger.
         lvl: The logging level. Default is 20 (INFO).
         file_name: The file to which logs will be saved. If None, logs will not be saved to a file.
         format: The logging formatter.
         datefmt: The date format for the logging formatter. Specify only if `(asctime)` is in the format. Default is "%H:%M:%S".
         disable_existing_loggers: If True, disable existing loggers.
         predefined: Choose a predefined configuration. This will override all other arguments.
             Available configurations:
                 - "simple": A simple logger that works like `print()` but with colors.
                 - "professional": Saves logs to a file and displays time, filename, line number, and log level.
                 - "default": Default logger configuration.

     Returns:
         A logger with colored logs and filtering for IPython/Jupyter Notebook cells.

    """
    if predefined:
        try:
            config = _LOGGERS[predefined]
        except KeyError:
            raise FailedToLoadLoggingConfigException(
                f"Failed to load predefined configuration: {predefined}"
            )
        predefined = None
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
    if colored:
        logger.handlers[0].setFormatter(ColoredFormatter(format, datefmt))
    else:
        logger.handlers[0].setFormatter(logging.Formatter(format, datefmt))
    if file_name:
        if Path(file_name).suffix != ".log":
            file_name += ".log"
        logger.addHandler(logging.FileHandler(file_name))
        file_formatter = logging.Formatter(format, datefmt)
        logger.handlers[1].setFormatter(file_formatter)
    return logger
