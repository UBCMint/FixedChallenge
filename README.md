# Mentha 1.0

### Background

For the NeurotechX competition Fixed Challenge, MINT is building an EEG collection system from scratch, that will accurately and effectively collect scalp potentials and minimise noise.
The system will use an Arudino microcontroller to send the data aqcuired to the computer. We will then use a python script to live-plot the fourier transform of the data recieved. 


### Usage
The scripts can be downloaded from the github repository and can be run with any Python interpreter. The electrodes should be clipped onto the hair and placed closely against the scalp. Alternatively, gel electrodes can be placed on the forehead. The Arduino Leo pins A0-A3 receive the data from the main circuit. 

## Mechanical:

## Electrical:
The 4-channel EEG system consists of a notch filter, voltage regulator, and instrumental amplifier. 

Since the Arduino can only read from 0-5V, the signal acquired through the electrode is amplified by a LM324 quadruple operational amplifier from microvolts to volts. The notch filter then filters out 60Hz noise that arises from power line interference. The shifter offsets the signal by 2.5V so that there are no negative voltages being inputted into the Arduino. The 9V battery connects to a voltage regulator to power the entire circuit.

## Software:
We are using python to collect data from an Arduino and plotting the fourier transform of the the EEG signal in realtime. This allows us to see the peaks in amplitude of the different frequencies of brain signals.

We chose to use pyqtgraph instead of matplotlib to improve the speed of live plotting. 

### Limitations
The limitations of the software application include the number of channels that acquire data and the delay in the real-time plotting.

To increase the number of channels, we could use more of the pins available on the Arduino. This can be easily added into the python script, albeit we are limited to the 
number of pins on the Arduino or microcontroller we are using. In the future, we could add more interative components to our system, such as a GUI that allows the user to start and stop data acquisition. Another improvement would include the ability to save data and retrieve previous data. These
extra features could also be implemented through a phone app. 


