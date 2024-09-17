import sys
import grid
# import mainUI
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
basewidget = QtWidgets.QMainWindow()  

ui = grid.Ui_MainWindow()
# ui = mainUI.Ui_MainWindow()
ui.setupUi(basewidget)

ui.manual_Answer()
ui.manual_game()

basewidget.show()
sys.exit(app.exec_())
