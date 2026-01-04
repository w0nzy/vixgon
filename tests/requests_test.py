import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))

from modules.request import Requests
from PySide6.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton,QVBoxLayout,QWidget


class Requests_Test(QMainWindow):
    def __init__(self):
        super(Requests_Test,self).__init__()
        self.widget = QWidget()
        self.vbox = QVBoxLayout(self.widget)
        self.qlabel = QLabel("No data")
        self.req = Requests("http://127.0.0.1:8000")
        self.pbp = QPushButton("Click me")
        self.pbp.clicked.connect(lambda:self.req.post("/vixgon/test"))
        self.req.request_exception.connect(lambda:self.qlabel.setText("Timeout error"))
        self.req.request_server_closed.connect(lambda:self.qlabel.setText("Server closed"))
        self.req.request_data.connect(lambda d:self.qlabel.setText(d.text))
        self.vbox.addWidget(self.qlabel)
        self.vbox.addWidget(self.pbp)
        self.setCentralWidget(self.widget)


if __name__ == "__main__":
    app = QApplication([])
    window = Requests_Test()
    window.show()
    app.exec()