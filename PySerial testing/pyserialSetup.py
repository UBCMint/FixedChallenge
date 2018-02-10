'''
Can't really take any credit for this, this is basically exactly what was written
in an article online on using pyserial to communiate with Arduino

Corresponding Arduino sketch is called testing.ino
'''


from time import sleep
import serial

ser = serial.Serial('COM4', 9600)
i = 0

while True:
	 i +=1
	 ser.write(str(i).encode())
	 print (ser.readline())
	 sleep(.5)
	 if i == 5:
	 	i = 0

