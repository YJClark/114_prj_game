import numpy as np
import methodsUI
from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont
from functools import partial

class MainDialog(QtWidgets.QDialog, methodsUI.Ui_Dialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setStyleSheet("background-color: #9999CC;")

        # 設定不同的檔案和第一個label index
        self.files = [
            ("./results/obs.txt", 1),
            ("./results/spa.txt", 10),
            ("./results/bfs.txt", 19),
            ("./results/maac.txt", 28)
        ]

        self.steps = []  # 每個方法的步驟
        self.current_steps = [0] * len(self.files)  # 每個方法的當前步驟
        self.timers = []

        for file, _ in self.files:
            self.steps.append(self.read_file(file))

        for i in range(len(self.files)):
            timer = QTimer()
            timer.timeout.connect(partial(self.update_grid, i))  # 使用 partial 傳遞index
            self.timers.append(timer)
            # timer.start(1000)

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
        self.obsLabel.setFont(QFont("Arial", 14, QFont.Bold))
        self.spaLabel.setFont(QFont("Arial", 14, QFont.Bold))
        self.bfsLabel.setFont(QFont("Arial", 14, QFont.Bold))
        self.maacLabel.setFont(QFont("Arial", 14, QFont.Bold))
        self.puzzleLabel.setFont(QFont("Arial", 16, QFont.Bold))
        self.puzzleLabel.setStyleSheet("background-color: Yellow; color: black;")
        self.egLabel.setFont(QFont("Arial", 14, QFont.Bold))
        self.egLabel.setStyleSheet("background-color: Gray; color: white;")
        self.pushButton.setFont(QFont("Arial", 10, QFont.Bold))
        self.pushButton.setStyleSheet("background-color: Red; color: white;")

        self.pushButton.clicked.connect(self.start_execution) #連結按鈕點擊事件(按下去才開始執行)

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

        for row in grid:
            for value in row:
                label_name = f"label_{index}"
                label = getattr(self, label_name, None)
                if label is not None:
                    if value == -1:
                        label.setText("")
                        label.setStyleSheet("background-color: gray;")
                    elif value == 0:
                        label.setText("")
                        label.setStyleSheet("background-color: white;")
                    else:
                        label.setText(str(value))
                        label.setFont(QFont("Arial", 14, QFont.Bold))
                        label.setStyleSheet("background-color: blue; color: white;")
                index += 1

        self.update_step_label(method_idx, step)

    def update_step_label(self, method_idx, step):
        method_map = {
            0: "障礙物觀點",
            1: "空格觀點",
            2: "動態規劃",
            3: "強化學習"
        }
        
        method_name = method_map.get(method_idx)
        labels = [self.obsLabel, self.spaLabel, self.bfsLabel, self.maacLabel]
        if 0 <= method_idx < len(labels):
            labels[method_idx].setText(f"{method_name}: 第 {step} 步")

    def set_method_label_red(self, method_idx):
        labels = [self.obsLabel, self.spaLabel, self.bfsLabel, self.maacLabel]
        if 0 <= method_idx < len(labels):
            labels[method_idx].setStyleSheet("background-color: pink; color: black;")

