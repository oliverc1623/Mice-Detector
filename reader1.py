from keyboard_alike import reader
import usb.core
import usb.util
#By Oliver Chang 6/23/17

'''Current strategy: 
	Let's try making 2 Reader objects. The way we can differentiate that is by using the 		device number.
'''

reader1 = reader.Reader(0x16c0, 0x27db, 36, 3, should_reset=False)

device = list(usb.core.find(find_all=True, idVendor=0x16c0, idProduct = 0x27db))

reader1.initialize(device[0])

#reader2.initialize()
file = open("RFID_log1.txt", "w")

while True:
	file.write(str(reader1.read()))
	
reader1.disconnect()
file.close()