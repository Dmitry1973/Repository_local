import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QCheckBox, QLabel)
from PyQt5.QtCore import Qt

class CheckBoxWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(400, 400 , 450, 250)
        self.setWindowTitle('QCheckBox Widget')
        self.displayCheckBoxes()

        self.show()

    def displayCheckBoxes(self):
        """
        Setup checkboxes and other widgets
        """
        header_label = QLabel(self)
        header_label.setText("Which shifts can you work? (Please check all that apply)")
        header_label.setWordWrap(True)
        header_label.move(10, 10)
        header_label.resize(230, 60)

        # Set up checkboxes

        morning_cb = QCheckBox("Morning [8 AM - 2 PM]", self)
        morning_cb.move(20, 80)
        # morning_cb.toggle() # uncomment if you want box to start off checked,
        # shown as an example here.
        morning_cb.stateChanged.connect(self.printToTerminal)
        after_cb = QCheckBox("Afternoon [1 PM - 8 PM]", self)
        after_cb.move(20, 100)
        after_cb.stateChanged.connect(self.printToTerminal)

        night_cb = QCheckBox("Night [7 PM - 3 AM]", self)
        night_cb.move(20, 120)
        night_cb.stateChanged.connect(self.printToTerminal)

    def printToTerminal(self, state):
        """
        Simple function to show how to determine the state of a checkbox.
        prints the text label of the checkbox by determining which widget
        is sending the signal
        """
        sender = self.sender()
        if state == Qt.Checked:
            print("{} Selected.".format(sender.text()))
        else:
            print("{} Deselected.".format(sender.text()))

# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CheckBoxWindow()
    sys.exit(app.exec_())