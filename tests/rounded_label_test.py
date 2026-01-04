import os
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
sys.path.append(os.path.join(os.path.dirname(__file__),".."))

from modules.widgets.rounded_label import RoundedLabel
from modules import get_assets_path
class Rounded_LabelTest(QMainWindow):
    def __init__(self):
        super(Rounded_LabelTest,self).__init__()
        self.widget = QWidget()
        self.rounded_label = RoundedLabel(get_assets_path("alperen.png"))
        self.vbox = QVBoxLayout(self.widget)
        self.vbox.addWidget(self.rounded_label)
        self.setCentralWidget(self.widget)
if __name__ == "__main__":
    app = QApplication([])
    window = Rounded_LabelTest()
    window.show()
    app.exec()