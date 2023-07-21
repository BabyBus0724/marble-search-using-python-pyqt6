import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QPushButton
from PyQt6.QtSql import QSqlDatabase, QSqlQuery


class PaymentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Payment")
        self.setGeometry(300, 300, 300, 150)

        self.amount_line_edit = QLineEdit()
        self.card_number_line_edit = QLineEdit()
        self.expiration_date_line_edit = QLineEdit()
        self.cvv_line_edit = QLineEdit()

        self.pay_button = QPushButton("Pay")
        self.pay_button.clicked.connect(self.pay)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.amount_line_edit)
        self.layout.addWidget(self.card_number_line_edit)
        self.layout.addWidget(self.expiration_date_line_edit)
        self.layout.addWidget(self.cvv_line_edit)
        self.layout.addWidget(self.pay_button)

        self.setLayout(self.layout)

    def pay(self):
        amount = self.amount_line_edit.text()
        card_number = self.card_number_line_edit.text()
        expiration_date = self.expiration_date_line_edit.text()
        cvv = self.cvv_line_edit.text()

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database.sqlite")
        db.open()

        query = QSqlQuery()
        query.exec_("INSERT INTO payments (amount, card_number, expiration_date, cvv) VALUES ('{}', '{}', '{}', '{}')".format(amount, card_number, expiration_date, cvv))

        if query.lastError().isValid():
            self.show_message("Payment failed!")
        else:
            self.show_message("Payment successful!")

        db.close()

    def show_message(self, message):
        QMessageBox.information(self, "Payment", message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PaymentWindow()
    window.show()
    sys.exit(app.exec())
