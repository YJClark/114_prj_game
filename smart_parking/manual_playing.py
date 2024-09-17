from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton

class ManualPlaying:
    def __init__(self, ui):
        self.ui = ui
        self.selected_button = None #追蹤目前選擇的button
     
    def button_clicked(self, button: QPushButton):
        if button:
            print(f"Button {button.text()} is clicked!")
            self.selected_button = button
        else:
            print("No button is clicked!")

        
        if self.selected_button is button:
            # print(self.selected_button)
            # 取消選取
            self.selected_button = None
            self.update_label_text("")
        
        else:
            # 已經有選取的button
            if self.selected_button:
                self.update_label_text("")
            # 設定新的button為選取狀態
            self.selected_button = button
            self.update_selected_label(button.text())
            print(button.text())
                                    
    def update_label_text(self, text: str):
        self.ui.statusLabel.setText(f"You choose {text}")
        self.ui.statusLabel.setFont(QFont("Arial", 14, QFont.Bold))
        # print("notcrashed")
        print("xx"+text)

