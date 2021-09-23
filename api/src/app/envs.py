import os
from distutils import util

from app.settings import ENVIRONMENT


def get_string(name, default=None):
    """
    Get string from environment variable
    @param name:
    @param default:
    @return:
    """
    return os.environ.get(name, default)


def get_bool(name, default=True) -> bool:
    """
    Get boolean value from environment variable
    @param name:
    @param default:
    @return:
    """
    val = os.environ.get(name)
    if val:
        return util.strtobool(val)
    else:
        return default


def get_int(name, default=0) -> int:
    """
    Get integer value from environment variable
    @param name:
    @param default:
    @return:
    """
    val = os.environ.get(name)
    if val:
        return int(val)
    else:
        return default


def is_local_environment() -> bool:
    """
    Check current environment is local
    @return: The true|false
    """
    return True if ENVIRONMENT == 'local' else False


def is_prod_environment() -> bool:
    """
    Check current environment is prod
    @return: The true|false
    """
    if ENVIRONMENT == 'prod':
        return True
    return False
