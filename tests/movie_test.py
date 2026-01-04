import os
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
sys.path.append(os.path.join(os.path.dirname(__file__),".."))

from modules.loading_bar import LoadingIcon

class App(QMainWindow):
    def __init__(self):
        super(App,self).__init__()
        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)
        self.pbp = QPushButton("Click me")
        self.loading_icon_widget = LoadingIcon("Hello")
        self.pbp.clicked.connect(self.loading_icon_widget.start_movie)
        self.layout.addWidget(self.loading_icon_widget)
        self.layout.addWidget(self.pbp)
        self.setCentralWidget(self.central_widget)
if __name__ == "__main__":
    app = QApplication()
    window = App()
    window.show()
    app.exec()