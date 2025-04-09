import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
)
from components import (
    ClassLabel,
    StudentLabel,
    ClassComboBox,
    RollCallButton,
    ResetButton
)
from components.grid_layout import GridLayoutWidget
from service.roll_cal import RollCallService

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Roll call Easy")
        self.resize(800, 600)
        # 初始化点名服务
        self.roll_call_service = RollCallService()

        # 学生姓名
        self.student_name = ""

        # 班级标签
        class_label = ClassLabel()
        # 学生姓名标签
        self.studentNameLabel = StudentLabel()
        # 班级下拉框
        self.class_combobox = ClassComboBox()
        self.class_combobox.currentTextChanged.connect(self.text_changed)

        # 开始点名按钮
        roll_call_button = RollCallButton()
        roll_call_button.clicked.connect(self.roll_call_button_clicked)
        # 重置按钮
        reset_button = ResetButton()
        reset_button.clicked.connect(self.reset_button_clicked)
        # 网格布局
        widget = GridLayoutWidget(class_label, self.class_combobox, self.studentNameLabel, roll_call_button, reset_button)
        self.setCentralWidget(widget)

    def roll_call_button_clicked(self):
        class_name = self.class_combobox.currentText()
        student = self.roll_call_service.get_random_student(class_name)
        if student:
            self.student_name = student
            self.studentNameLabel.setText(self.student_name)
        else:
            self.studentNameLabel.setText("无可选学生")

    def reset_button_clicked(self):
        self.roll_call_service.reset()
        self.student_name = ""
        self.studentNameLabel.setText(self.student_name)

    def text_changed(self, text):
        pass

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()