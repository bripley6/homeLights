"""functions for momentary button presses for activiating wirless remote"""
import time
import pigpio
     

pi = pigpio.pi()
buttonPins = [20, 26, 16, 19] # in order from bottom of remote to top button
# remote, upside down, pins from left to right [3v, 4, 3, 2, 1, gnd]
# cable connector, pins from left to right [13, 19, 16, 26, 20, gnd]

"""def initializeButtons:
    #Initializes the button pins as outputs. Must be called before pressButton.
    for pin in buttonPins:
        pi.set_mode(pin, pigpio.OUTPUT)
"""

def pressButton(button):
    """Momentarily "presses" a button to activate it. Leave it in input mode to not drive over 3.3v"""
    if (button >= len(buttonPins) or button < 0):
        print "Button " + button + " is not a valid button."
        return -1
    
    pi.set_mode(buttonPins[button], pigpio.OUTPUT)
    time.sleep(.1)    
    pi.write(buttonPins[button],0)
    time.sleep(.3)
    pi.write(buttonPins[button],1)
    pi.set_mode(buttonPins[button], pigpio.INPUT)    