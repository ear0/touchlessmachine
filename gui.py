from tkinter import Tk, Button, Frame, Entry, END
import datetime
from pynput.keyboard import Listener, Key, Events
from gpiozero import Motor
from time import sleep

states = ['FWD', 'BWD', 'STOP']

motor = Motor(forward=4, backward=14)
motor.stop()

def fwd():
    endTime = datetime.datetime.now() + datetime.timedelta(seconds = 5)
    while True:
        if datetime.datetime.now() >= endTime:
            motor.stop()
            break
        else:
            motor.forward()

window = Tk()
window.title('Vending Machine Control')
window.geometry('600x600')
frame = Frame(window)
frame.pack()
button = Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack()
dispense = Button(None, text = 'Press to move motor',
          command = fwd, height = 40, width = 40)
stahp = Button(None, text = 'Shutoff',
               fg = 'red',
               command = motor.stop,
               height = 40, width = 40)
dispense.pack(side = 'right')
stahp.pack(side = 'left')
window.mainloop()
