"""functions for momentary button presses for activiating Lutron 4-scene wirless remote"""
import time
import pigpio
import logging
     

pi = pigpio.pi()
buttonPins = [20, 26, 16, 19] # in order from bottom of remote to top button
# remote, upside down, pins from left to right [3v, 4, 3, 2, 1, gnd]
# cable connector, pins from left to right [13, 19, 16, 26, 20, gnd]

def initializeButtons():
    """Initializes the button pins as inputs. Must be called before pressButton."""
    for pin in buttonPins:
        pi.set_mode(pin, pigpio.INPUT)
        pi.set_pull_up_down(pin, pigpio.PUD_OFF) #Assures the Pi doesn't overdrive into the remote IC if the battery is dead
        


def pressButton(button):
    """Momentarily "presses" a button to activate it. Leave it in input mode to not drive over 3.3v"""
    if (button >= len(buttonPins) or button < 0):
        logging.warning("Button " + str(button) + " is not a valid button.")
        return -1
    
    if (button == 1):
        # this is quite dim and the lights flicker on, so set to brighter, then back down to avoid flicker
        pi.write(buttonPins[2],0)
        time.sleep(.2)    
        pi.set_mode(buttonPins[2], pigpio.INPUT)
        time.sleep(.3) # wait for the lights to come up
        pi.write(buttonPins[button],0)
        time.sleep(.2)    
        pi.set_mode(buttonPins[button], pigpio.INPUT)
 
    else:    
        pi.write(buttonPins[button],0)
        time.sleep(.2)    
        pi.set_mode(buttonPins[button], pigpio.INPUT)
        
    return 1


if __name__ == "__main__":
    """ If script run from commandline, run a test of each button """
    initializeButtons()
    
    for button in [1, 2, 3, 0]:
        logging.info("Pressing button " + str(button))
        pressButton(button)
        time.sleep(3)
