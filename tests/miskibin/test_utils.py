import pytest
from miskibin.utils import get_logger


def test_get_logger():

    logger = get_logger()
    assert logger.name == "miskibin"
    assert logger.level == 20
    assert logger.handlers[0].formatter._fmt == "%(message)s"
    assert logger.handlers[0].formatter.datefmt == "%H:%M:%S"
    logger = get_logger(file_name="test")
    assert str(logger.handlers[1].baseFilename).endswith("test.log")


def test_get_logger_with_custom_format():
    logger = get_logger(format="%(asctime)s %(message)s")
    assert logger.handlers[0].formatter._fmt == "%(message)s"
    logger = get_logger(file_name="test", format="%(asctime)s %(message)s")
    assert logger.handlers[1].formatter._fmt == "%(asctime)s %(message)s"
