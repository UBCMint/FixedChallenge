# Mentha 1.0

### Background

For the NeurotechX competition Fixed Challenge, MINT is building an EEG collection system from scratch, that will accurately and effectively collect scalp potentials and minimise noise.
The system will use an Arudino microcontroller to send the data aqcuired to the computer. We will then use a python script to live-plot the fourier transform of the data recieved. 

We made our design choices based on availability and affordabiliity such that other teams can recreate our system. 

### Usage
The scripts can be downloaded from the github repository and can be run with any Python interpreter. The electrodes should be clipped onto the hair and placed closely against the scalp. Alternatively, gel electrodes can be placed on the forehead. The Arduino Leo pins A0-A3 receive the data from the main circuit. 

## Mechanical:
We used CAD to design the case for the electrical components out of 3D-printed ABS and sheet metal, with the goals of minmizing interference between the parts and keeping the assembly as small as possible. 

We also designed many different styles of electrodes for the EEG system. Choosing to 3D-print the electrodes and then coat them in conductive silver paint allowed us to fully optimize their geometry for skin contact through hair.

## Electrical:
The 4-channel EEG system consists of a notch filter, voltage regulator, and instrumental amplifier. 

Since the Arduino can only read from 0-5V, the signal acquired through the electrode is amplified by a INA114 precision instrumentation amplifier from microvolts to volts. The INA114 was chosen because it was readily available and affordable. 
The notch filter then filters out 60Hz noise that arises from power line interference using the LM324 quadruple operational amplifier. The shifter then offsets the signal by 2.5V so that there are no negative voltages being inputted into the Arduino. 
Lastly, the 9V battery connects to a voltage regulator to power the entire circuit.

### Limitations

A limitation of Mentha's electrical system is the amount of space available within the mechanical chassis, as we wanted to keep the device small and portable. We had to design our circuits wisely to have efficient use of the available space. In the future we would implement our design on a PCB to optimize layout and increase reliability. 


## Software:
We are using python to collect data from an Arduino and plotting the fourier transform of the the EEG signal in realtime. This allows us to see the peaks in amplitude of the different frequencies of brain signals.

![Python GUI](https://raw.githubusercontent.com/UBCMint/FixedChallenge/master/PythonGUI/screenshots/plot.PNG)

We chose to use pyqtgraph instead of matplotlib to improve the speed of live plotting. 

We originally prototyped with Matlab, but found that Python provided a better GUI and realtime plotting.

### Limitations
The limitations of the software application include the number of channels that acquire data and the delay in the real-time plotting.

To increase the number of channels, we could use more of the pins available on the Arduino. This can be easily added into the python script, albeit we are limited to the 
number of pins on the Arduino or microcontroller we are using. In the future, we could add more interative components to our system, such as a GUI that allows the user to start and stop data acquisition. Another improvement would include the ability to save data and retrieve previous data. These
extra features could also be implemented through a phone app. 

## About Us

Mentha was created by the [(Medical Innovation in NeuroTechnology](https://ubcmint.github.io/) (MINT) team of undergraduate students, part of the group [Biomedical Engineering Student Team](http://www.ubcbest.com/) at the University of British Columbia in Vancouver, Canada.

Mentha was submitted as a project for the Fixed Challenge category of the [NeuroTechX 2018 Student Club competition](https://neurotechx.github.io/studentclubs/competition/).
