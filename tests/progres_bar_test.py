import sys
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt, QRectF

class DotProgressBar(QWidget):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.setMinimumSize(300, 50)

    def set_value(self, val):
        self.value = max(0, min(100, val))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        dot_count = 10 
        spacing = 10
        available_width = self.width() - (spacing * (dot_count + 1))
        dot_size = available_width / dot_count
        
        y_pos = (self.height() - dot_size) / 2
        filled_dots = int((self.value / 100) * dot_count)

        for i in range(dot_count):
            x_pos = spacing + i * (dot_size + spacing)
            rect = QRectF(x_pos, y_pos, dot_size, dot_size)
            
            if i < filled_dots:
                painter.setBrush(QColor("#3498db"))
                painter.setPen(Qt.NoPen)
            else:
                painter.setBrush(QColor("#e6e6e6"))
                painter.setPen(Qt.NoPen)
                
            painter.drawEllipse(rect)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DotProgressBar()
    window.set_value(60)
    window.show()
    sys.exit(app.exec())