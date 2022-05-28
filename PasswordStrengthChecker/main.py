import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import re
import pyautogui


class App(QWidget):

    def __init__(self):
        super().__init__()

        self.title = 'Password Strength Checker'
        self.w, self.h = pyautogui.size()
        self.left = int(self.w / 3.5)
        self.top = int(self.h / 5.5)
        self.width = 600
        self.height = 400
        self.setFixedSize(self.width, self.height)

        self.label_1 = QLabel(self.title, self)
        self.line = QLineEdit(self)
        self.button = QPushButton('Click me', self)

        self.total_letter = QLabel("Total Length", self)
        self.total_letter.move(140, 260)
        self.total_letter.setFont(QFont('Arial', 14))
        self.total_numbers = QLabel("Numbers", self)
        self.total_numbers.move(140, 285)
        self.total_numbers.setFont(QFont('Arial', 14))
        self.total_uppercase = QLabel("UpperCase", self)
        self.total_uppercase.move(140, 310)
        self.total_uppercase.setFont(QFont('Arial', 14))
        self.total_special = QLabel("Special Symbols", self)
        self.total_special.move(140, 335)
        self.total_special.setFont(QFont('Arial', 14))

        self.total_letter_val = QLabel("0", self)
        self.total_letter_val.move(450, 260)
        self.total_letter_val.resize(40, 14)
        self.total_letter_val.setFont(QFont('Arial', 14))
        self.total_numbers_val = QLabel("0", self)
        self.total_numbers_val.resize(40, 14)
        self.total_numbers_val.move(450, 285)
        self.total_numbers_val.setFont(QFont('Arial', 14))
        self.total_uppercase_val = QLabel("0", self)
        self.total_uppercase_val.move(450, 310)
        self.total_uppercase_val.resize(40, 14)
        self.total_uppercase_val.setFont(QFont('Arial', 14))
        self.total_special_val = QLabel("0", self)
        self.total_special_val.move(450, 335)
        self.total_special_val.resize(40, 14)
        self.total_special_val.setFont(QFont('Arial', 14))

        self.b1 = QCheckBox("Show Password", self)
        self.b1.setChecked(False)
        self.b1.setFont(QFont('Arial', 10))
        self.b1.setStyleSheet("")
        self.b1.move(355, 130)
        self.b1.setStyleSheet("color:white")
        self.b1.stateChanged.connect(lambda: self.check())
        self.b1.show()

        # creating a label title

        self.label_1.setAlignment(Qt.AlignCenter)
        self.label_1.resize(self.width, int(self.height / 6))
        self.label_1.setFont(QFont('Arial', 24))
        # setting up the border
        self.label_1.move(0, 15)
        self.label_1.setStyleSheet("color:black")

        self.line.setFont(QFont('Arial', 15))
        self.line.move(140, int(self.height / 2.5))
        self.line.textChanged.connect(lambda: self.clicked())
        self.line.setEchoMode(QLineEdit.Password)
        self.line.setAlignment(Qt.AlignCenter)
        self.line.setStyleSheet("border:hidden;padding:5px 5px;background-color:white;color:black")
        self.line.resize(330, 40)

        self.button.setFont(QFont('Arial', 15))
        self.button.setStyleSheet("border:hidden;background:red;color:white;border-radius:5px")
        self.button.resize(330, 40)
        self.button.clicked.connect(lambda: self.clicked())
        self.button.move(140, int(self.height / 1.99))
        self.button.setText("Very Weak")
        self.initUI()



    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color:#0073cf;color:black")
        self.show()

    def clicked(self):
        string = (self.line.text())
        self.total_letter_val.setText(str(len(self.line.text())))
        self.total_uppercase_val.setText(str(self.count_upper_case_letters(string)))
        self.total_numbers_val.setText(str(self.count_integers_letters(string)))
        self.total_special_val.setText(str(self.count_special_letters(string)))

        if len(string) <= 4:
            self.set_weak()
        elif len(string) <= 8 and bool(re.match(r'\w*[A-Z]\w*', string)) and bool(
                re.search(r'\d', string)) and not bool(string.isalnum()):
            self.set_medium()
        elif len(string) <= 8 and bool(re.match(r'\w*[A-Z]\w*', string)) and (
                bool(re.search(r'\d', string)) or not bool(string.isalnum())):
            self.set_medium()
        elif len(string) <= 8 and (
                bool(re.match(r'\w*[A-Z]\w*', string)) or not bool(string.isalnum()) or bool(re.search(r'\d', string))):
            self.set_medium()
        elif len(string) <= 8 and not bool(re.match(r'\w*[A-Z]\w*', string)) and not bool(
                re.search(r'\d', string)) and bool(string.isalnum()):
            self.set_very_weak()
        elif len(string) > 8 and bool(re.search(r'\d', string)) and bool(re.match(r'\w*[A-Z]\w*', string)) and not bool(
                string.isalnum()):
            self.set_very_strong()
        elif len(string) > 8 and bool(re.match(r'\w*[A-Z]\w*', string)) and (
                bool(re.search(r'\d', string)) or not bool(string.isalnum())):
            self.set_strong()
        elif len(string) > 8 and (
                bool(re.match(r'\w*[A-Z]\w*', string)) or not bool(string.isalnum()) or bool(re.search(r'\d', string))):
            self.set_medium()
        elif len(string) > 8 and not bool(re.match(r'\w*[A-Z]\w*', string)) and not bool(
                re.search(r'\d', string)) and bool(string.isalnum()):
            self.set_weak()

    @staticmethod
    def count_upper_case_letters(str_obj):
        count = 0
        for elem in str_obj:
            if elem.isupper():
                count += 1
        return count

    @staticmethod
    def count_integers_letters(str_obj):
        count = 0
        integers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for elem in str_obj:
            if elem in integers:
                count += 1
        return count

    def set_weak(self):
        self.button.setText("Weak")
        self.button.setStyleSheet("border:hidden;background:red;color:white;border-radius:5px")

    def set_medium(self):
        self.button.setText("Medium")
        self.button.setStyleSheet("border:hidden;background:#FCD900;color:black;border-radius:5px")

    def set_strong(self):
        self.button.setText("Strong")
        self.button.setStyleSheet("border:hidden;background:green;color:white;border-radius:5px")

    def set_very_weak(self):
        self.button.setText("Very Weak")
        self.button.setStyleSheet("border:hidden;background:red;color:white;border-radius:5px")

    def set_very_strong(self):
        self.button.setText("Very Strong")
        self.button.setStyleSheet("border:hidden;background:green;color:white;border-radius:5px")

    @staticmethod
    def count_special_letters(str_obj):
        count = 0
        special = ['!', ' ', '"', '#', '$', '%', '&', '\'', '(', ')',
                   '*', '+', ',', '-', '.', '/', ':', ';', '<', '>',
                   '=', '@', '[', ']', '\\', '?', '^', '_', '`', '|',
                   '{', '}', '~']
        for elem in str_obj:
            if elem in special:
                count += 1
        return count

    def check(self):

        if self.b1.isChecked():
            self.line.setEchoMode(QLineEdit.EchoMode.Normal)
            self.line.setText(self.line.text())
        else:
            self.line.setEchoMode(QLineEdit.Password)
            self.line.setText(self.line.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
