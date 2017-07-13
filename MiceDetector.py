
# coding: utf-8

                ## THis is a notebook for troubleshooting things

1. Will connect to arduino
2. Move the servo motor
3. Check if RFid works......
                
# In[1]:

# Define all of my import....

import serial
import time
from keyboard_alike import reader
import usb.core
import usb.util
from multiprocessing import Process


# In[2]:

#initialize arduino object
arduino = serial.Serial('/dev/ttyACM0', 9600)
#initialize RFidReader1
reader1 = reader.Reader(0x16c0, 0x27db, 36, 3, should_reset=False)
reader2 = reader.Reader(0x16c0, 0x27db, 36, 3, should_reset=False)

#initialize list of RFidReaders connected to computer
device = list(usb.core.find(find_all=True, idVendor=0x16c0, idProduct = 0x27db))

#initialize reader1 to the RFidReader at position 0 in device list

#reader2.initialize(device[1])

#initialize open and close gate values
openGate = 160
closeGate = 70
#initialize empty string for RFid value to be stored in
code1 = ''
code2 = ''


# In[3]:



entries = 0
reader1.initialize(device[0])
while entries <3:
    
    
    code1 = int(reader1.read()) 
    if(code1== 6164996):
        arduino.write(str(openGate))
        time.sleep(2)
        arduino.write(str(closeGate))
        entries+=1
        print 'entered ' + str(entries) + ' times'
        
        
reader1.disconnect()

print 'all Done'


# In[5]:

reader1.disconnect()

