import numpy as numpy
from numpy import fft
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
from pyqtgraph.ptime import time
import serial
import struct
import matplotlib

# Create object serial port
portName = "COM4"                      # replace this port name with what it says in arduino IDE thing
baudrate = 9600
ser = serial.Serial(portName,baudrate)

# Writing to a file
datafile = open("datafile.txt", "wb+") # file where the data values will be written

### Starting and setup of QtApp ###
app = QtGui.QApplication([])            

win = pg.GraphicsWindow(title="Signal from serial port") 
p = win.addPlot(title="Realtime plot")  
curve = p.plot()                        
windowWidth = 500                       # width of the window displaying the curve
Xm = numpy.linspace(0,0,windowWidth)          # create array that will contain the relevant time series     
ptr = -windowWidth                      

# Realtime data plot. Each time this function is called, the data display is updated
def update():
    global curve, ptr, Xm    
    Xm[:-1] = Xm[1:]                    
    value = ser.readline()              # writes the values to the file
    datafile.write(value)                   
    Xm[-1] = float(value)  
    ptr += 1                            
    curve.setData(numpy.abs(fft.fft(Xm)))                   
    curve.setPos(ptr,0)                  
    QtGui.QApplication.processEvents()    

### MAIN PROGRAM ###    
while True: update()

### END QtApp ###
pg.QtGui.QApplication.exec_()
