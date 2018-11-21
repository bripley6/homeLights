"""Make the leds do flashy fun things"""
import time
import pigpio
from math import *
     

# LED output state object and output update method
class LEDDriver:
    """Led state is set to 0 for off and up to 100 for full brightness"""
    pi = pigpio.pi()
    
    pwmFreq = 100 # limited to certain frquencies, check docs. Lower is higher resolution
    pwmRange = 1000
    
    led = 0
    ledPin = 21 # for Attic LED light control
    r = (pwmRange * log10(2))/(log10(1000))
    
    # set all LEDs signals to outputs
    def __init__(self):
        self.pi.set_PWM_frequency(self.ledPin, self.pwmFreq)
        self.pi.set_PWM_range(self.ledPin, self.pwmRange)
        self.update()
    
    # sets the brightness of all the LEDs to whatever is set in the object
    def update(self):
        pwm = pow (2, (self.led*(1000/100) / self.r)) - 1 # Make the LED output linear
        self.pi.set_PWM_dutycycle(self.ledPin, (self.pwmRange-pwm)) # invert the PWM output for the attic
            
def pulse(duration):
    """Pulse output for the duration, in seconds"""
    leds.led = 100
    leds.update()
    time.sleep(duration)
    leds.led = 0
    leds.update()

def strobe(leds, frequency, dutyCycle):
    for i in range(10):
        leds.led = 100
        leds.update()
        time.sleep(1/float(frequency) * float(dutyCycle))
        leds.led = 0
        leds.update()
        time.sleep(1/float(frequency)*(1-float(dutyCycle)))
    
def _fade(leds, duration, direction):
    """Fade in turn on leds set in ledsActive over the fade duration, from 0.01 to 10s
    direction = 1 is fade on direciton = -1 is fade off"""
    duration = float(duration)
    if (duration == 0 or duration < 0.01):
        stepSize = 1000
    elif duration > 10:
        stepSize = 1
    else:
        stepSize = int(1/duration * 10)
        
    if direction == 1:
        brightnessRange = range (0,1000,stepSize)
    else:
        brightnessRange = range (1000,0,-stepSize)
          
    # loop runs at about 200 steps/second
    for brightness in brightnessRange:
        leds.led = brightness / 10
        leds.update()
        time.sleep(.003)

# consider making these object functions so it's more consistent
def fadeOn(leds, duration):
    """Fade in turn on leds set in ledsActive over the fade duration, from 0.01 to 10s"""
    _fade(leds, duration, 1)

def fadeOff(leds, duration):
    """Fade out turn off leds set in ledsActive over the fade duration, from 0.01 to 10s"""
    _fade(leds, duration, -1)

