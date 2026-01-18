from functools import wraps
from typing import Callable,Any
from modules.vixgon_log import create_logger

logger = create_logger()
def check_db_initialized_or_not(func: Callable) -> bool:
    def wrapper(*args,**kwargs):
        base = args[0]
        session = hasattr(base,"session")
        engine = hasattr(base,"engine")
        if base.__class__.__name__ == "PostgreSQLDB" and not (session and engine):
            logger.warning("Maybe you forget :/ initialize db")
            return False
        return func(*args,**kwargs)
    return wrapper

