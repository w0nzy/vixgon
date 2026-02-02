import errno
import requests
from typing import Any, Callable
from PySide6.QtCore import QObject
from PySide6.QtCore import Signal
from PySide6.QtCore import QThreadPool
from PySide6.QtCore import QRunnable

from modules.error_handling import geterrno
from modules.vixgon_log import create_logger
logger = create_logger()

class Workerw(QRunnable):
    def __init__(self,session: requests.Session,signal_class: QObject,url: str,**kw):
        super().__init__()
        self.session = session
        self.base_url = url
        self.kwargs = kw
        self.parent = signal_class
        self.func = self.post_
    def get_(self,url: str,**kws):
        return self.session.get(url,**kws)
    def post_(self,url: str,**kws):
        return self.session.post(url,**kws)
    def run(self):
        self.parent.request_begin.emit(True)
        try:
            result = self.func(self.base_url,json = self.kwargs,timeout=1)
            if result.status_code == 401:
                self.parent.request_bad_authenticate.emit(True)
                return
            self.parent.request_data.emit(result)
        except Exception as e:
            logger.critical("Cannot reach server %s -> %s" % (self.base_url,str(e)))
            self.parent.request_exception.emit(True)
   
class Requests(QObject):
    request_begin = Signal(bool)
    request_data = Signal(requests.Response) # at startup
    request_bad_authenticate = Signal(bool)
    request_exception = Signal(bool) # if error occured
    def __init__(self,base_url: str,session: requests.Session = None,token: str = None):
        super().__init__()
        self.base_url = base_url
        self.threadpool = None
        self.session = session  if isinstance(session,requests.Session) else requests.Session()
        self.url = ""
        self.kws = {}
        self.test_thread = None
        self.threadpool = QThreadPool().globalInstance()
        self.registers = {}
        self.request_data.connect(lambda x:self.handle_data(x))
        if isinstance(token,str):
            self.session.set_header("Authorization",token)
    def post(self,url: str,**kwargs):

        self.url = url
        self.kws = kwargs
        self.test_thread = Workerw(self.session,self,self.base_url + url,**self.kws)
        self.test_thread.func = self.test_thread.post_
        self.threadpool.start(self.test_thread)
    def get(self,url: str = "",**kwargs):
        self.test_thread = Workerw(self.session,self,self.base_url + url,**kwargs)
        self.test_thread.func = self.test_thread.get_
        self.threadpool.start(self.test_thread)
    def register_func(self,action: str,*,handler: Callable):
         if (len(handler.__annotations__) != 2):
             raise ValueError("function must be have annotations :/ or status code parameter")
         self.registers[action] = handler
    def handle_data(self,payload: requests.Response):

        if (payload.headers.get("action") is None):
            logger.warning("No action :/")
            return
        action = payload.headers.get("action")
        if self.registers.get(action) is None:
            logger.warning("No function registered for %s action" % (action))
            return
        try:
            function = self.registers.get(action)
            model_type,_ = function.__annotations__.values()
            function(model_type(**payload.json()),payload.status_code)
        except Exception as exec_error:
            logger.critical("Execution failed for %s register error is %s" % (self.registers.get(action).__name__,str(exec_error)))
    def set_header(self,key: str,value: Any):
        self.session.headers[key] = value
    def __repr__(self):
        return "<%s base_url = %s>" % (self.__class__.__name__,self.base_url)