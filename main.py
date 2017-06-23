from keyboard_alike import reader

#by Oliver Chang 6/23/17

reader1 = reader.Reader(0x16c0,  0x27db, 36, 3, should_reset=False)
'''reader2 = reader.Reader(0x16c0,  0x27db, 36, 3, should_reset=False)'''

reader1.initialize()
while True:
	print('The current rfid code is...... ' + str(reader1.read()))
reader1.disconnect()
