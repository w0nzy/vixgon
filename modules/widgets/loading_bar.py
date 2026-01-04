import os
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from modules import get_assets_path
class LoadingIcon(QWidget):
    def __init__(self,label_text: str = ""):
        super(LoadingIcon,self).__init__()
        self.label_text = label_text
        self.gif_path = get_assets_path("gif","loading.gif")
        if not os.path.exists(self.gif_path) or os.path.isdir(self.gif_path):
            raise OSError("Bad image path %s not exists or not file :/" % (self.gif_path))
        self.vertical_layout = QVBoxLayout(self)
        self.text_label = QLabel(self.label_text)
        self.text_label.setStyleSheet("font: 700 11pt 'Candara';\ncolor:#687069;")
        self.gif_label = QLabel()
        self.gif_label.setScaledContents(True)
        self.gif_label.setFixedSize(50,50)
        self.setMaximumHeight(70)
        self.movie = QMovie(get_assets_path("gif","loading.gif"))
        self.gif_label.setMovie(self.movie)
        self.vertical_layout.addWidget(self.gif_label,alignment = Qt.AlignmentFlag.AlignCenter)
        self.vertical_layout.addWidget(self.text_label,alignment = Qt.AlignmentFlag.AlignCenter)
        self.hided = False
    def start_movie(self):
        if self.hided:
            self.show()
            self.hided = False
        self.movie.start()
    def stop_movie(self):
        self.movie.stop()
    def hide_widget(self):
        self.hided = True
        self.movie.stop()
        self.hide()
    def set_gif_size(self,w: int,h: int):
        self.gif_label.setFixedSize(w,h)