import errno
import requests
from urllib3 import exceptions
from typing import override
from PySide6.QtCore import QObject
from PySide6.QtCore import Signal
from PySide6.QtCore import QThreadPool
from PySide6.QtCore import QRunnable
import urllib3

from modules.error_handling import geterrno
from modules.vixgon_log import create_logger
logger = create_logger()

class Workerw(QRunnable):
    def __init__(self,session: requests.Session,signal_class: QObject,url: str,**kw):
        super().__init__()
        self.session = session if isinstance(session,requests.Session) else requests.Session()
        self.base_url = url
        self.kwargs = kw
        self.parent = signal_class
    def run(self):
        self.parent.request_begin.emit(True)
        try:
            result = self.session.post(self.base_url,json = self.kwargs,timeout=1)
            self.parent.request_data.emit(result)
        except Exception as e:
            logger.critical("Cannot reach server %s -> %s" % (self.base_url,str(e)))
            self.parent.request_exception.emit(True)

class Requests(QObject):
    request_begin = Signal(bool)
    request_data = Signal(requests.Response) # at startup
    request_exception = Signal(bool) # if error occured
    def __init__(self,base_url: str,session: requests.Session = None):
        super().__init__()
        self.base_url = base_url
        self.threadpool = None
        self.session = session
        self.url = ""
        self.kws = {}
        self.test_thread = None
        self.threadpool = QThreadPool().globalInstance()
    def post(self,url: str = "",**kwargs):
        print(url)
        self.url = url
        self.kws = kwargs
        self.test_thread = Workerw(self.session,self,self.base_url + url,**self.kws)
        self.threadpool.start(self.test_thread)
    def __repr__(self):
        return "<%s base_url = %s>" % (self.__class__.__name__,self.base_url)