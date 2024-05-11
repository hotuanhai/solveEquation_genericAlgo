import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
class GraphWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create a Matplotlib figure and canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot()

        # Create a vertical layout for the widget
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def draw_fitness_graph(self, best_fitness_list, solution_list):
        # Clear previous plot
        self.ax.clear()

        # Plot the fitness graph
        self.ax.plot(best_fitness_list, solution_list, marker='o')
        self.ax.set_xlabel('Best Fitness')
        self.ax.set_ylabel('Solution')
        self.ax.set_title('Solution vs. Best Fitness')

        # Adjust layout spacing
        self.figure.tight_layout()

        # Refresh canvas
        self.canvas.draw()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     widget = GraphWidget()
#     widget.show()
#     sys.exit(app.exec())
