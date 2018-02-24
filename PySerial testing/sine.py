import numpy as np
from numpy import fft
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

app = QtGui.QApplication([])

win = pg.GraphicsWindow(title="Something else")  # creates a window
s = win.addPlot(title="Sine plot")  # creates empty space for the plot in the window
f = win.addPlot(title="FFT plot")  # creates empty space for FFT plot in window

windowWidth = 500  # width of the window displaying the curve
Xm = np.linspace(-np.pi, np.pi, windowWidth)
b = 1


def update():
    global b
    y = np.sin(b * Xm)
    fy = np.abs(fft.fft(y))
    s.plot(Xm, y, pen='g', clear=True)
    f.plot(Xm, fy, pen='r', clear=True)
    b += 1
    if b == 10:
        b = 1
    QtGui.QApplication.processEvents()


while True:
    update()

pg.QtGui.QApplication.exec_()  # you MUST put this at the end
