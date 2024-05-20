import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QWidget, QPushButton

# import các trang giao diện
from main_ui import Ui_MainWindow
from xem_info import GraphWidget
# cac ham tinh toan
from solveEquation import solve
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init_variable()
        #các kết quả tính toán
        # solution_list chứa danh sách các kết quả, best_fitness_list chứa độ fitness tương ứng với solution
        #self.be_equation la pt duoc xu ly
        self.best_fitness_list = ''
        self.solution_list = ''
        self.be_equation = ''
        # danh sách chứa text của các nút
        self.btn_list = self.ui.frame_2.findChildren(QPushButton)
        # for button in self.btn_list:
            # print(button.text())
        # nhấn 1 nút bất kì sẽ gọi hàm num_operand_click
        for button in self.btn_list:
            button.clicked.connect(self.num_operand_click)

        # equation and ans
        # dù gõ vào textfield hay bấm nút đều được cập nhật
        self.equation = ''
        self.outputfield.textChanged.connect(self.update_equation)

        # Tạo ra đồ thị ứng với kết quả tìm được
        self.graph_widget = GraphWidget()
    def init_variable(self):
        self.info = self.ui.info    # xem đồ thị
        self.resultfield = self.ui.resultfield  # khu vực chứa kết quả
        self.outputfield = self.ui.outputfield  # khu vực chứa pt

    def num_operand_click(self):
        # lấy ra text của nút được nhấn
        button = self.sender()
        text = button.text()
        # DEL: nếu rơi vào các ký hiệu đặc biệt(sin cos...): sẽ xoá tương ứng với độ dài ký tự đó
        # còn lại như + _ * 1,2,3.. thì chỉ xoá ký tự cuối cùng
        # cập nhật cho self.equation và self.outputfield
        if text == 'DEL':
            if self.equation.endswith('sin') or self.equation.endswith('cos') or self.equation.endswith('abs'):
                self.equation = self.equation[:-3]  # xóa 3 ký tự cuối
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
        # AC thid xoá text ở outputfield và resultfield
        elif text == 'AC':
            self.equation = ''
            self.outputfield.setText('')
            self.ui.resultfield.setText('')
        # solve: thay thế '^' thành '**' do python không s dụng '^'
        # gọi đến hàm solve ở module solveEquation
        # hàm solve trả về best_fitness_list và solution_list
        # kết quả tối ưu của bài toán là solution_list[-1] với fitness best_fitness_list[-1]
        # nếu best_fitness = 999 nghĩa là có lỗi cú pháp trong pt , in ra FUNC ERR ở result_text
        # nếu không, in ra kết quả ở result_text
        elif text == 'Solve':
            self.backend_equation()

            # solve(self.equation)
            self.best_fitness_list, self.solution_list = solve(self.be_equation)
            print(self.best_fitness_list)
            print(self.solution_list )
            best_fitness = self.best_fitness_list[-1]
            solution = self.solution_list[-1]
            print("Best Fitness:", best_fitness)
            print("Solution:", solution)
            if best_fitness == 999:
                result_text = "FUNC ERR"
            else:
                result_text = "Best Fitness: {}\nSolution: {}".format(best_fitness, solution)
            self.ui.resultfield.setText(result_text)
        # Xem info giúp ta thấy được các kết quả được xét cùng fitness tương ứng dưới dạng đồ thị
        elif text == 'Xem info':
            pass
            self.graph_widget.draw_fitness_graph(self.best_fitness_list, self.solution_list)
            self.graph_widget.show()
        # các trường hợp khác, chỉ cần thêm vào self.equation và cập nhật self.outputfield
        else:
            self.equation += text
            self.outputfield.setText(self.equation)

    # cập nhật self.outputfield khi người dùng gõ trực tiếp
    def update_equation(self):
        self.equation = self.outputfield.text()
        # print(self.equation)
    def backend_equation(self):
        self.be_equation = self.equation.replace('^', '**')
        i = 0
        while i < len(self.be_equation):
            if self.be_equation[i] == 'x':
                # Check if the character before 'x' is a digit
                if i > 0 and self.be_equation[i - 1].isdigit():
                    # Insert '*' before 'x'
                    self.be_equation = self.be_equation[:i] + '*' + self.be_equation[i:]
                    i += 1  # Move the index forward to account for the inserted '*'
            i += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())