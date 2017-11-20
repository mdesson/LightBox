import time
from itertools import cycle
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT) # Blue
GPIO.setup(20, GPIO.OUT) # Red
GPIO.setup(24, GPIO.OUT) # Yellow
GPIO.setup(21, GPIO.OUT) # Green
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP) # input command
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP) # cycle command

blue = [1, 0, 0, 0]
red = [0, 1, 0, 0]
yellow = [0, 0, 1, 0]
green = [0, 0, 0, 1]
execute = [1, 1, 1, 1]
clear = [1, 0, 0, 1]
shutdown = [0, 0, 0, 0]

commands = cycle([blue, red, yellow, green, execute, clear, shutdown])
pin_colours = [23, 20, 24, 21]

selection = blue
halt = False

try:
    while halt == False:
        input_command = GPIO.input(12)
        input_cycle = GPIO.input(25)
        if input_cycle == False:
            print("Button pressed!")
            for colour, led in zip(pin_colours, selection):
                print("Inputting: Pin {}, turned {}.".format(colour, led))
                GPIO.output(colour, led)
                selection = next(commands)
                print("Outputting: Pin {}, turned {}.".format(colour, led))
                time.sleep(0.2)

finally:
    GPIO.cleanup()
