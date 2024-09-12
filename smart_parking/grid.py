from PySide6.QtWidgets import QLabel, QGridLayout, QWidget
from PySide6.QtCore import Qt, QPoint, qDebug

class CarLabel(QLabel):
    def __init__(self, car_id, parent=None):
        super().__init__(parent)
        self.car_id = car_id
        self.setText(f"Car {car_id}")
        # self.setStyleSheet(f"background-color: {'red' if car_id == 1 else 'blue'}; color: white;")
        self.setStyleSheet(f"background-color: {'white' if car_id == 0 else 'blue'}; color: white;")
        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(100, 100)
        self.drag_start_position = QPoint()  # Initialize drag_start_position


class GridWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Car Grid - Drag and Drop")
        self.grid_layout = QGridLayout()

        self.cars = {}  # 用來追蹤車子的位置
        self.init_ui()

    def init_ui(self):
        # moving grid
        for row in range(3):
            for col in range(3):
                empty_label = QLabel()
                empty_label.setStyleSheet("background-color: gray;")
                empty_label.setFixedSize(100, 100)
                self.grid_layout.addWidget(empty_label, row, col)

        # add car to the moving grid
        start = [
            [2, 3, -1],
            [-1, -1, 0],
            [4, -1, 1]
        ]
        for row in range(len(start)):
            for col in range(len(start[row])):
                car_id = start[row][col]
                if car_id != -1 and car_id != 0:  # Only add cars if the value is not -1 (obstacle) and 0 (space)
                    self.add_car(row, col, car_id)
                if car_id == 0:
                    empty_label.setStyleSheet("background-color: lightgray;")


        self.setLayout(self.grid_layout)

    def add_car(self, row, col, car_id):
        car_label = CarLabel(car_id)
        self.grid_layout.addWidget(car_label, row, col)
        self.cars[car_id] = (row, col)
