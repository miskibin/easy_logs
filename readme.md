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
from miskibin.utils import get_logger

logger = get_logger()

logger.debug("debug")
logger = get_logger(
    format="%(asctime)s - %(funcName)s - %(levelname)s - %(message)s",
    disable_existing_loggers=True,
    logger_name="test",
)
logger.warning("warning")
logger.error("error")
logger = get_logger(
    datefmt="%Y-%m-%d %H:%M:%S",
    format="%(asctime)s - %(message)s",
    disable_existing_loggers=True,
    logger_name="test2",
)
logger.critical("critical")
```
### output:
![](logging.png)