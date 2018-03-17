
<h1 style="text-align:center">UBC Biomedical Engineering Student Team (BEST)</h1>
<h1 style="text-align:center">MINT: Medical Innovation in NeuroTechnology</h1>
<h2 style="text-align:center">Submission to NeuroTechX 2018 Fixed Challenge</h2>

# Mentha 1.0

### Background

### Mechanical:

### Electrical:
We built a 4-channel EEG system which consists of a notch filter, voltage regulator, and instrumental amplifier. 

### Software:
We are using python to collect data from an Arduino and plotting the fourier transform of the the EEG signal in realtime. This allows us to see the peaks in amplitude of the different frequencies of brain signals.

We chose to use pyqtgraph instead matplotlib to improve the speed of live plotting. 

The limitations of this project include the number of channels that acquire data and the delay in the real-time plotting.

To increase the number of channels, we could use more pins available on the Arduino. In the future, we could add more interative components to our system, such as a GUI that allows the user to start and stop data acquisition. 
