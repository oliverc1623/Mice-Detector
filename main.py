from keyboard_alike import reader

reader = reader.Reader(0x16c0,  0x27db, 36, 16, should_reset=False)
reader.initialize()
while True:
	print(reader.read().strip())
reader.disconnect()
