import numpy as np
from numpy import fft
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

app = QtGui.QApplication([]) 

win = pg.GraphicsWindow(title="Something else") # creates a window
p = win.addPlot(title="A plot")  # creates empty space for the plot in the window

windowWidth = 500                       # width of the window displaying the curve
Xm = np.linspace(-np.pi, np.pi, windowWidth)
b=1

def update():
	global b
	y = np.sin(b*Xm)
	fy = np.abs(fft.fft(y))
	p.plot(Xm, y, pen='g', clear = True)
	b+=1
	if b == 10:
		b = 1
	QtGui.QApplication.processEvents() 

while True:
	update()

pg.QtGui.QApplication.exec_() # you MUST put this at the end

