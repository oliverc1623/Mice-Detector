# RFidReaderCalTech

# Table of Contents
1. [Prerequisites](#Prerequisites)
2. [Example2](#example2)
3. [Third Example](#third-example)

## Getting Started

Welcome to Mice-Detector. The goal of this project is to allow mice to enter and exit testing chambers without human help. The mice will travel through a tube with 2 RFid sensors on each end. The mice will also have a RFid chip implemented in their head so they can be read. 


### Prerequisites

Hardware: 2 arduino unos, 2 Tower Pro SG-5010 servos, 2 ONETAK 125kHZ RFid Readers, linux machine

Libraries: pyUSB, pyTransitions, keyboard_alike, machine can run python 2.7/3.0

### Installing

To install simply clone/downloads the repository.

Instructions for installing the libraries can be found in the links.

pyUSB: https://github.com/walac/pyusb#installing-pyusb-on-gnulinux-systems

keyboard_alike: https://github.com/riklaunim/pyusb-keyboard-alike

pyTransitions: https://github.com/pytransitions/transitions#installation

Arduino: https://playground.arduino.cc/Linux/Ubuntu

### Connecting Python to Arduino

On the python side initialize 2 arduino objects

Depending on which port you plug the arduino into, the device location may differ. 
```python
arduino1 = serial.Serial('/dev/ttyACM1', 9600)
arduino2 = serial.Serial('/dev/ttyACM0', 9600)
```

### Connecting Arduino to Python

Create servo object
```arduino
Servo myservo;
```

In the setup loop, set the buad to 96000 and connect the servo to the port.
```arduino
Serial.begin(9600); 
myservo.attach(9);
```

### Connecting RFid sensors with Python

```python
#initialize list of RFidReaders connected to computer
device = list(usb.core.find(find_all=True, idVendor=0x16c0, idProduct = 0x27db))
reader1 = reader.Reader(0x16c0, 0x27db, 36, 3, should_reset=False)
reader2 = reader.Reader(0x16c0, 0x27db, 36, 3, should_reset=False)
```

### Running the main file: MiceDetector.py

Open the terminal and cd to folder with all the files.

```terminal
sudo python MiceDetector.py
```
