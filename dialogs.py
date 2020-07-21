import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QMessageBox, QLineEdit, QPushButton)
from PyQt5.QtGui import QFont


class DisplayMessageBox(QWidget):

    def __init__(self):
        super().__init__()
        self.auth_entry = QLineEdit(self)
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(400, 400, 800, 600)
        self.setWindowTitle('QMessageBox Example')
        self.displayWidgets()

        self.show()

    def displayWidgets(self):

        catalogue_label = QLabel("Author Catalogue", self)
        catalogue_label.move(20, 20)
        catalogue_label.setFont(QFont('Arial', 20))

        auth_label = QLabel("Enter the name of the author you are searching for:", self)
        auth_label.move(40, 60)

        author_name = QLabel("Name:", self)
        author_name.move(50, 90)

        self.auth_entry.move(95, 90)
        self.auth_entry.resize(240, 20)
        self.auth_entry.setPlaceholderText("firstname lastname")

        search_button = QPushButton("Search", self)
        search_button.move(125, 130)
        search_button.resize(150, 40)
        search_button.clicked.connect(self.displayMessageBox)

    def displayMessageBox(self):
        """
        When button is clicked, search through catalogue of names.
        If name is found, display Author Found dialog.
        Otherwise, display Author Not Found dialog
        """
        # Check if authors.txt exists

        try:
            with open(r"D:\Repository_local\Qt_trial\images/authors.txt", "r") as f:
                # read each line into a list
                authors = [line.rstrip('\n') for line in f]
        except FileNotFoundError:
            print("The file cannot be found")

        # Check for name in list
        not_found_msg = QMessageBox()  # create not_found_msg object to avoid causing a
        # 'referenced before assignment' error
        if self.auth_entry.text() in authors:
            QMessageBox().information(self, "Author Found", "Author Found in catalogue!",
                                      QMessageBox.Ok, QMessageBox.Ok)
        else:
            not_found_msg = QMessageBox.question(self, "Author Not Found",
                                                 "Author not found in catalogue.\nDo you wish to continue",
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if not_found_msg == QMessageBox.No:
            print("Closing application")
        else:
            pass


# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DisplayMessageBox()
    sys.exit(app.exec_())
