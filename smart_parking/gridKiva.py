import kivaUI
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont
from functools import partial

class MainDialog(QtWidgets.QDialog, kivaUI.Ui_Dialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setStyleSheet("background-color: #9999CC;")

        # 設定不同的檔案和每個佈局的第一個label index
        self.files = [
            ("./results/model_cargo.txt", 1),
            ("./results/model_robot.txt", 1),
            ("./results/model_cargo.txt", 10),
            ("./results/model_robot.txt", 10),
            ("./results/model_cargo.txt", 19),
            ("./results/model_robot.txt", 19),
            ("./results/model_cargo.txt", 28),
            ("./results/model_robot.txt", 28)
        ]

        self.steps = []  # 每個方法的步驟
        self.current_steps = [0] * len(self.files)  # 每個方法的當前步驟
        self.timers = []

        for file, _ in self.files:
            self.steps.append(self.read_file(file))

        for i in range(len(self.files)):
            timer = QTimer()
            timer.timeout.connect(partial(self.update_grid, i))  # 使用 partial 傳遞 index
            self.timers.append(timer)

        self.setupUi(self)
        self.show_initial_states()  # 顯示初始狀態

    def read_file(self, filename):
        steps = []
        try:
            with open(filename, "r") as file:
                grid = []
                for line in file:
                    line = line.strip()
                    if line:
                        grid.append([int(x) if x.isdigit() or x == "-1" else 0 for x in line.split()])
                    else:
                        if grid:
                            steps.append(grid)
                            grid = []
                if grid:  # 清理最後一個步驟
                    steps.append(grid)
        except Exception as e:
            print(f"Error reading file {filename}: {e}")
            return [np.zeros((3, 3))]
        return steps

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.modelLabel.setFont(QFont("Arial", 14, QFont.Bold))
        self.gdLabel.setFont(QFont("Arial", 14, QFont.Bold))
        self.gnLabel.setFont(QFont("Arial", 14, QFont.Bold))
        self.psoLabel.setFont(QFont("Arial", 14, QFont.Bold))
        self.kivaLabel.setFont(QFont("Arial", 16, QFont.Bold))
        self.kivaLabel.setStyleSheet("background-color: Yellow; color: black;")
        self.egLabel.setFont(QFont("Arial", 14, QFont.Bold))
        self.egLabel.setStyleSheet("background-color: Gray; color: white;")
        self.pushButton.setFont(QFont("Arial", 10, QFont.Bold))
        self.pushButton.setStyleSheet("background-color: Red; color: white;")

        self.pushButton.clicked.connect(self.start_execution)  # 連結按鈕點擊事件

    # 顯示每個方法的初始狀態
    def show_initial_states(self):
        for method_idx in range(len(self.files)):
            self.update_grid(method_idx, initial=True)

    def start_execution(self):
        for timer in self.timers:
            timer.start(1000)  # 每個方法每秒更新一步

    def update_grid(self, method_idx, initial=False):
        if initial:
            step = 0
        elif self.current_steps[method_idx] < len(self.steps[method_idx]):
            step = self.current_steps[method_idx]
            self.current_steps[method_idx] += 1
        else:
            self.timers[method_idx].stop()
            self.set_method_label_red(method_idx)
            return

        grid = self.steps[method_idx][step]
        start_index = self.files[method_idx][1]
        index = start_index

        # 如果是貨物層，對應機器人層為 method_idx + 1
        robot_grid = self.steps[method_idx + 1][step] if method_idx % 2 == 0 else None

        STYLES = {
            "obs": "background-color: gray",
            "spa": "background-color: white",
            "cargo": "background-color: blue; color: white",
            "rob": "background-color: yellow; color: black; border-radius: 40px;",
            "tran": "background-color: transparent;",
        }

        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                label_name = f"{'klabel' if method_idx % 2 == 0 else 'label'}_{index}"
                label = getattr(self, label_name, None)

                label_name2 = f"{'klabel' if method_idx % 2 == 0 else None}_{index}"
                clabel = getattr(self, label_name2, None)

                if label:
                    if method_idx % 2 == 0:  # 貨物層 (kLabel)
                        if value == -1:  # 障礙物
                            label.setText("")
                            label.setStyleSheet(STYLES["obs"])
                        elif value == 0:  # 空格
                            if robot_grid and robot_grid[i][j] == 0:
                                label.setText("")
                                label.setStyleSheet(STYLES["spa"])
                        else:  # 貨物
                            label.setText(str(value))
                            label.setFont(QFont("Arial", 14, QFont.Bold))
                            label.setStyleSheet(STYLES["cargo"])
                    else:  # 機器人層 (label)
                        if value == 0:  # 空格
                            label.setText("")
                            label.setStyleSheet(STYLES["tran"])
                        else:  # 機器人
                            label.setText("")
                            label.setStyleSheet(STYLES["rob"])
                index += 1

        self.update_step_label(method_idx, step)


    def update_step_label(self, method_idx, step):
        method_map = {
            0: "Kiva模型",
            1: "貪婪演算法",
            2: "基因演算法",
            3: "粒子群演算法"
        }
        method_name = method_map.get(method_idx // 2)
        labels = [self.modelLabel, self.gdLabel, self.gnLabel, self.psoLabel]
        if 0 <= method_idx // 2 < len(labels):
            labels[method_idx // 2].setText(f"{method_name}: 第 {step} 步")

    def set_method_label_red(self, method_idx):
        labels = [self.modelLabel, self.gdLabel, self.gnLabel, self.psoLabel]
        if 0 <= method_idx // 2 < len(labels):
            labels[method_idx // 2].setStyleSheet("background-color: pink; color: black;")
