import Tkinter
from Tkinter import *
import tkMessageBox

root = Tkinter.Tk()
frame = Frame(root)
frame.pack()
label = Label(frame, text='Mice Detector GUI', fg = 'red')
label.pack(side = TOP)

sensorLabel = Label(root, text = 'RFid Sensors', fg = 'blue')
sensorLabel.pack(side = LEFT)
SensorText = Text(root, height = 4)
SensorText.insert(INSERT,'RFid Sensor 1 status...' + '(show status here)\n')
SensorText.insert(INSERT,'RFid Sensor 2 status...' + '(show status here)\n')
SensorText.pack()

middleFrame = Frame(root)
middleFrame.pack(side = BOTTOM)

code = 'hi'

miceLabel = Label(middleFrame, text = 'Mice states', fg = 'green')
miceLabel.pack(side = LEFT)
MiceText = Text(middleFrame, height = 10)
MiceText.insert(INSERT, 'Mice 1 state: ' + 'home' + '\n' + 'Mice 2 state: ' + 'home' +
 '\n' + 'Mice 3 state: ' + 'home' + '\n')
#MiceText.insert(INSERT, 'Mice 2 state... ' + '(state)\n')
#MiceText.insert(INSERT, 'Mice 3 state... ' + '(state)\n')
MiceText.pack()

path = 'log.txt'

file = open(path, 'r')

message = file.read()

MiceText.insert("1.0", message + '\n')

def task():
	file = open(path, 'r')
	message = file.read()
	file.close
	if(message == '6164996'):
		MiceText.delete("1.0", END)
		MiceText.insert(INSERT, 'Mice 1 state: ' + 'tube' + '\n' + 'Mice 2 state: ' + 'home' +
 		'\n' + 'Mice 3 state: ' + 'home' + '\n')
 	if(message == '12919161'):
 		MiceText.delete("1.0", END)
 		MiceText.insert(INSERT, 'Mice 1 state: ' + 'home' + '\n' + 'Mice 2 state: ' + 'home' +
 		'\n' + 'Mice 3 state: ' + 'tube' + '\n')
 	if(message == '8657565'):
 		MiceText.delete("1.0", END)
 		MiceText.insert(INSERT, 'Mice 1 state: ' + 'home' + '\n' + 'Mice 2 state: ' + 'tube' +
 		'\n' + 'Mice 3 state: ' + 'home' + '\n')
 	if(message == '6164996e'):
 		MiceText.delete("1.0", END)
 		MiceText.insert(INSERT, 'Mice 1 state: ' + 'test place' + '\n' + 'Mice 2 state: ' + 'home' +
 		'\n' + 'Mice 3 state: ' + 'home' + '\n')
 	if(message == '12919161e'):
 		MiceText.delete("1.0", END)
 		MiceText.insert(INSERT, 'Mice 1 state: ' + 'home' + '\n' + 'Mice 2 state: ' + 'home' +
 		'\n' + 'Mice 3 state: ' + 'test place' + '\n')
 	if(message == '8657565e'):
 		MiceText.delete("1.0", END)
 		MiceText.insert(INSERT, 'Mice 1 state: ' + 'home' + '\n' + 'Mice 2 state: ' + 'test place' +
 		'\n' + 'Mice 3 state: ' + 'home' + '\n')
	root.after(1000, task)

#root.after(1000,task)
root.mainloop()