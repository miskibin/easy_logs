"""
This module provides a convenient way to create loggers with colored logs.

The main function get_logger can be used to obtain a logger with various configurations, 
including colored logs, saving logs to a file, and specifying log formatting. Additionally,
it supports predefined configurations that simplify logger setup.

Example usage:
logger = get_logger(predefined="professional")
logger.info("Everything is OK!")
>>> 2021-01-01 12:00:00,000 - INFO - demo.py:1 - Everything is OK!

For more information, refer to the docstring of the get_logger function.

Author: Michał Skibiński
Contact: mskibinski109@gmail.com
"""
from .main import get_logger, ColoredFormatter

__all__ = ["get_logger", "ColoredFormatter"]
