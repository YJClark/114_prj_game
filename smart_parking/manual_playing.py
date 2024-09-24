from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton

class ManualPlaying:
    def __init__(self, ui):
        self.ui = ui
        self.selected_button = None
        self.selected_position = None
        self.count = 0
    
    def button_clicked(self, button: QPushButton, row: int, col: int, grid, stop):
        if grid[row][col] > 0 or grid[row][col] == -1:  # 如果是車輛 或 障礙物
            if self.selected_button == button:  # 再次點擊取消選擇
                self.selected_button = None
                self.selected_position = None
                self.update_label_text("You choose nothing!")
            else:
                self.selected_button = button
                self.selected_position = (row, col)
                self.update_label_text("You choose obstacle" if grid[row][col] == -1 else f"You choose {button.text()}")

        elif grid[row][col] == 0 and self.selected_button:  # 如果是空格且有選擇的車輛
            car_row, car_col = self.selected_position
            #檢查是否相鄰
            if self.is_adjacent(car_row, car_col, row, col):
                # 交換邏輯
                grid[row][col], grid[car_row][car_col] = grid[car_row][car_col], grid[row][col]
                self.swapCount()    #交換後+1

                # 更新UI，不重新生成按鈕，直接修改按鈕樣式
                self.update_button(button, car_row, car_col, grid)
                
                # 清空選擇
                self.selected_button = None
                self.selected_position = None
                self.update_label_text("You choose nothing!")

                #檢查結束沒
                self.check_finish(grid, stop)

            else:
                self.update_label_text("Invalid move!")

    def update_button(self, button: QPushButton, car_row: int, car_col: int, grid):
        # 更新當前空格按鈕
        button.setText(self.selected_button.text())
        button.setStyleSheet(self.selected_button.styleSheet())

        # 更新原來的車輛按鈕
        original_button = getattr(self.ui, f"pushButton_{car_row * len(grid[0]) + car_col + 1}")
        original_button.setText("")
        original_button.setStyleSheet("background-color: white;")

    #只能相鄰且不能斜著走
    def is_adjacent(self, car_row: int, car_col: int, row: int, col: int) -> bool: 
        return (abs(car_row - row) == 1 and car_col == col) or (abs(car_col - col) == 1 and car_row == row)

    def update_label_text(self, text: str):
        self.ui.statusLabel.setText("")
        self.ui.statusLabel.setText(text)
        self.ui.statusLabel.setFont(QFont("Arial", 14, QFont.Bold))

    #結束條件
    def check_finish(self, grid, stop):
        if all(
            grid[i][j] == stop[i][j] for i in range(len(grid)) for j in range(len(grid[i])) if stop[i][j] > 0
        ):
            self.update_label_text("You've finished the game")
            self.ui.statusLabel.setStyleSheet("background-color: Red; color: white;")
            
            # Disable all buttons to prevent further operations
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    button_name = f"pushButton_{i * len(grid[i]) + j + 1}"
                    button = getattr(self.ui, button_name, None)
                    if button:
                        button.setEnabled(False)

    #算swap幾次
    def swapCount(self):
        self.count += 1
        self.ui.countLabel.setText(f"Swap Counts: {self.count}")
        self.ui.countLabel.setFont(QFont("Arial", 10, QFont.Bold))

 #空白周圍的格子會閃爍
    def hint():
        pass

    def rewind():
        pass

    def reset():
        pass