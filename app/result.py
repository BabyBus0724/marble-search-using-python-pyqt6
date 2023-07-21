import time

from PyQt6 import uic,QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

# from .ui.home_ui import Ui_LandingWindow
from .ui.result_ui import Ui_ResultWindow

class ResultWindow(QMainWindow, Ui_ResultWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #     self.go_back.clicked.connect(self.backLogin)

    # def  backLogin(self):
    #     self.w.show()
    #     self.close