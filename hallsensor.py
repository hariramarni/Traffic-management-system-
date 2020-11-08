# First step into learning the uses of the hall effect sensor.
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
hallpin = 2
ledpin = 3
gpio.setup( hallpin, gpio.IN)
gpio.setup(ledpin, gpio.OUT)
gpio.output(ledpin, False)
while True:
    if(gpio.input(hallpin) == False):
        gpio.output(ledpin, True)
        print("magnet detected")
    else:
        gpio.output(ledpin, False)
        print("magnetic field not detected")
