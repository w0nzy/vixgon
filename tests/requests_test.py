import os,sys

sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from modules.request import Requests

from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QWidget,QLabel,QVBoxLayout,QPushButton
from pydantic import BaseModel
from dataclasses import field
class LabelTest(BaseModel):
    text: str = field(default="no_data")
class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp,self).__init__()
        self.requests = Requests("http://localhost:5000")
        self.requests.register_func("set_label",handler = self.handle)
        self.main_widget = QWidget()
        self.vbox_layout = QVBoxLayout(self.main_widget)
        self.label = QLabel("No data")
        self.pbp = QPushButton("Click me")
        self.pbp.clicked.connect(lambda:self.requests.post("/get_label"))
        self.vbox_layout.addWidget(self.label)
        self.vbox_layout.addWidget(self.pbp)
        self.setCentralWidget(self.main_widget)
    def handle(self,data: LabelTest,status_code: int):

        if data.text != "no_data":
            self.label.setText(data.text)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec()