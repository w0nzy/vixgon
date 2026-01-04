import os
import time
import logging


from . import is_running_exe


class ColorizedFormat(logging.Formatter):
    color_table = {
        logging.INFO:"\033[1;92m",
        logging.CRITICAL:"\033[1;31m",
        logging.WARNING:"\033[1;33m"
    }
    def format(self,record):
        fmt = self.get_format(record.levelno)
        formatter = logging.Formatter(fmt)
        return formatter.format(record)
    @classmethod
    def get_format(cls,level: int) -> str:
        return cls.color_table.get(level,"\033[1;0m")  + "%(levelname)s" + "\033[1;0m"+ ":\t %(filename)s::Says \033[1;97m %(message)s at line %(lineno)d " + "\033[1;0m"

def create_logger():
    log_filename = "vixgon_log_%s.txt" % (time.strftime("%d_%m_%y"))
    log_file_path = os.path.join(os.path.dirname(__file__),os.path.join("..","log") if not is_running_exe() else "log",log_filename)
    os.makedirs(os.path.dirname(log_file_path),exist_ok=True)
    log_file_format = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s - %(lineno)s")
    file_handler = logging.FileHandler(log_file_path)
    colorized_formatter = ColorizedFormat()
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(colorized_formatter)
    stream_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(log_file_format)
    logging.basicConfig(handlers=[file_handler,stream_handler],encoding="utf-8",level = logging.DEBUG)
    return logging.getLogger()