
# -*- coding: utf-8 -*-



from http import client
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
from backend import Database, UserLoginDataModel
from backend.models import UserDataModel
from models.login_ui import QPainter, Ui_Dialog
from backend.enums import UserType
from models.vixgon_main_ui import Ui_MainWindow
from modules.request import Requests
from modules.widgets.loading_bar import LoadingIcon
from modules.widgets.typer_label import QLabelTyper
from modules.widgets.rounded_label import RoundedLabel
from modules.db import ClientDatabase
from modules.db_models import LocalCredentialsModel
from modules.error_handling import error

from modules import get_app_path, get_assets_path, get_local_database_path

sys.path.append(os.path.dirname(__file__))




class SignalClass(QObject):
    closed = Signal(requests.Session)

class VixgonMainApp(QMainWindow,Ui_MainWindow):
    def __init__(self,session: requests.Session,data: UserLoginDataModel = None):
        self.session = session
        super(VixgonMainApp,self).__init__()
        self.setupUi(self)
        self.request = Requests("http://127.0.0.1:8000",self.session)
        self.about_btn.clicked.connect(lambda:self.request.post("/vixgon/api/get_user/alperen"))
        self.user_actions.clicked.connect(lambda:self.tabWidget.setCurrentIndex(0))
        self.data = data
    def setup_ui(self):
        self.user_actions.setIcon(QPixmap(f":/main/assets/gender_{self.data.gender}.png"))
class VixgonLogin(Ui_Dialog,QDialog):
    def __init__(self,parent = None):
        super(VixgonLogin,self).__init__()
        self.setupUi(self)
        self.signal = SignalClass()
        self.parent = parent
        self.request = Requests("http://127.0.0.1:80")
        self.loading_icon_widget = LoadingIcon()
        self.loading_icon_widget_layout = QVBoxLayout(self.loading_icon_frame)
        self.loading_icon_widget_layout.setContentsMargins(0,0,0,0)
        self.loading_icon_widget_layout.addWidget(self.loading_icon_widget,alignment = Qt.AlignmentFlag.AlignBottom )
        self.request.request_exception.connect(self.post_timeout)
        self.request.request_begin.connect(lambda:self.status_label.setText("Sunucuya bağlanılıyor"))
        self.request.request_data.connect(self.handle_server_data)
        self.login_btn.clicked.connect(self.post_login_data)
        self.setup_ui_at_startup()
    def handle_server_data(self,data: requests.Response):
        if data.status_code == 401:
            self.status_label.setText("Oturum zaman aşımına uğradı :/")
            ClientDatabase.remove_local_db()
            self.show()
            return
        payload = UserLoginDataModel(**data.json())
        if payload.user_name == "no_username":
            self.status_label.setText("Kullanıcı adı/parola yanlış")
            return
        if self.checkbox_user_creds.isChecked():
            client_db = ClientDatabase()
            client_db.init_db()
            client_db.push_user_login_credentials(
                user_data = LocalCredentialsModel(
                    username = payload.user_name,
                    token = payload.auth_token,
                    user_photo = payload.user_photo,
                    user_photo_path="user.png"
                    )
                )
            client_db.close()
        self.parent.data = payload
        self.close()
        self.parent.setup_ui()
        self.parent.show()
    def post_login_data(self):
        username_len = len(self.username_input.text())
        password_len = len(self.password_input.text())
        if (not 0 < username_len <= 25 and not 0 < password_len <= 25):
            self.status_label.setText("Kullanıcı adı/parola kısa")
            return
        self.loading_icon_widget.start_movie()
        self.request.post("/vixgon/api/login_test",username = self.username_input.text(),password = self.password_input.text(),remember_me = self.checkbox_user_creds.isChecked())
    def post_timeout(self):
        self.status_label.setText("Sunucuya ulaşılamıyor")
    def check_db_exists(self) -> bool:
        return os.path.exists(get_local_database_path())
    def get_db_data(self) -> LocalCredentialsModel:
        local_db = ClientDatabase()
        local_db.init_db()
        data = local_db.extract_user_credentials()
        local_db.close()
        return data
    def post_login_data_with_token(self):
        data = self.get_db_data()
        print("Token is ",data)
        self.request.post("/vixgon/api/login_with_token/{token}?token_data=%s" % (data.token))
    def show_widgets(self):
        self.password_input.show()
        self.username_input.show()
        self.checkbox_user_creds.show()
    def hide_widgets(self):
        self.password_input.hide()
        self.username_input.hide()
        self.checkbox_user_creds.hide()
    def setup_ui_at_startup(self):
        if self.check_db_exists():
            self.post_login_data_with_token()
            return
        self.show()
def launch_main_app(session: requests.Session):
    print("Launching app")
    main_app = VixgonMainApp(session)
    main_app.show()
if __name__ == "__main__":
    app = QApplication([])
    main_app = VixgonMainApp(session = None)
    login = VixgonLogin(parent=main_app)
    app.exec()