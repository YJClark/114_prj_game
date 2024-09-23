import mainUI
from PyQt5.QtGui import QFont
from manual_playing import ManualPlaying

from functools import partial


class Ui_MainWindow(mainUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # self.setupUi()
        self.ManualPlaying = ManualPlaying(self)
        self.statusLabel = None
        
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.manual_game()
        self.manual_Answer()

    def manual_Answer(self):
        #美化answer label
        self.ansLabel.setStyleSheet("background-color: Green; color: white;")
        self.ansLabel.setFont(QFont("Arial", 12, QFont.Bold))

        stop = [
            [4, 1, -1],
            [-1, -1, 2],
            [3, -1, 0]
        ]
        
        index = 1
        for row in range(len(stop)):
            for col in range(len(stop[row])):
                label_name = f"label_{index}"   #取得label名字
                # print(label_name)
                label = getattr(self, label_name, None) 
                if label is not None: 
                    # print("find label");        
                    if stop[row][col] == -1:
                        label.setText("")
                        label.setStyleSheet("background-color: gray;")
                    elif stop[row][col] == 0:
                        label.setText("")
                        label.setStyleSheet("background-color: white;")
                    else:
                        label.setText("Car" + str(stop[row][col]))
                        label.setFont(QFont("Arial", 16, QFont.Bold))
                        label.setStyleSheet("background-color: blue; color: white;")
                index += 1

    def manual_game(self):
        start = [
            [2, 3, -1],
            [-1, -1, 0],
            [4, -1, 1]
        ]

        index = 1
        for row in range(len(start)):
            for col in range(len(start[row])):
                button_name = f"pushButton_{index}"  # 取得button名字
                # print(button_name, index)
                button = getattr(self, button_name, None)
                if button is not None: 
                    if start[row][col] == -1:
                        button.setText(" ")
                        button.setStyleSheet("background-color: gray;")
                    elif start[row][col] == 0:
                        button.setText("")
                        button.setStyleSheet("background-color: white;")
                    else:
                        button.setText("Car" + str(start[row][col]))
                        button.setFont(QFont("Arial", 16, QFont.Bold))
                        button.setStyleSheet("background-color: blue; color: white;")

                    # button.clicked.connect(lambda _, b=button: self.ManualPlaying.button_clicked(b)) 
                    button.clicked.connect(partial(self.ManualPlaying.button_clicked, button)) 
                    print(f"Connecting to button: {button.text()}")
                index += 1

