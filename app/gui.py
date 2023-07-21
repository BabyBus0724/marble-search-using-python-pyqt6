import time

from PyQt6 import uic,QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sqlite3

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
        # QFontDatabase.addApplicationFont("ui/assets/fonts/Century Gothic.TTF")

        self.app = app
        self.func_login.clicked.connect(self.gotoResult)
        self.func_signUp.clicked.connect(self.register_func)
        self.go_signin_2.clicked.connect(self.gotoLogin)
        self.go_signin.clicked.connect(self.gotoLogin)
        self.go_signup.clicked.connect(self.gotoRegister)

    # def button_press(self):
    #     text = self.operation()
    #     QMessageBox.information(self, "Message Box", text)
        
    def register_func(self):
        firstName = self.firstname_field.text()
        lastName = self.lastname_field.text()
        email = self.email_2_field.text()
        password1 = self.password1_field.text()
        password2 = self.password2_field.text()
        mobileNum = self.mobile_num_field.text()

        conn = sqlite3.connect("marble.db")
        
        # Execute a SELECT query to check if the username and password are correct
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (firstName, lastName, email, mobileNum, password1))

        # Commit the changes to the database
        conn.commit()
        
        # Close the database connection
        conn.close()
        
        # Show a success message using a QMessageBox
        QMessageBox.information(self, "Success", "Signup successful!")

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


