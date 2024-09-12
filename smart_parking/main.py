#import sys
#from PySide6 import QtWidgets
#from widget import Widget

#if __name__ == '__main__':
#    app = QtWidgets.QApplication(sys.argv)
#    window = Widget()
#    window.show()
#    sys.exit(app.exec_())
    

import sys
from grid import GridWindow, CarLabel
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QVBoxLayout
from PySide6.QtCore import Qt, QPoint, qDebug
from PySide6.QtGui import QMouseEvent

# class CarLabel(QLabel):
#     def __init__(self, car_id, parent=None):
#         super().__init__(parent)
#         self.car_id = car_id
#         self.setText(f"Car {car_id}")
#         self.setStyleSheet(f"background-color: {'red' if car_id == 1 else 'blue'}; color: white;")
#         self.setAlignment(Qt.AlignCenter)
#         self.setFixedSize(100, 100)
#         self.drag_start_position = QPoint()  # Initialize drag_start_position

class CarLabelMouseEvents:
    @staticmethod
    def mousePressEvent(label: CarLabel, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            label.drag_start_position = event.pos()

    @staticmethod
    def mouseMoveEvent(label: CarLabel, event: QMouseEvent):
        if event.buttons() == Qt.LeftButton:
            current_pos = event.pos()
            dx = current_pos.x() - label.drag_start_position.x()
            dy = current_pos.y() - label.drag_start_position.y()
            
            if abs(dx) > abs(dy):
                # 水平移動
                new_pos = QPoint(current_pos.x(), label.drag_start_position.y())
            else:
                # 垂直移動
                new_pos = QPoint(label.drag_start_position.x(), current_pos.y())
            
            distance = (new_pos - label.drag_start_position).manhattanLength()
            if distance >= QApplication.startDragDistance():
                label.setStyleSheet("background-color: grey; color: white;")
                label.setText("Moving")
                
                # 更新拖動起始位置，以實現連續移動
                label.drag_start_position = new_pos

    @staticmethod
    def mouseReleaseEvent(label: CarLabel, event: QMouseEvent):
        # label.setStyleSheet(f"background-color: {'red' if label.car_id == 1 else 'blue'}; color: white;")
        label.setStyleSheet(f"background-color: blue;")

        label.setText(f"Car {label.car_id}")

# class GridWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Car Grid - Drag and Drop")
#         self.grid_layout = QGridLayout()

#         self.cars = {}  # 用來追蹤車子的位置
#         self.init_ui()

#     def init_ui(self):
#         # moving grid
#         for row in range(3):
#             for col in range(3):
#                 empty_label = QLabel()
#                 empty_label.setStyleSheet("background-color: lightgray;")
#                 empty_label.setFixedSize(100, 100)
#                 self.grid_layout.addWidget(empty_label, row, col)

#         # add car to the moving grid
#         self.add_car(0, 0, 1)
#         self.add_car(0, 1, 2)
#         self.add_car(1, 1, 3)
#         self.add_car(2, 2, 4)

#         self.setLayout(self.grid_layout)

#     def add_car(self, row, col, car_id):
#         car_label = CarLabel(car_id)
#         self.grid_layout.addWidget(car_label, row, col)
#         self.cars[car_id] = (row, col)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GridWindow()
    window.show()
    sys.exit(app.exec())
