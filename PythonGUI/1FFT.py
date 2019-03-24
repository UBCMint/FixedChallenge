# Author: Jessica Ma
# Date: March 13th, 2018
# Reads four values from serial and plots their FFTs in four plots in pyqtgraph
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
# Remember to change port name if necessary and run the appropriate Arduino program
port_name = "COM7"
baudrate = 250000
ser = serial.Serial(port_name,baudrate)

# Creates file with current time to store data in csv format
timestr = time.strftime("%Y%m%d-%H%M%S")
datafile = open( "raw-" + timestr + ".txt", "w+")
datafile.write("port1,port2,port3,port4\n")

# Initializing all the windows/plots 
app = QtGui.QApplication([])
view = pg.GraphicsView()
view.resize(800,600)
win = pg.GraphicsLayout()
view.setCentralItem(win)
view.show()
view.setWindowTitle('Live plots of EEG in frequency domain from 4 channels')

# Top label
win.addLabel('EEG data from Arduino in frequency domain', colspan=4)

# First row of plots
win.nextRow()
p1 = win.addPlot(title="FFT Signal 1", labels={'left':'Amplitude', 'bottom':'Frequency (Hz)'})
p2 = win.addPlot(title="FFT Signal 2", labels={'left':'Amplitude', 'bottom':'Frequency (Hz)'})

# Second row of plots 
win.nextRow()
p3 = win.addPlot(title="FFT Signal 3", labels={'left':'Amplitude', 'bottom':'Frequency (Hz)'})
p4 = win.addPlot(title="FFT Signal 4", labels={'left':'Amplitude', 'bottom':'Frequency (Hz)'})

p1.setRange(xRange=[0,170])
p2.setRange(xRange=[0,170])
p3.setRange(xRange=[0,170])
p4.setRange(xRange=[0,170])

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
	return list(map(float, data.split(",")))

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
	value2 = data_array[0]
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

# filter out 60Hz note: the filter cuts out a frequency 2.13 times larger than the index target
	FFT1=np.abs(fft.fft(Xm1))
	FFFT1 = [f if (index < 27 and f >1 or index > 30 and f > 1) else 0 for index, f in enumerate(FFT1)]
	FFT1=FFFT1[1:251]    
	FFT2=np.abs(fft.fft(Xm1))
	FFFT2 = [f if (index < 27 and f >1 or index > 30 and f > 1) else 0 for index, f in enumerate(FFT2)]
	FFT2=FFFT2[1:251]
	FFT3=np.abs(fft.fft(Xm3))
	FFFT3 = [f if (index < 27 and f >1 or index > 30 and f > 1) else 0 for index, f in enumerate(FFT3)]
	FFT3=FFFT3[1:251]
	FFT4=np.abs(fft.fft(Xm4))
	FFFT4 = [f if (index < 27 and f >1 or index > 30 and f > 1) else 0 for index, f in enumerate(FFT4)]
	FFT4=FFFT4[1:251]

	ptr += 1

	curve3.setData(Xm1)
	curve4.setData(Xm1)

	curve3.setPos(ptr,0)
	curve4.setPos(ptr,0)
#currently not displaying the 4 channels correctly, adjust
	curve1.setData(np.linspace(0,540,250), FFT1)
	curve2.setData(np.linspace(0,540,250), FFT2)
	curve3.setData(np.linspace(0,170,250), FFT3)
	curve4.setData(np.linspace(0,170,250), FFT4)
	
	QtGui.QApplication.processEvents()

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)

# Main program: executes the update function and updates the graph
while True: update()
pg.QtGui.QApplication.exec_()
