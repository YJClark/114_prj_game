import sys
import grid
import manual_playing
# import mainUI
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
basewidget = QtWidgets.QMainWindow()  

ui = grid.Ui_MainWindow()

ui.setupUi(basewidget)
ui.centralwidget.setStyleSheet("background-color: #9999CC;")

basewidget.show()
sys.exit(app.exec_())
