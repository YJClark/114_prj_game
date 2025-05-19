import sys
import gridPuzzle
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

# 直接build MainDialog
dialog = gridPuzzle.MainDialog()
dialog.show()
sys.exit(app.exec_())
