import numpy 
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
from pyqtgraph.ptime import time
import serial
import struct
import csv
import collections

source = open('datafile.txt')
reader = source.readline()
dq = collections.deque(maxlen=50)

for _ in range(50):
	dq.append(source.readline())

while True:
	for _ in range(10):
		dq.append(source.readline())

'''
app = QtGui.QApplication([])            

win = pg.GraphicsWindow(title="Fourier Transform") 
p = win.addPlot(title="Realtime plot")  
curve = p.plot()                        
windowWidth = 500                       # width of the window displaying the curve
Xm = linspace(0,0,windowWidth)          # create array that will contain the relevant time series     
shift = -windowWidth     

def update():
	global dq, curve, shift, Xm
	Xm[:-1] = Xm[1:] 
	value = fft.fft(dq)
	Xm[-1] = value
	shift += 1                            
	curve.setData(Xm)                   
	curve.setPos(shift,0)                  
	QtGui.QApplication.processEvents()    

### MAIN PROGRAM ###    
while True: update()

### END QtApp ###
pg.QtGui.QApplication.exec_()

'''