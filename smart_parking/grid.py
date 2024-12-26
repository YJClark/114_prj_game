import mainUI
import methodsUI
# from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
from PyQt5.QtGui import QFont
from manual_playing import ManualPlaying
import numpy as np

class Ui_MainWindow(mainUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.ManualPlaying = ManualPlaying(self)
        self.statusLabel = None
        
        # 初始 start 和 stop
        self.start = np.array([])  
        self.stop = np.array([])

        # 從檔案讀取資料
        self.start = self.read_file("./data_graphform/3x3/tar3/start/graph_start_3x3_tar3_sp4_0.txt")
        self.stop = self.read_file("./data_graphform/3x3/tar3/end/graph_end_3x3_tar3_sp4_0.txt")

        # 連接按鈕到切換 methodsUI 的方法
        # self.tomethodsbtn.clicked.connect(self.open_methods_ui)     

    def read_file(self, filename):
        data = []
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                for line in lines[1:]:  # 忽略第一行
                    row = [int(x) for x in line.strip().split(",")]
                    data.append(row)
        except Exception as e:
            print(f"Error reading file {filename}: {e}")
        return np.array(data)  # 將列表轉為 numpy 陣列

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.manual_game()
        self.manual_Answer()
        self.countLabel.setFont(QFont("Arial", 14, QFont.Bold))
        self.egLabel.setFont(QFont("Arial", 14, QFont.Bold))
        self.egLabel.setStyleSheet("background-color: Gray; color: white;")
        self.ansLabel.setFont(QFont("Arial", 12, QFont.Bold))
        self.ansLabel.setStyleSheet("background-color: Green; color: white;")
        self.manualLabel.setFont(QFont("Arial", 16, QFont.Bold))
        self.manualLabel.setStyleSheet("background-color: Yellow; color: black;")
        
        # 連接按鈕到切換 methodsUI 的方法(但我不知道為何要放在這裡)
        # self.tomethodsbtn.clicked.connect(self.open_methods_ui)     

    def manual_Answer(self):
        index = 1
        for row in range(self.stop.shape[0]):
            for col in range(self.stop.shape[1]):
                label_name = f"label_{index}"  # 取得 label 名字
                label = getattr(self, label_name, None)
                if label is not None:
                    if self.stop[row, col] == -1:
                        label.setText("")
                        label.setStyleSheet("background-color: gray;")
                    elif self.stop[row, col] == 0:
                        label.setText("")
                        label.setStyleSheet("background-color: white;")
                    else:
                        label.setText("Car" + str(self.stop[row, col]))
                        label.setFont(QFont("Arial", 16, QFont.Bold))
                        label.setStyleSheet("background-color: blue; color: white;")
                index += 1

    def manual_game(self):
        index = 1
        for row in range(self.start.shape[0]):
            for col in range(self.start.shape[1]):
                button_name = f"pushButton_{index}"  # 取得 button 名字
                button = getattr(self, button_name, None)
                if button is not None:
                    if self.start[row, col] == -1:
                        button.setText(" ")
                        button.setFont(QFont("Arial", 16, QFont.Bold))
                        button.setStyleSheet("background-color: gray;")
                    elif self.start[row, col] == 0:
                        button.setText("")
                        button.setFont(QFont("Arial", 16, QFont.Bold))
                        button.setStyleSheet("background-color: white;")
                    else:
                        button.setText("Car" + str(self.start[row, col]))
                        button.setFont(QFont("Arial", 16, QFont.Bold))
                        button.setStyleSheet("background-color: blue; color: white;")

                    button.clicked.connect(
                        lambda _, b=button, r=row, c=col: self.ManualPlaying.button_clicked(b, r, c, self.start, self.stop)
                    )
                index += 1

#     def open_methods_ui(self):
#         """打開 methodsUI 並關閉自己"""
#         self.methods_window = MethodsWindow()
#         self.methods_window.show()
#         self.close()


# #methodsUI
# class MethodsWindow(QDialog, methodsUI.Ui_Dialog):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         print("MethodsWindow has been called.")

#         # 連接按鈕到切換 mainUI 的方法
#         self.back_to_manual.clicked.connect(self.open_main_ui)

#     def open_main_ui(self):
#         self.main_window = Ui_MainWindow()
#         self.main_window.show()
#         self.close()


# # #測試終止條件的
# #         self.start = [
# #             [4, 1, -1],
# #             [-1, -1, 0],
# #             [3, -1, 2]
# #         ]

# #         self.stop = [
# #             [4, 1, -1],
# #             [-1, -1, 2],
# #             [3, -1, 0]
# #         ]