"""functions for momentary button presses for activiating wirless remote"""
import time
import pigpio
     

pi = pigpio.pi()
buttonPins = [1, 2, 3, 4] # in order from bottom of remote to top button


def initializeButtons:
    """Initializes the button pins as outputs. Must be called before pressButton."""
    for pin in buttonPins:
        pi.set_mode(pin, pigpio.OUTPUT)


def pressButton(button):
    """Momentarily "presses" a button to activate it."""
    if (button >= len(buttonPins) || button < 0):
        print "Button " + button " is not a valid button."
        return -1
        
    pi.write(buttonPins[button],0)
    time.sleep(.1)
    pi.write(buttonPins[button],1)
    