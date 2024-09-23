# from PyQt5.QtGui import QFont
# from PyQt5.QtWidgets import QPushButton

# class ManualPlaying:
#     def __init__(self, ui):
#         self.ui = ui
#         self.selected_button = None #追蹤目前選擇的button
    
#     def button_clicked(self, button: QPushButton): 
#         if self.selected_button == button:  # 如果是同一個按鈕，則取消選擇
#             print(f"Cancel clicked button {button.text()}!")
#             self.selected_button = None
#             self.update_label_text("nothing!")
#         else:  # 如果是新的按鈕，則選擇該按鈕
#             print(f"Button {button.text()} is clicked!")
#             self.selected_button = button
#             if button.text()== " ":     # 障礙物
#                 print(f"You choose obstacle!")
#                 self.update_label_text("obstacle")
#             elif button.text()=="":     # space
#                 print(f"You choose space!")
#                 self.update_label_text("nothing!")
#             else:
#                 print(f"You choose {button.text()}!")
#                 self.update_label_text(button.text())
                                    
#     def update_label_text(self, text: str):
#         self.ui.statusLabel.setText("")
#         self.ui.statusLabel.setText(f"You choose {text}")
#         self.ui.statusLabel.setFont(QFont("Arial", 14, QFont.Bold))

# #這裡要做數字交換
#     def swapping():
#         pass

# #檢查結束沒
#     def check_finish():
#         pass

# #數總共換了幾次
#     def countSwapping():
#         pass
        
# #空白周圍的格子會閃爍
#     def hint():
#         pass
 


from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton

class ManualPlaying:
    def __init__(self, ui):
        self.ui = ui
        self.selected_button = None
        self.selected_position = None
    
    def button_clicked(self, button: QPushButton, row: int, col: int, grid):
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

                # 更新UI，不重新生成按鈕，直接修改按鈕樣式
                self.update_button(button, car_row, car_col, grid)
                
                # 清空選擇
                self.selected_button = None
                self.selected_position = None
                self.update_label_text("You choose nothing!")
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
