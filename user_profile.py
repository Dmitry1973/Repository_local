import sys, os.path
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QFont, QPixmap

class UserProfile(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """

        self.setGeometry(600, 400, 300, 450)
        self.setWindowTitle("2.1 - User Profile GUI")
        self.displayImages()
        self.displayUserInfo()
        self.show()

    def displayImages(self):
        """
        Display background and profile images.
        Check to see if image files exist, if not throe as exception
        """

        background_image = r"D:\Repository_local\Qt_trial\images/skyblue.png"
        profile_image= r"D:\Repository_local\Qt_trial\images/profile_image.png"

        try:
            with open(background_image):
                background = QLabel(self)
                pixmap = QPixmap(background_image)
                background.setPixmap(pixmap)
        except FileNotFoundError:
            print("Image not found")

        try:
            with open(profile_image):
                user_image = QLabel(self)
                pixmap = QPixmap(profile_image)
                user_image.setPixmap(pixmap)
                user_image.move(80,10)
        except FileNotFoundError:
            print("Image not found")

    def displayUserInfo(self):
        """
        Create the labels to be displayed for the User Profile
        """

        user_name = QLabel(self)
        user_name.setText("John Doe")
        user_name.move(85, 160)
        user_name.setFont((QFont('Arial', 20)))

        bio_title = QLabel(self)
        bio_title.setText("Biography")
        bio_title.move(15, 190)
        bio_title.setFont(QFont('Areal', 15))

        about = QLabel(self)
        about.setText("I'm Engineer with 20+ years\
                        experience creating code")
        about.setWordWrap(True)
        about.move(15, 220)

        skills_title = QLabel(self)
        skills_title.setText("Skills")
        skills_title.move(15, 260)
        skills_title.setFont(QFont('Arial', 15))

        skills = QLabel(self)
        skills.setText("Python | PHP | SQL | JavaScript")
        skills.move(15,285)

        experience_title = QLabel(self)
        experience_title.setText("Experience")
        experience_title.move(15, 315)
        experience_title.setFont(QFont('Arial', 15))

        experience = QLabel(self)
        experience.setText("Completion Engineer")
        experience.move(15, 345)

        dates = QLabel(self)
        dates.setText("May 2008 - Nov 2019")
        dates.move(15, 365)
        dates.setFont(QFont('Arial', 10))

        experience = QLabel(self)
        experience.setText("Geophysicist")
        experience.move(15, 385)

        dates = QLabel(self)
        dates.setText("Oct 2000 - May 2008")
        dates.move(15, 405)
        dates.setFont(QFont('Arial', 10))

# Run Program

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserProfile()
    sys.exit(app.exec_())