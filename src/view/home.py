# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\view\home.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_person = QtWidgets.QTableView(self.centralwidget)
        self.table_person.setMinimumSize(QtCore.QSize(400, 300))
        self.table_person.setObjectName("table_person")
        self.verticalLayout.addWidget(self.table_person)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)
        self.edit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_name.setObjectName("edit_name")
        self.gridLayout.addWidget(self.edit_name, 0, 1, 1, 1)
        self.label_class = QtWidgets.QLabel(self.centralwidget)
        self.label_class.setObjectName("label_class")
        self.gridLayout.addWidget(self.label_class, 1, 0, 1, 1)
        self.edit_class = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_class.setObjectName("edit_class")
        self.gridLayout.addWidget(self.edit_class, 1, 1, 1, 1)
        self.label_score = QtWidgets.QLabel(self.centralwidget)
        self.label_score.setObjectName("label_score")
        self.gridLayout.addWidget(self.label_score, 2, 0, 1, 1)
        self.edit_score = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_score.setObjectName("edit_score")
        self.gridLayout.addWidget(self.edit_score, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.button_clear = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear.setObjectName("button_clear")
        self.horizontalLayout.addWidget(self.button_clear)
        self.button_load = QtWidgets.QPushButton(self.centralwidget)
        self.button_load.setObjectName("button_load")
        self.horizontalLayout.addWidget(self.button_load)
        self.button_save = QtWidgets.QPushButton(self.centralwidget)
        self.button_save.setObjectName("button_save")
        self.horizontalLayout.addWidget(self.button_save)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_name.setText(_translate("MainWindow", "Name"))
        self.label_class.setText(_translate("MainWindow", "Class"))
        self.label_score.setText(_translate("MainWindow", "Score"))
        self.button_clear.setText(_translate("MainWindow", "Clear"))
        self.button_load.setText(_translate("MainWindow", "Load"))
        self.button_save.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())