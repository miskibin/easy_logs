"""
This module provides a convenient way to create loggers with colored logs and filtering for IPython/Jupyter Notebook cells.

The main function `get_logger` can be used to obtain a logger with various configurations, including colored logs, saving logs to a file, and specifying log formatting. Additionally, it supports predefined configurations that simplify logger setup.

Example usage:
    logger = get_logger(logger_name="my_logger", lvl=20, file_name="logs.log", format="%(message)s (%(filename)s:%(lineno)d)")

Predefined Configurations:
    - `simple`: A simple logger that works like `print()` but with colors.
    - `professional`: A logger that saves logs to a file and displays additional information such as time, filename, line number, and log level.
    - `default`: Default logger configuration.

Note: To use the predefined configurations, specify the `predefined` argument with the desired configuration name.

For more information, refer to the docstring of the `get_logger` function.

Author: Michał Skibiński
Contact: mskibinski109@gmail.com
"""

from .main import get_logger, ColoredFormatter

__all__ = ["get_logger", "ColoredFormatter"]
