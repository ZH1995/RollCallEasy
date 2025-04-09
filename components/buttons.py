from PySide6.QtWidgets import QPushButton

class RollCallButton(QPushButton):
    def __init__(self, text="开始点名", parent=None):
        super().__init__(text, parent)

class ResetButton(QPushButton):
    def __init__(self, text="全部重置", parent=None):
        super().__init__(text, parent)