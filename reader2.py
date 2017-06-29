from keyboard_alike import reader
import usb.core
import usb.util
import time
#By Oliver Chang 6/23/17

'''Current strategy: 
	Let's try making 2 Reader objects. The way we can differentiate that is by using the 		device number.
'''

reader2 = reader.Reader(0x16c0, 0x27db, 36, 3, should_reset=False)

device = list(usb.core.find(find_all=True, idVendor=0x16c0, idProduct = 0x27db))

reader2.initialize(device[1])
file = open("RFID_log2.txt", "w+")

t = time.time()

while (time.time() - t) < 30:
	#file.write(str(reader2.read()))
	print time.time()-t
	#file.write("\n")
	
	print len(reader2.read())
	#file.write(str(reader2.read()))

file.close()

reader2.disconnect()
