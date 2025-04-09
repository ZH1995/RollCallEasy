from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt

class StudentLabel(QLabel):
    def __init__(self):
        super().__init__("")
        student_font = self.font()
        student_font.setPointSize(30)
        self.setFont(student_font)
        self.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)