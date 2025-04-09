import json
import os
import sys
from PySide6.QtWidgets import QComboBox

class ClassComboBox(QComboBox):
    def __init__(self, config_path="config.json"):
        super().__init__()
        # 获取应用程序根目录路径
        if getattr(sys, 'frozen', False):
            # PyInstaller打包后的路径
            base_path = sys._MEIPASS
        else:
            # 开发环境中的路径
            base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

        config_file_path = os.path.join(base_path, config_path)

        with open(config_file_path, "r", encoding="utf-8") as config_file:
            config = json.load(config_file)
        class_dict = config.get("class_list", {})
        self.addItems(class_dict.keys())