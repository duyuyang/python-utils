from functools import wraps
import logging, sys

LOGGER_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s"
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
LOGGING_HANDLER_OUT = logging.StreamHandler(sys.stdout)
LOGGING_HANDLER_OUT.setLevel(logging.DEBUG)
LOGGING_HANDLER_OUT.setFormatter(logging.Formatter(LOGGER_FORMAT))
#LOGGING_HANDLER_OUT.addFilter(InfoFilter())
LOGGER.addHandler(LOGGING_HANDLER_OUT)

LOGGING_HANDLER_ERR = logging.StreamHandler(sys.stderr)
LOGGING_HANDLER_ERR.setLevel(logging.WARNING)
LOGGING_HANDLER_ERR.setFormatter(logging.Formatter(LOGGER_FORMAT))
LOGGER.addHandler(LOGGING_HANDLER_ERR)

def logger(function):
    """
    Wrapper function to display function entry and exit for debugging
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        """
        Wrapper definition - uses debug level
        """
        LOGGER.debug('About to run - %s', function.__name__)
        out = apply(function, args, kwargs)
        LOGGER.debug('Done running - %s', function.__name__)
        return out
    return wrapper

@logger
def f(x):
    LOGGER.info("Helo")
    return x

print f(1)
