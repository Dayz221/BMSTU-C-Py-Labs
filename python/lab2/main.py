from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt
from design import Ui_MainWindow
import sys

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import numpy as np
import math

from functions import *

matplotlib.use("Qt5Agg")


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.fig.set_facecolor("#eee")
        self.axes.set_facecolor("#eee")
        self.fig.subplots_adjust(0.1, 0.2, 0.95, 0.9)

        self.clear()

        super().__init__(self.fig)

    def clear(self):
        self.axes.cla()

        self.axes.set_title("График функции", pad=15)

        self.axes.spines['top'].set_visible(False)
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['left'].set_visible(False)
        self.axes.spines['bottom'].set_visible(False)

        self.axes.axhline(0, color='#0a0', linewidth=1, label="Ось Ox")

        self.axes.grid(True)


class Root:
    def __init__(self, x = None, fx = None, segment = None, iters = None, error = 0):
        self.x = x
        self.fx = fx
        self.segment = segment
        self.iters = iters
        self.error = error

    def getX(self):
        if self.x is not None: return QTableWidgetItem(f"{self.x:.5g}")
        else: return QTableWidgetItem("-")

    def getY(self):
        if self.fx is not None: return QTableWidgetItem(f"{self.fx:.1g}")
        else: return QTableWidgetItem("-")

    def getSegment(self):
        if self.segment is not None: return QTableWidgetItem(f"[{self.segment[0]:.5g}, {self.segment[1]:.5g}]")
        else: return QTableWidgetItem("-")

    def getIters(self):
        if self.iters is not None: return QTableWidgetItem(f"{self.iters}")
        else: return QTableWidgetItem("-")
    
    def getStatus(self):
        return QTableWidgetItem(f"{self.error}")


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Лабораторная работа №2")
        
        self.matplotlibCanvas = MplCanvas()

        graphContainer = self.graphContainer.layout()
        graphContainer.addWidget(self.matplotlibCanvas)

        self.table.setAlternatingRowColors(True)
        header = self.table.horizontalHeader()
        for column in range(self.table.columnCount()):
            header.setSectionResizeMode(column, QHeaderView.Stretch)

        self.table.setHorizontalHeaderLabels(['№ корня', '[xi; xi+1]', 'x`', 'f(x`)', 'Количество итераций', 'Код ошибки'])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        self.buildGraph.clicked.connect(self.redrawGraph)
        
        self.redrawGraph()
        self.matplotlibCanvas.fig.legend(loc="lower center", bbox_to_anchor=(0.5, 0), ncol=3)

    def strToFunc(self, string: str):
        math_functions = {name: func for name, func in math.__dict__.items() if callable(func)}
        math_constants = {name: value for name, value in math.__dict__.items() if not callable(value)}
        
        math_dump = {"__builtins__": None}
        math_dump.update(math_functions)
        math_dump.update(math_constants)

        return lambda x: eval(string.lower(), math_dump, {"x": x})

    def redrawGraph(self):
        func = self.strToFunc(self.funcVal.text())

        start = self.startVal.value()
        end = self.endVal.value()
        step = self.stepVal.value()
        
        eps = self.epsVal.value()
        
        if not (0 < eps <= 1):
            self.matplotlibCanvas.clear()
            self.matplotlibCanvas.axes.set_title("Eps должна быть в полуинтервале (0, 1]!")
            self.matplotlibCanvas.draw()
            return

        n_max = self.maxIterVal.value()

        x_coords = list(np.arange(start, end, step)) + [end]
        y_coords = []

        roots: list[Root] = []

        for x in x_coords:
            try:
                val = func(x)
                y_coords.append(val)

            except ZeroDivisionError as ex:
                y_coords.append(np.nan)

            except (SyntaxError, NameError, TypeError, ValueError, OverflowError) as ex:
                self.table.setRowCount(0)
                self.matplotlibCanvas.clear()
                self.matplotlibCanvas.axes.set_title("Некорректная формула")
                self.matplotlibCanvas.draw()
                print(ex)
                return

            try:
                iters, root = findRoot(func, x + step / 2, x, x + step, eps, n_max)
                if iters > 0: 
                    print(root)
                    roots.append(Root(root, func(root), [x, x+step], iters))
                
                elif iters == TOO_MANY_ITERATIONS:
                    roots.append(Root(root, func(root), [x, x+step], error=1))
                
                elif iters == DIVISION_BY_ZERO:
                    roots.append(Root(segment=[x, x+step], error=2))
                    pass

            except Exception as ex:
                print(ex)

        self.matplotlibCanvas.clear()

        self.matplotlibCanvas.axes.set_xlim(start - 0.3*abs(start-end), end + 0.3*abs(start-end))
        self.matplotlibCanvas.axes.plot(x_coords, y_coords, label="График функции", zorder=2)

        roots_pos = list(zip(*[[e.x, e.fx] for e in roots if not e.error]))
        if len(roots_pos) != 0:
            self.matplotlibCanvas.axes.scatter(roots_pos[0], roots_pos[1], marker="o", color="red", label="Корни", zorder=4)
        
        self.matplotlibCanvas.draw()

        self.table.setRowCount(len(roots))
        for i, root in enumerate(roots):
            self.table.setItem(i, 0, QTableWidgetItem(str(i+1)))
            self.table.setItem(i, 1, root.getSegment())
            self.table.setItem(i, 2, root.getX())
            self.table.setItem(i, 3, root.getY())
            self.table.setItem(i, 4, root.getIters())
            self.table.setItem(i, 5, root.getStatus())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    app.exec()
