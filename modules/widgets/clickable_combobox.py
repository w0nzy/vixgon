from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import QObject,Signal,Qt
from typing import override

class QComboBox(QComboBox,QObject):
    clicked = Signal(bool)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    @override
    def mousePressEvent(self,event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit(True)
            super().mousePressEvent(event)