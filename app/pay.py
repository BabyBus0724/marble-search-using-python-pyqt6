import boto3
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QPushButton


class PurchaseDialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AWS Purchase")
        self.setGeometry(300, 300, 300, 150)

        self.resource_type_label = QLabel("Resource Type:")
        self.resource_type_line_edit = QLineEdit()

        self.quantity_label = QLabel("Quantity:")
        self.quantity_line_edit = QLineEdit()

        self.purchase_button = QPushButton("Purchase")
        self.purchase_button.clicked.connect(self.purchase)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.resource_type_label)
        self.layout.addWidget(self.resource_type_line_edit)
        self.layout.addWidget(self.quantity_label)
        self.layout.addWidget(self.quantity_line_edit)
        self.layout.addWidget(self.purchase_button)

        self.setLayout(self.layout)

    def purchase(self):
        resource_type = self.resource_type_line_edit.text()
        quantity = self.quantity_line_edit.text()

        client = boto3.client("ec2")
        response = client.purchase_reserved_instances(
            ReservationType="standard",
            InstanceCount=quantity,
            InstanceType="t2.micro",
            AvailabilityZone="us-east-1a",
        )

        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            self.show_message("Purchase successful!")
        else:
            self.show_message("Purchase failed!")

    def show_message(self, message):
        QMessageBox.information(self, "Purchase", message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PurchaseDialog()
    window.show()
    sys.exit(app.exec())
