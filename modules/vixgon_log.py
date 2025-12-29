import os
import time
import logging


from . import is_running_exe
def create_logger():
    log_filename = "vixgon_log_%s.txt" % (time.strftime("%d_%m_%y"))
    log_file_path = os.path.join(os.path.dirname(__file__),os.path.join("..","log") if not is_running_exe() else "log",log_filename)
    os.makedirs(os.path.dirname(log_file_path),exist_ok=True)
    log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s - %(lineno)s")
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setFormatter(log_format)
    logging.basicConfig(handlers=[file_handler],encoding="utf-8",level = logging.DEBUG)
    return logging.getLogger()