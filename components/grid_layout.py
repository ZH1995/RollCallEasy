from PySide6.QtWidgets import QGridLayout, QWidget, QSizePolicy

class GridLayoutWidget(QWidget):
    def __init__(self, class_label, class_combobox, student_name_label, roll_call_button, reset_button):
        super().__init__()
        layout = QGridLayout()
        # 设置子组件的大小策略
        class_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        class_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        student_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        roll_call_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        reset_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout.addWidget(class_label, 0, 1)
        layout.addWidget(class_combobox, 0, 2)
        layout.addWidget(student_name_label, 1, 1, 1, 2)
        layout.addWidget(roll_call_button, 2, 0)
        layout.addWidget(reset_button, 2, 3)
        self.setLayout(layout)