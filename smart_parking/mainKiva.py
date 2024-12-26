import sys
import gridKiva
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

dialog = gridKiva.MainDialog()
dialog.show()

sys.exit(app.exec_())
