from PyQt5 import QtWidgets, QtGui, QtCore
from ..view.home import Ui_MainWindow
from ..model.table_model import TableModel
from ..database import create_connection, create_person, delete_person, read_person


class controllerHome(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(controllerHome, self).__init__()
        self.setupUi(self)
        self.load_data()
        self.init_table()

        self.button_save.clicked.connect(self.save_data)
        self.button_load.clicked.connect(self.load_data)
        self.button_clear.clicked.connect(self.clear_data)

    def init_table(self):
        self.table_person.setModel(TableModel(self.data_table))

    def load_data(self):
        conn = create_connection('database.db')
        self.data_table = read_person(conn)
        self.init_table()

    def clear_data(self):
        conn = create_connection('database.db')
        delete_person(conn)
        self.load_data()

    def save_data(self):
        conn = create_connection('database.db')
        create_person(conn, {"name": self.edit_name.text(),
                             "class": self.edit_class.text(),
                             "score": self.edit_score.text()})
        self.load_data()
