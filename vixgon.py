
# -*- coding: utf-8 -*-


import os
import time
import json
import base64
import hashlib
import requests

from PySide6.QtWidgets import QDialog,QApplication
from PySide6.QtGui import QPixmap,QBrush
from PySide6.QtCore import Qt,QRect
from requests import status_codes
from models.login_ui import QPainter, Ui_Dialog
from backend.enums import UserType
from modules.typer_label import QLabelTyper
from PySide6.QtWidgets import (QMainWindow,QApplication)
from PySide6.QtGui import QPen,QBrush,QPixmap,QIcon
from models.vixgon_main_ui import Ui_MainWindow





class Vixgon(QMainWindow,Ui_MainWindow):
    def __init__(self,session,data: dict):
        super(Vixgon,self).__init__()
        self.setupUi(self)
        self.about_btn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(3))
        self.username_text.setText("NaN")
        self.data = data
        self.session = session
        self.setup_ui_begin_startup()
    def setup_ui_begin_startup(self):
        user_action_img = self.data.get("gender","non_identified")
        print("Gender ",user_action_img)
        self.user_actions_pixmap = QPixmap(f":/main/assets/gender_{user_action_img}.png")
        self.user_actions.setIcon(self.user_actions_pixmap)
        self.user_actions.setText("KULLANICI BİLGİSİ" if self.data["user_type"] != 2 else "KULLANICI YÖNETİMİ")
class login_window(QDialog,Ui_Dialog):
    def __init__(self):
        super(login_window,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login")
        self._pixmap = QPixmap(".\\user128px.png")
        self.username_input.returnPressed.connect(self.handle_login)
        self.password_input.returnPressed.connect(self.handle_login)
        self.base_url = "http://127.0.0.1:8000/login" # this is not static may change configuration
        self.login_btn.clicked.connect(self.handle_login)
        self.exit_btn.clicked.connect(self.close)
        self.base_dir = os.path.join(os.path.dirname(__file__),"creds")
        self.local_data_file = os.path.join(self.base_dir,"data.json")
        self.setup_ui_begin_at_startup()
        self.session = requests.Session()
    def handle_login(self):
        save_creds = self.checkbox_user_creds.isChecked()
        username = self.username_input.text()
        password = self.password_input.text()

        username_len = len(username)
        password_len = len(password)
        if (username_len < 4 or password_len < 4):
            self.status_label.setText("Username or password must be at least 4 characters")
            return
        data = self.post(username = username,password = password)
        if (data.get("status",None) is None):
            self.status_label.setText("Server connection problem")
            print(data)
            return
        status = data["status"]
        if (status == "BAD"):
            self.status_label.setText("Invalid username or password")
            return
        data = data["data"]
        self.write_credentials(username=username,name=data["name"],surname=data["surname"],photo=data["user_photo"])
        self.status_label.setText("Giriş başarılı")
        app = Vixgon(self.session,data)
        app.show()
        self.close()
    def setup_ui_begin_at_startup(self):
        self.password_input.setPlaceholderText("Enter your password")
        self.pixmap = QPixmap()
        data = None
        if os.path.exists(self.local_data_file) and self.get_local_data().get("username") != None:
            data = self.get_local_data()
            self.typer = QLabelTyper(self,self.username_text, "Greetings %s %s :)" % (data["name"],data["surname"]), 50)
            self.typer.start()
        self.pixmap.loadFromData(data["photo"] if data is not None else self.get_png_data())
        self.rounded_pixmap = QPixmap(self.pixmap.size())
        self.rounded_pixmap.fill(Qt.transparent)
        painter = QPainter(self.rounded_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(self.pixmap))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self.pixmap.rect(), 300,300)
        self.user_icon_label.setPixmap(self.rounded_pixmap)
    def post(self,**kwargs) -> dict:
        self.session
        try:
            data = self.session.post(self.base_url,json=kwargs)
        except Exception as e:
            print("Error ",e)
            return {"error":None}
        return data.json()
    def write_credentials(self,**kwargs):
        if not os.path.exists(self.base_dir):
            try:
                os.makedirs(self.base_dir)
            except:
                return
        try:
            data = json.dumps(kwargs)
            with open(os.path.join(self.local_data_file),"w") as fd:
                fd.write(data)
        except Exception as photo_write_error:
            self.status_label.setText("Cannot write photo data")
            return False
        return True
    def get_local_data(self) -> dict:
        return_data = {"username":None}
        if (os.path.exists(self.local_data_file)):
            try:
                with open(self.local_data_file,"r") as fd:
                    data = fd.read()
                data = json.loads(data)
                username = data.get("username","_bad_username")
                userphoto = data.get("photo","_bad_photo")
                name = data.get("name","_bad_name")
                surname = data.get("surname","_bad_surname")
                return_data["username"] = username
                return_data["photo"] = base64.b64decode(userphoto.encode())
                return_data["name"] = name
                return_data["surname"] = surname
            except IOError:
                self.status_label.setText("Cannot read local data")
            except json.JSONDecodeError:
                self.status_label.setText("Json parsing error")
            except Exception as non_identified_error:
                self.status_label.setText("Non identified error %s" % (str(non_identified_error)))
        return return_data
    def get_png_data(self):
        try:
            with open(os.path.join(os.path.dirname(__file__),"assets","vixgon_window.icon.png"),"rb") as fd:
                return fd.read()
        except Exception as err:
            print("Error ",err)
            return b""
if __name__ == "__main__":
    app = QApplication()
    window = login_window()
    window.show()
    app.exec()