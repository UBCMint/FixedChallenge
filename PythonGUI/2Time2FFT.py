
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
baudrate = 9600
ser = serial.Serial(port_name,baudrate)

# Creates file with current time to store data in csv format
timestr = time.strftime("%Y%m%d-%H%M%S")
datafile = open( "raw-" + timestr + ".txt", "w+")
datafile.write("port1,port2\n")

# Initializing all the windows/plots 
app = QtGui.QApplication([])
view = pg.GraphicsView()
view.resize(800,600)
win = pg.GraphicsLayout()
view.setCentralItem(win)
view.show()
view.setWindowTitle('Live plots of EEG from 2 channels in time and frequency domain')

# Top label
win.addLabel('Raw and processed signal from Arduino', colspan=4)

# First row of plots: plain signal
win.nextRow()
p1 = win.addPlot(title="Signal 1", labels={'left':'Amplitude', 'bottom':'Time elapsed'})
p2 = win.addPlot(title="Signal 2", labels={'left':'Amplitude', 'bottom':'Time elapsed'})

# Second row of plots: FFT
win.nextRow()
p3 = win.addPlot(title="FFT of Signal 1", labels={'left':'Amplitude', 'bottom':'Frequency (Hz)'})
p4 = win.addPlot(title="FFT of Signal 2", labels={'left':'Amplitude', 'bottom':'Frequency (Hz)'})

curve1 = p1.plot()
curve2 = p2.plot()
curve3 = p3.plot()
curve4 = p4.plot()

# Only need to limit axes for FFT plots
p3.setRange(xRange=[0,170])
p4.setRange(xRange=[0,170])

windowWidth = 500                      
Xm1 = np.linspace(0,0,windowWidth)
Xm2 = np.linspace(0,0,windowWidth)
Xm3 = np.linspace(0,0,windowWidth)
Xm4 = np.linspace(0,0,windowWidth)   
ptr = -windowWidth
data_array = [0.0, 0.0]

# Reads string from serial and converts it to list of ints
def read_data():
	data = ser.readline().decode()
	while data.isspace(): # if faulty reading (whitespace), keep trying
		data = ser.readline().decode()
	millis = str(round(time.time() * 1000))
	datafile.write(data + ',' + millis)
	return list(map(int, data.split(",")))

# Infinite loop that implements live graphing
def update():
	global curve1, curve2, curve3, curve3, ptr, Xm1, Xm2, Xm3, Xm4

	# Gets data and writes to file in csv format
	data_array = read_data()
	
	Xm1[:-1] = Xm1[1:]
	Xm2[:-1] = Xm2[1:]

	value1 = data_array[0]
	value2 = data_array[1]

    # Stop it from ending spontaneously if there is conversion error
	try: 
		Xm1[-1] = float(value1)
		Xm2[-1] = float(value2)
	except ValueError:
		pass

	ptr += 1
	if ptr%10 == 0:
		FFT1=np.abs(fft.fft(Xm1))
		FFT1=FFT1[1:251]    
		FFT2=np.abs(fft.fft(Xm2))
		FFT2=FFT2[1:251]
		curve3.setData(np.linspace(0,170,250), FFT1)
		curve4.setData(np.linspace(0,170,250), FFT2)

	curve1.setData(Xm1)
	curve2.setData(Xm2)
	curve1.setPos(ptr,0)
	curve2.setPos(ptr,0)
	
	QtGui.QApplication.processEvents()

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)

# Main program: executes the update function and updates the graph
while True: update()
pg.QtGui.QApplication.exec_()
