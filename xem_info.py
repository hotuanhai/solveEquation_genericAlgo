from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
class GraphWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Tạo Matplotlib figure and canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot()

        # Tạo  bố cục cho widget
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def draw_fitness_graph(self, best_fitness_list, solution_list):
        # Xoá đồ thị trước đó
        self.ax.clear()

        # vẽ đồ thị với
        # best_fitness_list ở trục y và solution_listo ở trục x
        self.ax.plot(solution_list,best_fitness_list , marker='o')
        self.ax.set_xlabel('Solution')
        self.ax.set_ylabel('Best Fitness')
        self.ax.set_title('Solution vs. Best Fitness')

        # Điều chỉnh khoảng cách bố cục
        self.figure.tight_layout()

        # làm mới canvas
        self.canvas.draw()

