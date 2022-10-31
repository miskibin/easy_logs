![example workflow](https://github.com/michalskibinski109/miskibin/actions/workflows/python-app.yml/badge.svg)
[![PyPI version](https://badge.fury.io/py/miskibin.svg)](https://badge.fury.io/py/miskibin)

# miskibin

this repo contains some of my scripts and tools, that i
could not find anywhere else.

## installation:

```bash
pip install miskibin
```

## modules:

- [miskibin.utils:](#miskibinutils)
  - [get_logger()](#get_logger)
- [miskibin.ml](#miskibinml)
  - [LinearModel](#linearmodel)
- [miskibin.cn](#miskibincn)
  - [AnimatedGraph](#AnimatedGraph)

## [miskibin.utils](src/miskibin/utils):

module contains some useful functions, that i use in my projects.

### [get_logger()](src/miskibin/utils/utils.py):

returns highly configurable logger object.

- Every level has its own color. (If it is printed to terminal)
- Problems with logging messages from `ipynb` cells are resolved.
- Includes validation for file name and path.
- Has `disable_existing_loggers` param to disable all other loggers.

#### Example 1:

```python
logger = get_logger()
logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
logger.critical("critical")
```

#### output:

<img src="logging.png" width="500"/>

#### example 2:

```python
logger = get_logger(
    datefmt="%Y-%m-%d %H:%M:%S",
    format="%(asctime)s %(levelname)s %(funcName)s %(message)s",
    disable_existing_loggers=True,
    logger_name="test2",
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

<img src="advenced_logging.png" width="500"/>

## [miskibin.ml](src/miskibin/ml):

Machine learning module. Contains models, functions and classes for machine learning.

### LinearModel:

model with analytical solution for linear regression.
Implemnted from math formulas.

## [miskibin.cn](src/miskibin/cn):

module for working with complex networks.

### AnimatedGraph:

creates animated graph to visualize how some 'virus' spreads through network.
