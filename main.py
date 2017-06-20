import usb

from keyboard_alike import reader

readerCurr = readerCurr.Reader(0x16C0, 0x27DB, 84, 16, should_reset=True)

readerCurr.initialize()
print(readerCurr.read().strip())
                       
readerCurr.disconnect()
