
# -*- coding: utf-8 -*-




import os
import sys

import requests

from PySide6.QtWidgets import QComboBox, QDialog,QApplication, QMessageBox, QVBoxLayout,QHeaderView,QTableWidgetItem
from PySide6.QtGui import QPixmap,QBrush,QIcon
from PySide6.QtCore import QFile, QObject, Qt,QRect, Signal
from PySide6.QtGui import QPen,QBrush,QPixmap,QIcon
from PySide6.QtWidgets import (QMainWindow,QApplication,QLabel,QFileDialog)
from requests import status_codes
from backend import Database, UserLoginDataModel
from backend.models import UserDataModel
from models.login_ui import QPainter, QWidget, Ui_Dialog
from backend.enums import UserType
from backend.models import ShelfList
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

swallow = lambda **x:x
class VixgonMainApp(QMainWindow,Ui_MainWindow):
    def __init__(self,
                 session: requests.Session,
                 data: UserLoginDataModel = None):
        self.session = session
        self.parent = None
        super(VixgonMainApp,self).__init__()
        self.setupUi(self)
        self.request = Requests("http://127.0.0.1:80",self.session)
        self.user_actions.clicked.connect(lambda:self.tabWidget.setCurrentIndex(0))
        self.item_add_btn.clicked.connect(self.push_photo_list)
        self.data = data
        self.item_management.clicked.connect(self.set_item_management_page_components)
        self.about_btn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(5))
        self.stackedWidget.setCurrentIndex(5)

        self.toolButton_2.clicked.connect(self.handle_item_management_send_button)
        self.toolButton.clicked.connect(self.remove_db)
        self.request.register_func("get-shelfs",handler = self.handle_combobox_items)
    def push_photo_list(self,data):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("PNG (*.png)")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        result = file_dialog.exec()
        if result == 1: # if only file
            self.item_photo_list_table_widget.setRowCount(self.item_photo_list_table_widget.rowCount() + 1)
            self.item_photo_list_table_widget.setItem(self.item_photo_list_table_widget.rowCount() - 1,0,QTableWidgetItem(str(self.item_photo_list_table_widget.rowCount())))
            self.item_photo_list_table_widget.setItem(self.item_photo_list_table_widget.rowCount() - 1,1,QTableWidgetItem(file_dialog.selectedFiles()[0]))
    def setup_ui(self):
        self.user_actions.setIcon(QPixmap(f":/main/assets/gender_{self.data.gender}.png"))
        self.item_shelf_box.view().window().setWindowFlags(Qt.Popup | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
        self.item_shelf_box.view().window().setAttribute(Qt.WA_TranslucentBackground)
        self.item_photo_list_table_widget.setCornerButtonEnabled(False)
        self.item_photo_list_table_widget.verticalHeader().hide()
        self.item_photo_list_table_widget.setHorizontalHeaderLabels(["No","Ürün patikası","Ürün resmi","RAF ADI"])
        self.item_photo_list_table_widget.verticalScrollBar().hide()
        self.item_shelf_box.view().setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.item_photo_list_table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    def set_item_management_page_components(self):
        self.request.get("/vixgon/api/get_shelfs")
        self.stackedWidget.setCurrentIndex(4)
    def remove_db(self):
        ClientDatabase.remove_local_db()
        self.parent.show()
        self.close()
    def handle_combobox_items(self,shelfs: swallow,status_code: int):
        shelfs_ = [x["shelf_name"] for x in shelfs["shelfs"]]
        self.item_shelf_box.addItems(shelfs_)
    def handle_item_management_send_button(self):
        item_name = self.item_name.text()
        if len(shelf) > 0 and len(item_name) > 0:
            item_paths = [self.item_photo_list_table_widget.item(obj,1).text() for obj in range(self.item_photo_list_table_widget.rowCount())]
            item_description = self.textEdit.toPlainText()
            self.request.post("/vixgon/api/create_item",item_name = item_name,item_shelf = shelf,item_description = item_description,item_paths=item_paths)
            return
        
class VixgonLogin(Ui_Dialog,QDialog):
    def __init__(self,parent = None):
        super(VixgonLogin,self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.parent.parent = self
        self.request = Requests("http://127.0.0.1:80")
        self.loading_icon_widget = LoadingIcon()
        self.loading_icon_widget_layout = QVBoxLayout(self.loading_icon_frame)
        self.loading_icon_widget_layout.setContentsMargins(0,0,0,0)
        self.loading_icon_widget_layout.addWidget(self.loading_icon_widget,alignment = Qt.AlignmentFlag.AlignBottom )
        self.request.request_exception.connect(self.post_timeout)
        self.request.request_data.connect(self.handle_server_data)
        self.request.request_bad_authenticate.connect(self.handle_bad_authentication)
        self.login_btn.clicked.connect(self.post_login_data)
        self.setup_ui_at_startup()
    def handle_bad_authentication(self):
        self.status_label.setText("Oturum zaman aşımına uğradı")
        ClientDatabase.remove_local_db()
        self.show()
    def handle_server_data(self,data: requests.Response):
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
        self.parent.request.set_header("Authorization",payload.auth_token)
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
        msgbox = QMessageBox()
        msgbox.setWindowIcon(QIcon(":/main/assets/vixgon_window.icon.png"))
        msgbox.setStyleSheet("QDialog {\n\tbackground-color: #222422;\nfont: 700 11pt 'Candara';\n}\nQLabel {\n\ncolor: #ced9cf;\n}\nQPushButton { background-color: 'gray';\nheight: 30px;\nwidth: 60px;\nborder: 1px solid gray;\nborder-radius: 10px;padding-left: 30px;\npadding-right: 30px;\nmargin-right:15px; \nfont: 700 11pt 'Candara';\ncolor: #ced9cf;}\nQPushButton:hover {\ncolor: '#bf4392';\nbackground-color: #f2b818;}")
        msgbox.setWindowTitle("Bağlantı hatası")
        msgbox.setText("Sunucuya ulaşılamıyor :/")
        msgbox.exec()
        self.close()
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

        self.request.set_header("Authorization",data.token)
        self.request.post("/vixgon/api/login_with_token")
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

    main_app = VixgonMainApp(session)
    main_app.show()
if __name__ == "__main__":
    app = QApplication([])
    main_app = VixgonMainApp(session = None)
    login = VixgonLogin(parent=main_app)
    app.exec()