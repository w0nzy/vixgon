import os
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap,QPainter,QBrush
from PySide6.QtCore import Qt
class RoundedLabel(QLabel):
    def __init__(self,image_path: str = ""):
        super(RoundedLabel,self).__init__()
        self.image_path = image_path
        if not os.path.exists(self.image_path) or os.path.isdir(self.image_path):
            raise OSError("%s is not exists or not a file :/" % (self.image_path))
        self.orig_pixmap = QPixmap(self.image_path)
        self.rounded_pixmap = QPixmap(self.orig_pixmap.size())
        self.rounded_pixmap.fill(Qt.transparent)
        self.painter = QPainter(self.rounded_pixmap)
        self.painter.setRenderHint(QPainter.Antialiasing)
        self.painter.setBrush(QBrush(self.orig_pixmap))
        self.painter.setPen(Qt.NoPen)
        self.painter.drawRoundedRect(self.orig_pixmap.rect(), 300,300)
        self.setScaledContents(True)
        self.setPixmap(self.rounded_pixmap)
        self.setStyleSheet("border: 3px solid orange;\nborder-radius: 35px;")
        self.setFixedSize(150,150)
