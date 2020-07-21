import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox,
                             QPushButton, QLabel, QLineEdit)
from PyQt5.QtGui import QFont, QPixmap

class CreateNewUser(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initializeUI() # call function to set up window
    
    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(650, 350, 400, 500)
        self.setWindowTitle('3.2 - Create New User')
        self.displayWidgetsToCollectInfo()
        self.show()
        
    def displayWidgetsToCollectInfo(self):
        """
        Create widgets that will be used to collect information from
        the user to create a new user
        """
        # Crete label for image
        # new_user_image = "images/new_user_icon.png"
        new_user_image = r"D:\Repository_local\Qt_trial\images/profile_image.png"
        try:
            with open(new_user_image):
                new_user = QLabel(self)
                pixmap = QPixmap(new_user_image)
                new_user.setPixmap(pixmap)
                new_user.move(130, 80)
        except FileNotFoundError:
            print('Image not found')
            
        login_label = QLabel(self)
        login_label.setText('create new account')
        login_label.move(60, 20)
        login_label.setFont(QFont('Arial', 20))
        # Username and fullname labels and line edit widgets
        name_label = QLabel('username: ', self)
        name_label.move(50, 280)

        self.name_entry = QLineEdit(self)
        self.name_entry.move(130, 280)
        self.name_entry.resize(200, 20)

        name_label = QLabel('full name: ', self)
        name_label.move(50, 310)

        name_entry = QLineEdit(self)
        name_entry.move(130, 310)
        name_entry.resize(200, 20)

        # Create password and confirm password labels and line edit widgets

        pswd_label = QLabel('password: ', self)
        pswd_label.move(50, 340)

        self.pswd_entry = QLineEdit(self)
        self.pswd_entry.setEchoMode(QLineEdit.Password)
        self.pswd_entry.move(130, 340)
        self.pswd_entry.resize(200, 20)

        confirm_label = QLabel('confirm: ', self)
        confirm_label.move(50, 370)

        self.confirm_entry = QLineEdit(self)
        self.confirm_entry.setEchoMode(QLineEdit.Password)
        self.confirm_entry.move(130, 370)
        self.confirm_entry.resize(200, 20)

        # Create sign in button
        sign_in_button = QPushButton('sign up', self)
        sign_in_button.move(100, 420)
        sign_in_button.resize(200, 40)
        sign_in_button.clicked.connect(self.confirmSignUp)

    def confirmSignUp(self):
        """
        When user presses sign up, check if the passwords match.
        If they match. then save username text to users.txt
        """

        pswd_text = self.pswd_entry.text()
        confirm_text = self.confirm_entry.text()

        if pswd_text != confirm_text:
            #Display ma=essagebox if passwords don't match
            QMessageBox.warning(self, "Error Message",
                                "The passwords you entered doo not match. Pleas try again.",
                                QMessageBox.Close)
        else:
            # if passwords match, save passwords to file and return to login
            # and test if you can log in with new user information.
            with open(r"D:\Repository_local\Qt_trial\images\users.txt", 'a+') as f:
                f.write(self.name_entry.text() + " ")
                f.write(pswd_text + "\n")
            self.close()

# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CreateNewUser()
    sys.exit(app.exec_())