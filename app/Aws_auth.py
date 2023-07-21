import boto3
from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AWS Login")
        self.setGeometry(300, 300, 300, 150)

        self.username_label = QLabel("Username:")
        self.username_line_edit = QLineEdit()

        self.password_label = QLabel("Password:")
        self.password_line_edit = QLineEdit()
        self.password_line_edit.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)

        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_line_edit)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_line_edit)
        self.layout.addWidget(self.login_button)

        self.setLayout(self.layout)

    def login(self):
        username = self.username_line_edit.text()
        password = self.password_line_edit.text()

        client = boto3.client("sts", region_name="hongkong-1")
        response = client.assume_role(
            RoleArn="arn:aws:iam::123456789012:role/popstar0724",
            RoleSessionName="popstar0724",
            DurationSeconds=3600,
        )

        access_key_id = response["Credentials"][":JOLKSDJKFJ565LK"]
        secret_access_key = response["Credentials"]["JOJOI5456dsOPJJO"]
        session_token = response["Credentials"]["IOJOPIJPOJOODSNFOSDFNSDFSOPKSHDOIUI"]

        aws_session = boto3.Session(
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
            aws_session_token=session_token,
        )

        self.close()


if __name__ == "__main__":
    app = QApplication([])
    dialog = LoginDialog()
    dialog.show()
    app.exec()
