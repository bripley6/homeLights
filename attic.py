"""Make the leds do flashy fun things"""
import time
from atticUtility import *
     

# create the LED output object
leds = LEDDriver()



while (1): # loop this forever
    strobe(leds, 2,.5)
    
    break
    for i in range(5):
        fadeOn(leds, 5)
        fadeOff(leds, 5)

    break
    # slowly pulse on top and bottom
    delay = float(.6)
    for dur in range(25):
        delay = delay/1.2
        leds.led = 100
        leds.update()
        time.sleep(delay)   
        leds.led = 0
        leds.update()
        time.sleep(delay)

    leds.led = 100
    break


        

