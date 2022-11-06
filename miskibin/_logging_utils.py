import logging


class ColoredFormatter(logging.Formatter):
    def __init__(self, fmt, datefmt):
        super().__init__()
        self.fmt = fmt
        purple = "\x1b[34;20m"
        green = "\x1b[32;20m"
        yellow = "\x1b[33;20m"
        red = "\x1b[31;20m"
        bold_red = "\x1b[31;1m"
        reset = "\x1b[0m"
        self.datefmt = datefmt
        self.FORMATS = {
            logging.DEBUG: purple + self.fmt + reset,
            logging.INFO: green + self.fmt + reset,
            logging.WARNING: yellow + self.fmt + reset,
            logging.ERROR: red + self.fmt + reset,
            logging.CRITICAL: bold_red + self.fmt + reset,
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, self.datefmt)
        return formatter.format(record)


def filter_log_record(record: logging.LogRecord):
    if record.filename.split(".")[0].isnumeric():
        record.filename = "ipynb cell"
    else:
        return True
    return record
