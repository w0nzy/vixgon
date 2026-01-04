
# -*- coding: utf-8 -*-



import os
import sys
import time
import json
import base64
import hashlib
import requests

from PySide6.QtWidgets import QDialog,QApplication, QVBoxLayout
from PySide6.QtGui import QPixmap,QBrush
from PySide6.QtCore import QObject, Qt,QRect, Signal
from PySide6.QtGui import QPen,QBrush,QPixmap,QIcon
from PySide6.QtWidgets import (QMainWindow,QApplication,QLabel)

from requests import status_codes
from backend import UserLoginDataModel
from models.login_ui import QPainter, Ui_Dialog
from backend.enums import UserType
from models.vixgon_main_ui import Ui_MainWindow
from modules.request import Requests
from modules.widgets.loading_bar import LoadingIcon
from modules.widgets.typer_label import QLabelTyper
from modules.widgets.rounded_label import RoundedLabel
from modules.db import ClientDatabase
from modules.db_models import LocalCredentialsModel

from modules import get_app_path, get_local_database_path

sys.path.append(os.path.dirname(__file__))




class SignalClass(QObject):
    closed = Signal(requests.Session)

class VixgonMainApp(QMainWindow,Ui_MainWindow):
    def __init__(self,session: requests.Session):
        self.session = session
        super(VixgonMainApp,self).__init__()
        self.setupUi(self)
        self.request = Requests("http://127.0.0.1:8000",self.session)
        self.about_btn.clicked.connect(lambda:self.request.post("/vixgon/api/get_user/alperen"))
class VixgonLogin(Ui_Dialog,QDialog):
    def __init__(self,parent = None):
        super(VixgonLogin,self).__init__()
        self.setupUi(self)
        self.signal = SignalClass()
        self.parent = parent
        self.request = Requests("http://127.0.0.1:8000")
        self.loading_icon_widget = LoadingIcon()
        self.loading_icon_widget_layout = QVBoxLayout(self.loading_icon_frame)
        self.loading_icon_widget_layout.setContentsMargins(0,0,0,0)
        self.loading_icon_widget_layout.addWidget(self.loading_icon_widget,alignment = Qt.AlignmentFlag.AlignBottom )
        self.request.request_exception.connect(self.set_result_to_bad)
        self.request.request_begin.connect(lambda:self.status_label.setText("Sunucuya bağlanılıyor"))
        self.request.request_data.connect(self.handle_server_data)
        self.login_btn.clicked.connect(self.post_login_data)
        self.setup_ui_at_startup()
    def post_login_data(self):
        username_len = len(self.username_input.text())
        password_len = len(self.password_input.text())
        if (not 6 < username_len <= 25) or (not 6 < password_len <= 25):
            self.status_label.setText("Kullanıcı adı veya parola izin verilen maximum karakteri aşıyor max:25")
            return
        self.request.post("/vixgon/login_test",username = self.username_input.text(),password = self.password_input.text())
        self.loading_icon_widget.start_movie()
    def set_result_to_bad(self):
        self.loading_icon_widget.hide_widget()
        self.status_label.setText("Sunucuya ulaşılamıyor :/")
    def handle_server_data(self,response):
        self.status_label.setText("Sunucuya bağlanıldı ")
        self.loading_icon_widget.hide_widget()
        payload = UserLoginDataModel(**response.json()) # its not safe :/
        if payload.user_name == "no_username":
            self.status_label.setText("Kullanıcı bilgileri hatalı")
            return
        if self.checkbox_user_creds.isChecked():
            local_database = ClientDatabase()
            local_database.init_db()
            local_database.push_user_login_credentials(user_data=
                LocalCredentialsModel(
                    username = payload.user_name,
                    token = payload.auth_token,
                    user_photo = payload.user_photo
                    )
                )
            local_database.close()
        self.parent.session = self.request.session 
        self.parent.show()
        self.close()
    def setup_ui_at_startup(self):
        if os.path.exists(get_local_database_path()):
            database = ClientDatabase()
            database.init_db()
            user_data = database.extract_user_credentials()
            self.rounded_label = RoundedLabel(user_data.user_photo_path)
            self.user_greeting_label = QLabel()
            self.verticalLayout_4.setSpacing(10)
            self.typer = QLabelTyper(self, self.user_greeting_label,"Merhaba," + user_data.username ,50)
            self.verticalLayout_4.addWidget(self.rounded_label,alignment = Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
            self.verticalLayout_4.addWidget(self.user_greeting_label,alignment = Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom)
            self.typer.start()
def launch_main_app(session: requests.Session):
    print("Launching app")
    main_app = VixgonMainApp(session)
    main_app.show()
if __name__ == "__main__":
    app = QApplication([])
    main_app = VixgonMainApp(session = None)
    login = VixgonLogin(parent=main_app)
    login.show()

    app.exec()