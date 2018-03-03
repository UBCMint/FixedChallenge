import numpy as np
from numpy import fft
from pyqtgraph.Qt import QtGui, QtCore
from pyqtgraph.ptime import time

import pyqtgraph as pg
import serial
from time import time

# Create object serial port
portName = "/dev/cu.usbmodem1421"                      # replace this port name by yours!
baudrate = 9600
ser = serial.Serial(portName,baudrate)

start_time = time()
timepoints = []

app = QtGui.QApplication([])

win = pg.GraphicsWindow(title="Plotting Window")  # creates a window
s = win.addPlot(title="Sine plot")  # creates empty space for the plot in the window
f = win.addPlot(title="FFT plot")  # creates empty space for FFT plot in window
curve = pg.plot()                        # create an empty "plot" (a curve to plot)
data = [0]

windowWidth = 500  # width of the window displaying the curve
Xm = np.linspace(0, timepoints, windowWidth)
b = 1
ptr = 0


def update():
    global b
    line = ser.readline()
    data.append(int(line))
    xdata = np.array(data, dtype='float64')
    curve.setData(xdata)
    app.processEvents()
    Xm[:-1] = Xm[1:]  # shift data in the temporal mean 1 sample left
    value = ser.readline()  # read line (single value) from the serial port
    Xm[-1] = float(value)  # vector containing the instantaneous values
    ptr += 1  # update x position for displaying the curve
    curve.setData(Xm)  # set the curve with this data
    curve.setPos(timepoints[ptr], 0)  # set x position in the graph to 0
    y = np.sin(b * Xm)
    fy = np.abs(fft.fft(y))
    s.plot(Xm, y, pen='g', clear=True)
    f.plot(Xm, fy, pen='r', clear=True)
    #b += 1
    #if b == 10:
     #   b = 1
    if ptr > 5:
        ptr == 0

    QtGui.QApplication.processEvents()


while True:
    update()

pg.QtGui.QApplication.exec_()  # you MUST put this at the end
