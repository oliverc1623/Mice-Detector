# RFidReaderCalTech

# Table of Contents
1. [Getting Started](#getting-started)
2. [Prerequisites](#prerequisites)
3. [Installing](#installing)
4. [Connecting Python to Arduino](#connecting-python-to-arduino)
5. [Connecting arduino to python](#connecting-python-to-arduino)


## Getting Started

Welcome to Mice-Detector. The goal of this project is to allow mice to enter and exit testing chambers without human help. The mice will travel through a tube with 2 RFid sensors on each end. The mice will also have a RFid chip implemented in their head so they can be read. 


### Prerequisites

Hardware: 2 arduino unos, 2 Tower Pro SG-5010 servos, 2 ONETAK 125kHZ RFid Readers, linux machine, PVC pipe

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

In setup, set the buad to 96000 and connect the servo to the port.
```arduino
Serial.begin(9600); 
myservo.attach(9);
```
In loop we're checking to see if something came across serial. Then we parse it into an int and use that value to write to our servo.
```arduino
if (Serial.available() > 0) {   // something came across serial
            int integerValue = Serial.parseInt();
            if (integerValue != 0)
              {
              Serial.println(integerValue);
              myservo.write(integerValue);
              }
        }
```

### Connecting RFid sensors with Python

```python
#initialize list of RFidReaders connected to computer
device = list(usb.core.find(find_all=True, idVendor=0x16c0, idProduct = 0x27db))
reader1 = reader.Reader(0x16c0, 0x27db, 36, 3, should_reset=False)
reader2 = reader.Reader(0x16c0, 0x27db, 36, 3, should_reset=False)
```

### Mice Class

In the Mice Class there are 4 main attributes: code, isAllowed, States, and Transitions.

The code in Mice Class is an int value which we will use to compare to the RFid key.

isAllowed is a boolean value used to determine if the mice is allowed to enter the tube.

States is an array holding the state names we will use.
```python
states=['left', 'centerOut', 'right', 'centerIn']
```
transitions is an array holding arrays containing the tigger, source, and destination.
```python
transitions = [
        {'trigger': 'leftToCenter', 'source': 'left', 'dest': 'center'},
        {'trigger': 'centerToRight', 'source': 'center', 'dest': 'right'},
        {'trigger': 'rightToCenter', 'source': 'right', 'dest': 'center'},
        {'trigger': 'centerToLeft', 'source': 'center', 'dest': 'left'}
]
```

### Running the main file: MiceDetector.py

Open the terminal and cd to folder with all the files.

```terminal
sudo python MiceDetector.py
```
