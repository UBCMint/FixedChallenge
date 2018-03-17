# Author: Jessica Ma
# Date: March 13th, 2018
# Reads four values from serial and plots them in four separate plots with pyqtgraph.
# Adjust port_name to whatever it says in the Arduino IDE
# Arduino program: 4Reads

import numpy as np
from numpy import fft
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
from pyqtgraph.ptime import time
import time
import serial

# Create serial port and file for writing data
port_name = "COM4"
baudrate = 9600
ser = serial.Serial(port_name,baudrate)

# Creates file with current time to store data in csv format
# "raw-" indicates all four values are the raw data as opposed to fourier transformed
timestr = time.strftime("%Y%m%d-%H%M%S")
datafile = open( "raw-" + timestr + ".txt", "w+")
datafile.write("port1,port2,port3,port4\n")

# Initializing all the windows/plots 
app = QtGui.QApplication([])
view = pg.GraphicsView()
view.resize(800,500)
win = pg.GraphicsLayout()
view.setCentralItem(win)
view.show()
view.setWindowTitle('Live plots of EEG from 4 channels')

# Top label
win.addLabel('Raw signal from Arduino', colspan=4)

# First row of plots
win.nextRow()
p1 = win.addPlot(title="Signal 1", labels={'left':'Amplitude', 'bottom':'Time elapsed'})
p2 = win.addPlot(title="Signal 2", labels={'left':'Amplitude', 'bottom':'Time elapsed'})

# Second row of plots 
win.nextRow()
p3 = win.addPlot(title="Signal 3", labels={'left':'Amplitude', 'bottom':'Time elapsed'})
p4 = win.addPlot(title="Signal 4", labels={'left':'Amplitude', 'bottom':'Time elapsed'})

curve1 = p1.plot()
curve2 = p2.plot()
curve3 = p3.plot()
curve4 = p4.plot()

windowWidth = 500                      
Xm1 = np.linspace(0,0,windowWidth)
Xm2 = np.linspace(0,0,windowWidth)
Xm3 = np.linspace(0,0,windowWidth)
Xm4 = np.linspace(0,0,windowWidth)   
ptr = -windowWidth
data_array = [0.0, 0.0, 0.0, 0.0]

# Reads string from serial and converts it to list of ints
def read_data():
	data = ser.readline().decode()
	while data.isspace(): # if faulty reading (whitespace), keep trying
		data = ser.readline().decode()
	datafile.write(data)
	return list(map(int, data.split(",")))

# Infinite loop that implements live graphing
def update():
	global curve1, curve2, curve3, curve3, ptr, Xm1, Xm2, Xm3, Xm4

	# Gets data and writes to file in csv format
	data_array = read_data()
	
	Xm1[:-1] = Xm1[1:]
	Xm2[:-1] = Xm2[1:]
	Xm3[:-1] = Xm3[1:]
	Xm4[:-1] = Xm4[1:]

	value1 = data_array[0]
	value2 = data_array[1]
	value3 = data_array[2]
	value4 = data_array[3]

    # Stop it from ending spontaneously if there is conversion error
	try: 
		Xm1[-1] = float(value1)
		Xm2[-1] = float(value2)
		Xm3[-1] = float(value3)
		Xm4[-1] = float(value4)
	except ValueError:
		pass

	ptr += 1
	curve1.setData(Xm1)
	curve2.setData(Xm2)
	curve3.setData(Xm3)
	curve4.setData(Xm4)

	curve1.setPos(ptr,0)
	curve2.setPos(ptr,0)
	curve3.setPos(ptr,0)
	curve4.setPos(ptr,0)
	QtGui.QApplication.processEvents()

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)

# Main program: executes the update function and updates the graph
while True: update()
pg.QtGui.QApplication.exec_()
