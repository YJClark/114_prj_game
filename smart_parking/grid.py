import mainUI
from PyQt5.QtGui import QFont
from manual_playing import ManualPlaying

class Ui_MainWindow(mainUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ManualPlaying = ManualPlaying(self)
        self.statusLabel = None
        #之後改讀檔
        self.start = [
            [2, 3, -1],
            [-1, -1, 0],
            [4, -1, 1]
        ]

        self.stop = [
            [4, 1, -1],
            [-1, -1, 2],
            [3, -1, 0]
        ]
        
    def load_data():
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.manual_game()
        self.manual_Answer()

    def manual_Answer(self):
        #美化answer label
        self.ansLabel.setStyleSheet("background-color: Green; color: white;")
        self.ansLabel.setFont(QFont("Arial", 12, QFont.Bold))

        # stop = [
        #     [4, 1, -1],
        #     [-1, -1, 2],
        #     [3, -1, 0]
        # ]
        
        index = 1
        for row in range(len(self.stop)):
            for col in range(len(self.stop[row])):
                label_name = f"label_{index}"       # 取得label名字
                label = getattr(self, label_name, None) 
                if label is not None:        
                    if self.stop[row][col] == -1:
                        label.setText("")
                        label.setStyleSheet("background-color: gray;")
                    elif self.stop[row][col] == 0:
                        label.setText("")
                        label.setStyleSheet("background-color: white;")
                    else:
                        label.setText("Car" + str(self.stop[row][col]))
                        label.setFont(QFont("Arial", 16, QFont.Bold))
                        label.setStyleSheet("background-color: blue; color: white;")
                index += 1

    def manual_game(self):
        index = 1
        for row in range(len(self.start)):
            for col in range(len(self.start[row])):
                button_name = f"pushButton_{index}"     # 取得button名字
                button = getattr(self, button_name, None)
                if button is not None: 
                    if self.start[row][col] == -1:
                        button.setText(" ")
                        button.setStyleSheet("background-color: gray;")
                    elif self.start[row][col] == 0:
                        button.setText("")
                        button.setStyleSheet("background-color: white;")
                    else:
                        button.setText("Car" + str(self.start[row][col]))
                        button.setFont(QFont("Arial", 16, QFont.Bold))
                        button.setStyleSheet("background-color: blue; color: white;")

                    #button.clicked.connect(partial(self.ManualPlaying.button_clicked, button)) 
                    # print(f"Connecting to button: {button.text()}")
                    button.clicked.connect(lambda _, b=button, r=row, c=col: self.ManualPlaying.button_clicked(b, r, c, self.start))
                index += 1
