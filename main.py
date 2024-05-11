import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QListWidgetItem, QWidget, QPushButton
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QFont

# import ui class
from main_ui import Ui_MainWindow
# cac ham tinh toan
from solveEquation import solve
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init_variable()
        # list of button
        self.btn_list = self.ui.frame_2.findChildren(QPushButton)
        # for button in self.btn_list:
        #     print(button.text())
        for button in self.btn_list:
            button.clicked.connect(self.num_operand_click)

        # equation and ans
        self.resultfield = self.ui.resultfield
        self.outputfield = self.ui.outputfield
        self.equation = ''
        self.outputfield.textChanged.connect(self.update_equation)
    def init_variable(self):
        self.info = self.ui.info

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
            self.ui.resultfield.setText('')
        elif text == 'Solve':
            self.equation = self.equation.replace('^', '**')
            solve(self.equation)
            best_fitness, solution = solve(self.equation)
            print("Best Fitness:", best_fitness)
            print("Solution:", solution)
            if best_fitness == 999:
                result_text = "FUNC ERR"
            else:
                result_text = "Best Fitness: {}\nSolution: {}".format(best_fitness, solution)
            self.ui.resultfield.setText(result_text)
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