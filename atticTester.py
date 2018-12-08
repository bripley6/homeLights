"""Make the leds do flashy fun things"""
import time
from atticUtility import *
     

# create the LED output object
leds = LEDDriver()



while (1): # loop this forever

    print "Pulse on the lights for 1 second"
    leds.pulse(1)

    print "Strobing the lights at 2 Hz"
    leds.strobe(2,.5)
    
    print "Fading on and off 2 times"
    for i in range(2):
        leds.fadeOn(5)
        leds.fadeOff(5)


    print "Progressivly faster pulsing while fading on"
    delay = float(.6)
    for dur in range(25):
        delay = delay/1.2
        leds.led = 100
        leds.update()
        time.sleep(delay)   
        leds.led = 0
        leds.update()
        time.sleep(delay)

    print "Leaving the LEDs on and exiting"
    leds.led = 100
    leds.update()



        

