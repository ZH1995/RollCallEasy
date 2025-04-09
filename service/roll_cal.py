import json
import random
import os
import sys
class RollCallService:
    def __init__(self, config_path="config.json"):
        # 获取应用程序根目录路径
        if getattr(sys, 'frozen', False):
            # PyInstaller打包后的路径
            base_path = sys._MEIPASS
        else:
            # 开发环境中的路径
            base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        self.config_path = os.path.join(base_path, config_path)

        print("zhanghe :" + self.config_path)
        self.class_students = {}
        self.selected_students = []
        self.load_students()

    def load_students(self):
        # 从配置文件中加载学生列表
        with open(self.config_path, "r", encoding="utf-8") as config_file:
            config = json.load(config_file)
        self.class_students = config.get("class_list", {})

    def get_random_student(self, class_name):
        # 获取指定班级的学生列表
        students = self.class_students.get(class_name, [])
        # 去重后随机选择一名学生
        available_students = [s for s in students if s not in self.selected_students]
        if not available_students:
            return None  # 如果没有可选学生，返回 None
        student = random.choice(available_students)
        self.selected_students.append(student)
        return student

    def reset(self):
        # 重置已选学生列表
        self.selected_students = []