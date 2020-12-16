from pynput.keyboard import Listener, Key, Events
from gpiozero import Motor
from time import sleep

states = ['FWD', 'BWD', 'STOP']

motor = Motor(forward=4, backward=14)
motor.stop()

def move(key):
    state = states[2]
    if key == Key.ctrl:
        if state == 'STOP' or state == 'FWD':
            print("Key pressed: {0}".format(key))
            motor.forward()
        else:
            motor.stop()
            time.sleep(1)
            motor.forward()
            state = states[0]
    elif key == Key.alt:
        if state == 'STOP' or state == 'BWD':
            print("Key pressed: {0}".format(key))
            motor.backward()
        else:
            motor.stop()
            time.sleep(1)
            motor.backward()
            state = states[1]
    elif key == Key.esc:
        print("Key pressed: {0}".format(key))
        motor.stop()
        state = states[2]

with Listener(on_press = move) as listener:
    listener.join()
    
