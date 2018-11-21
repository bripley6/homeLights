# Edit line 6 to match your chosen GPIO pin
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
frequency = float(.3) #in Hz, need to use a decimal
dutyCycle = float(0.5) # on time percentage from 0 to 1

for x in range(1):
    GPIO.output(21, GPIO.HIGH)
    time.sleep(1/frequency * (1-dutyCycle))
    GPIO.output(21, GPIO.LOW)
    time.sleep(.1)
    #time.sleep(1/frequency * (dutyCycle))

GPIO.output(21, GPIO.HIGH)
#GPIO.cleanup()
