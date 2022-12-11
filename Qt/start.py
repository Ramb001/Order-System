from PyQt5.QtWidgets import QApplication

from Qt.loginMenu import LoginWindow


def run():
    app = QApplication([""])
    login = LoginWindow()
    login.show()
    app.exec_()