from PyQt5 import QtWidgets
from .controller.home import controllerHome
import sys


app = QtWidgets.QApplication(sys.argv)
ui = controllerHome()
ui.show()
sys.exit(app.exec_())