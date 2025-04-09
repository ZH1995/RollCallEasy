from PySide6.QtWidgets import QLabel

class ClassLabel(QLabel):
    def __init__(self, text="班级"):
        super().__init__(text)