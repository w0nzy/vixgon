from PySide6.QtCore import QTimer
from PySide6.QtCore import QObject
from PySide6.QtWidgets import QLabel
class QLabelTyper:
    def __init__(self,base_object,label:QLabel,text: str,duration: int) -> None:
        self.label = label
        self.text = text
        self.duration = duration
        self.timer = QTimer(base_object)
        self.timer.timeout.connect(self.update)
        self.counter = 0
        self.text_len = len(self.text)
    def update(self):

        if self.counter <= self.text_len:
            self.label.setText(self.text[0:self.counter])
            self.counter += 1
        else:
            self.timer.stop()
    def start(self):
        print("Starting typer...")
        self.timer.start(self.duration)
