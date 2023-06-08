![example workflow](https://github.com/michalskibinski109/easy_logs/actions/workflows/python-app.yml/badge.svg)
[![PyPI version](https://badge.fury.io/py/easy_logs.svg)](https://badge.fury.io/py/miskibin)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
# easy_logs

Did you ever regret that logging in python is so complicated?
Have you ever wanted to have a logger that is easy to use and has colored logs? If so, this module is for you.
## installation:

```bash
pip install easy_logs
```

### Usage

`get_logger` returns highly configurable logger object.

- Every level has its own color. (If it is printed to terminal)
- Problems with logging messages from `ipynb` cells are resolved.
- Includes validation for file name and path.
- Has `disable_existing_loggers` param to disable all other loggers.
#### params:
- `logger_name` - name of the logger
- `lvl`: [logging level](https://docs.python.org/3/library/logging.html#logging-levels). Default is 10 (DEBUG).
- `file_name`: file that logs will be saved to. If None, logs will not be saved to file.
- `format`: [logging format](https://docs.python.org/3/library/logging.html#logrecord-attributes).
- `datefmt`: date format for logging formatter. Define only if `(asctime)` in format Default is "%H:%M:%S".
- `disable_existing_loggers`: if True, disable existing loggers.
- `predefined`: Choose predefined configuration. Will override all other arguments

#### predefined_configuration:
- `default`: default configuration
- `simple`: simple logger that works like print() but with colors
- `profesionall`: saves logs to file, displays time, filename line number and lvl


#### Example 1:

```python
from easy_logs.utils import get_logger
logger = get_logger(lvl = 10)
logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
logger.critical("critical")
```

#### output:
<img src="https://user-images.githubusercontent.com/77834536/201940080-28e7dc08-ac99-4f8d-8f24-a9e0c6ac06c2.png" width="500"/>

#### example 2:

```python
from easy_logs.utils import get_logger
logger = get_logger(
    datefmt="%Y-%m-%d %H:%M:%S",
    format="%(asctime)s %(levelname)s %(funcName)s %(message)s",
    disable_existing_loggers=True,
    logger_name="test2",
    file_name = None,
    lvl="INFO",
)


def example_func():
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")
example_func()
```

#### output:

<img src="https://user-images.githubusercontent.com/77834536/201939466-228b110f-21de-4461-9c86-55f8f46652ef.png" width="500"/>


#### example 3:

```python
from easy_logs import get_logger

logger = get_logger(predefined="profesionall")
logger.info("Everything is OK!")
logger.warning("I'm worried about something...")
logger.error("Something went wrong...")
logger.critical("Let's panic!")

```

#### output:
<img src="https://github.com/michalskibinski109/easy_logs/assets/77834536/20d9602b-86f4-4ffb-b8d1-48686eb8d3d0" width="800"/>
