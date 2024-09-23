import sys
import grid
# import mainUI
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
basewidget = QtWidgets.QMainWindow()  

ui = grid.Ui_MainWindow()
# ui = mainUI.Ui_MainWindow()
ui.setupUi(basewidget)

# ui.manual_Answer() #放到setUi()
# ui.manual_game() #拿掉因為會重複呼叫

basewidget.show()
sys.exit(app.exec_())
