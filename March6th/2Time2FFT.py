# Author: Jessica Ma
# Date: March 13th, 2018
# Reads four values from serial and plots them in four separate plots with pyqtgraph.
# Adjust port_name to whatever it says in the Arduino IDE

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
timestr = time.strftime("%Y%m%d-%H%M%S")
datafile = open(timestr+".txt", "w+")

# Initializing all the windows/plots 
app = QtGui.QApplication([])
view = pg.GraphicsView()
view.resize(800,600)
win = pg.GraphicsLayout()
view.setCentralItem(win)
view.show()
view.setWindowTitle('Live plots of EEG from 4 channels')

# Top label
win.addLabel('FFT of EEG signal', colspan=4)

# First row of plots
win.nextRow()
p1 = win.addPlot(title="FFT of Signal 1", labels={'left':'Amplitude', 'bottom':'Frequency (Hz)'})
p2 = win.addPlot(title="FFT of Signal 2", labels={'left':'Amplitude', 'bottom':'Frequency (Hz)'})

# Second row of plots 
win.nextRow()
p3 = win.addPlot(title="Signal 1", labels={'left':'Amplitude', 'bottom':'Frequency (Hz)'})
p4 = win.addPlot(title="Signal 2", labels={'left':'Amplitude', 'bottom':'Frequency (Hz)'})

# Setting the axes limits and all that good stuff
p1.setRange(xRange=[0,100])
p2.setRange(xRange=[0,100])
#p3.setRange(xRange=[0,100])
#p4.setRange(xRange=[0,100])

curve1 = p1.plot()
curve2 = p2.plot()
curve3 = p3.plot()
curve4 = p4.plot()

windowWidth = 500                      
Xm1 = np.linspace(0,0,windowWidth)
Xm2 = np.linspace(0,0,windowWidth)
#Xm3 = np.linspace(0,0,windowWidth)
#Xm4 = np.linspace(0,0,windowWidth)   
ptr = -windowWidth
data_array = [0.0, 0.0, 0.0, 0.0]

# Collects the data from serial and places it in an array 
def read_data():
	val1 = ser.readline()
	val2 = ser.readline()
	#val3 = ser.readline()
	#val4 = ser.readline()
	#return [val1, val2, val3, val4]
	return [val1, val2]

# Update dat 
def update():
	global curve1, curve2, curve3, curve3, ptr, Xm1, Xm2, Xm3, Xm4

	data_array = read_data()

	Xm1[:-1] = Xm1[1:]
	Xm2[:-1] = Xm2[1:]
	#Xm3[:-1] = Xm3[1:]
	#Xm4[:-1] = Xm4[1:]

	value1 = data_array[0]
	value2 = data_array[1]
	#value3 = data_array[2]
	#value4 = data_array[3]

	datafile.write('port1: ' + str(value1))
	datafile.write('port2: ' + str(value2))
	#datafile.write('port3: ' + str(value3))
	#datafile.write('port4: ' + str(value4))

    # to stop it from ending spontaneously
	try: 
		Xm1[-1] = float(value1)
		Xm2[-1] = float(value2)
	#	Xm3[-1] = float(value3)
	#	Xm4[-1] = float(value4)
	except ValueError:
		pass

#For testing by plotting the raw signal:
	#curve1.setData(np.linspace(0,100,500), Xm1)
	#curve2.setData(np.linspace(0,100,500), Xm2)
	curve3.setData(np.linspace(0,100,500), Xm1)
	curve4.setData(np.linspace(0,100,500), Xm2)
	#QtGui.QApplication.processEvents()
		
	FFT1=np.abs(fft.fft(Xm1))
	FFT1=FFT1[:250]    
	FFT2=np.abs(fft.fft(Xm2))
	FFT2=FFT2[:250]
	#FFT3=np.abs(fft.fft(Xm3))
	#FFT3=FFT3[:250]
	#FFT4=np.abs(fft.fft(Xm4))
	#FFT4=FFT4[:250]
	ptr += 1

	curve1.setData(np.linspace(0,100,250), FFT1)
	curve2.setData(np.linspace(0,100,250), FFT2)
	#curve3.setData(np.linspace(0,100,250), FFT3)
	#curve4.setData(np.linspace(0,100,250), FFT4)
	QtGui.QApplication.processEvents()

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)

# Main program: executes the update function and updates the graph
while True: update()
pg.QtGui.QApplication.exec_()
