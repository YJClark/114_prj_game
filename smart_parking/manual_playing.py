from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton

class ManualPlaying:
    def __init__(self, ui):
        self.ui = ui
        self.selected_button = None #追蹤目前選擇的button
    
    def button_clicked(self, button: QPushButton): 
        if self.selected_button == button:  # 如果是同一個按鈕，則取消選擇
            print(f"Cancel clicked button {button.text()}!")
            self.selected_button = None
            self.update_label_text("nothing!")
        else:  # 如果是新的按鈕，則選擇該按鈕
            print(f"Button {button.text()} is clicked!")
            self.selected_button = button
            self.update_label_text(button.text())
                                    
    def update_label_text(self, text: str):
        self.ui.statusLabel.setText("")
        self.ui.statusLabel.setText(f"You choose {text}")
        self.ui.statusLabel.setFont(QFont("Arial", 14, QFont.Bold))
        print("xx"+text)

