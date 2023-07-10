import time

from PyQt6 import uic,QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from .ui.home_ui import Ui_LandingWindow
# from .ui.result_ui import Ui_ResultWindow

from .result import ResultWindow

from .ui import resources_rc

# class ResultWindow(QMainWindow, Ui_ResultWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
        

class MainWindow(QMainWindow, Ui_LandingWindow):
    def __init__(self, app, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.w = ResultWindow()
        QFontDatabase.addApplicationFont("ui/assets/fonts/Century Gothic.ttf")

        self.app = app
        self.func_login.clicked.connect(self.gotoResult)
        self.go_signin_2.clicked.connect(self.gotoLogin)
        self.go_signin.clicked.connect(self.gotoLogin)
        self.go_signup.clicked.connect(self.gotoRegister)

    # def button_press(self):
    #     text = self.operation()
    #     QMessageBox.information(self, "Message Box", text)

    def gotoResult(self):
        self.w.show();
        self.hide()

    def gotoLogin(self):
        self.stackedWidget.setCurrentIndex(0)

    def gotoRegister(self):
        self.stackedWidget.setCurrentIndex(1)


    # @long_operation("Calculation")
    # def operation(self):
    #     return self.app.calculation(3)


