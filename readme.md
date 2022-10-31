![example workflow](https://github.com/michalskibinski109/chess_analyse_app/actions/workflows/python-app.yml/badge.svg)
[![PyPI version](https://badge.fury.io/py/miskibin.svg)](https://badge.fury.io/py/miskibin)
# miskibin 
this repo contains some of my scripts and tools, that i 
could not find anywhere else.

## [miskibin.utils](src/miskibin/utils.py)
`get_logger()`:
returns highly configurable logger object.
- Every level has its own color. (If it is printed to terminal)
- Problems with logging messages from `ipynb` cells are resolved.
- Includes validation for file name and path.
- Has `disable_existing_loggers` param to disable all other loggers.

### Example:
```python
logger = get_logger()
logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
logger.critical("critical")
```
### output:
![](logging.png)
# example:
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
## output:
![](advenced_logging.png)
## to install:
```bash
pip install miskibin 
```
