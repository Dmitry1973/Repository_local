import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QMessageBox,
                             QLineEdit, QPushButton, QCheckBox)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from Qt_trial.Registration import CreateNewUser  # Import Registration module


class LoginUI(QWidget):

    def __init__(self):  # Constructor
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(600, 300, 400, 230)
        self.setWindowTitle('3.1 - Login GUI')
        self.loginUserInterface()

        self.show()

    def loginUserInterface(self):
        """
        Create the login GUI
        """

        login_label = QLabel(self)
        login_label.setText('Login')
        login_label.move(180, 10)
        login_label.setFont(QFont('Arial', 20))

        # Username and password labels and line edit widgets
        name_label = QLabel('username:', self)
        name_label.move(30, 60)

        self.name_entry = QLineEdit(self)
        self.name_entry.move(110, 60)
        self.name_entry.resize(220, 20)

        password_label = QLabel('password:', self)
        password_label.move(30, 90)

        self.password_entry = QLineEdit(self)
        self.password_entry.move(110, 90)
        self.password_entry.resize(220, 20)

        # Sign in push button
        sign_in_button = QPushButton('Login', self)
        sign_in_button.move(100, 140)
        sign_in_button.resize(200, 40)
        sign_in_button.clicked.connect(self.clickLogin)

        # Display show password checkbox
        show_pswd_cb = QCheckBox('show password', self)
        show_pswd_cb.move(110, 115)
        show_pswd_cb.stateChanged.connect(self.showPassword)
        show_pswd_cb.toggle()
        show_pswd_cb.setChecked(False)

        # Display sign up label and push button
        not_a_member = QLabel('not a memmber?', self)
        not_a_member.move(50, 200)

        sign_up = QPushButton('sign up', self)
        sign_up.move(160, 195)
        sign_up.clicked.connect(self.createNewUser)

    def clickLogin(self):
        """
        When user clicks on sign in button, check if username and
        password match any existing profiles in users.txt
        If they exist, display messagebox and close program.
        If they don't, display error messagebox
        """

        users = {}  # Create empty dictionary to store user information
        # Check if users.txt exists, otherwise create new file
        try:
            with open(r"D:\Repository_local\Qt_trial\images\users.txt", 'r') as f:
                for line in f:
                    user_fields = line.split(' ')
                    username = user_fields[0]
                    password = user_fields[1].strip('\n')
                    users[username] = password
        except FileNotFoundError:
            print('The file does not exist. Creating a new file')
            f = open(r"D:\Repository_local\Qt_trial\images\users.txt", 'w')

        username = self.name_entry.text()
        password = self.password_entry.text()
        if (username, password) in users.items():
            QMessageBox.information(self, "Login Successful!",
                                    "Login Successful!", QMessageBox.Ok, QMessageBox.Ok)
            self.close()  # close program
        else:
            QMessageBox.warning(self, "Error Message",
                                "The username or password is incorrect.",
                                QMessageBox.Close, QMessageBox.Close)

    def showPassword(self, state):
        """
        If checkbox is enabled, view password.
        Else, msk password so others cannot see it
        """
        if state == Qt.Checked:
            self.password_entry.setEchoMode(QLineEdit.Normal)
        else:
            self.password_entry.setEchoMode(QLineEdit.Password)

    def createNewUser(self):
        """
        If the sign up button is clicked, open
        a new window and allow the user to create a new account
        """
        self.create_new_user_dialog = CreateNewUser()
        self.create_new_user_dialog.show()

    def closeEvent(self, event):
        """Display a QMessageBoz when asking the user
        if they want to quit the program.
        """
        # Set up message box
        quit_msg = QMessageBox.question(self, "Quit Application?",
                                        "Are you sure you want to Quit?",
                                        QMessageBox.No | QMessageBox.Yes,
                                        QMessageBox.Yes)
        if quit_msg == QMessageBox.Yes:
            event.accept()  # accept the event and close the application
        else:
            event.ignore()  # ignore the close event


# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginUI()
    sys.exit(app.exec_())