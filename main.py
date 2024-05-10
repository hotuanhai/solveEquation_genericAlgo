import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QListWidgetItem, QWidget, QPushButton
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QFont

# import ui class
from main_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init_variable()
        # list of button
        self.btn_list = self.ui.frame_2.findChildren(QPushButton)
        for button in self.btn_list:
            print(button.text())
        for button in self.btn_list:
            button.clicked.connect(self.num_operand_click)

        # equation
        self.outputfield = self.ui.outputfield
        self.equation = ''
        self.outputfield.textChanged.connect(self.update_equation)
    def init_variable(self):
        self.plus = self.ui.plus
        self.minus = self.ui.minus
        self.multiple = self.ui.multiple
        self.divide = self.ui.multiple
        self.power = self.ui.power
        self.sqrt = self.ui.sqrt
        self.varx = self.ui.varx
        self.sin = self.ui.sin
        self.cos = self.ui.cos
        self.abs = self.ui.abs
        # other
        self.delete = self.ui.delete_2
        self.ac = self.ui.ac
        self.solve = self.ui.solve

    def num_operand_click(self):
        button = self.sender()
        text = button.text()
        if text == 'DEL':
            if self.equation.endswith('sin') or self.equation.endswith('cos') or self.equation.endswith('abs'):
                self.equation = self.equation[:-3]  # Remove the last 3 characters from equation
                current_text = self.outputfield.text()
                self.outputfield.setText(current_text[:-3])
            elif self.equation.endswith('sqrt'):
                self.equation = self.equation[:-4]
                current_text = self.outputfield.text()
                self.outputfield.setText(current_text[:-4])
            else:
                self.equation = self.equation[:-1]
                current_text = self.outputfield.text()
                self.outputfield.setText(current_text[:-1])
        elif text == 'AC':
            self.equation = ''
            self.outputfield.setText('')
        elif text == 'Solve':
            pass
        else:
            # add if its just num or regular operand
            self.equation += text
            self.outputfield.setText(self.equation)

    def update_equation(self):
        self.equation = self.outputfield.text()
        print(self.equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())