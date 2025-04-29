# Roll Call Easy

一个基于 PySide6 的点名工具，支持随机点名和重置功能，适用于课堂或其他需要随机选择的场景。

deepwiki：https://deepwiki.com/ZH1995/RollCallEasy/1-overview

## 功能特性

- **随机点名**：从指定班级中随机选择一名学生。
- **班级管理**：支持从配置文件中加载班级和学生信息。
- **重置功能**：清空已点名的学生列表，重新开始点名。

## 项目结构

```
RollCallEasy/
├── app.py # 主程序入口
├── components/ # 界面组件
│ ├── combobox.py # 班级下拉框组件
│ ├── grid_layout.py # 网格布局组件
│ └── ... # 其他组件
├── service/ # 服务逻辑
│ └── roll_cal.py # 点名服务
├── spec/ # PyInstaller 打包配置 
│ ├── mac/ # macOS 打包配置 
│ │ └── config.json # 配置文件 
│ └── windows/ # Windows 打包配置 
├── requirements.txt # 项目依赖 
└── README.md
```

## 安装与运行

### 环境要求

- Python 3.12 或更高版本
- pip 包管理工具

### 安装依赖

在项目根目录下运行以下命令安装依赖：

```bash
pip install -r requirements.txt
```

**注意**:由于国内网络的原因，安装PySide6可能需要执行如下命令：

```bash
python3 -m pip install PySide6 --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org
```

### 运行项目

在项目根目录下运行以下命令启动程序：

```bash
python app.py
```

## 配置文件

配置文件 config.json 用于定义班级和学生信息，格式如下：

```json
{
  "class_list": {
    "班级名称1": ["学生1", "学生2", "学生3"],
    "班级名称2": ["学生4", "学生5", "学生6"]
  }
}
```

## 打包应用

### macOS 打包

在打包前，将 config.json 文件拷贝到 spec/mac 目录下，然后运行以下命令：

```bash
pyinstaller --onefile --windowed --name=roll_call_easy --add-data="config.json:." --hidden-import=PySide6 --hidden-import=PySide6.QtWidgets --hidden-import=PySide6.QtCore --hidden-import=PySide6.QtGui --distpath=./output/mac --workpath=./build/mac --specpath=./spec/mac app.py
```

### Windows 打包

在打包前，将 config.json 文件拷贝到 spec/windows 目录下，然后运行以下命令：

```bash
pyinstaller --onefile --windowed --name=roll_call_easy --add-data="config.json:." --hidden-import=PySide6 --hidden-import=PySide6.QtWidgets --hidden-import=PySide6.QtCore --hidden-import=PySide6.QtGui --distpath=./output/windows --workpath=./build/windows --specpath=./spec/windows app.py
```

## 使用说明
1. 启动程序后，选择班级。
2. 点击“开始点名”按钮，随机选择一名学生。
3. 点击“重置”按钮，清空已点名的学生列表。

## 依赖

项目依赖如下：

- PySide6==6.5.2

## 贡献

欢迎提交 Issue 或 Pull Request 来改进本项目。

## 许可证

本项目基于 MIT 许可证开源。
