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

lightshow = []
selection = blue
current_selection = selection
halt = False

try:
    for colour, led in zip(pin_colours, selection):
        GPIO.output(colour, led)

    while halt == False:
        input_command = GPIO.input(12)
        input_cycle = GPIO.input(25)
        if input_cycle == False and input_command == True:
            time.sleep(0.2)
            for colour, led in zip(pin_colours, selection):
                GPIO.output(colour, led)

            current_selection = selection
            selection = next(commands)

        elif input_cycle == True and input_command == False:
            time.sleep(0.2)

            if current_selection == blue:
                lightshow.append(blue)

            elif current_selection == red:
                lightshow.append(red)

            elif current_selection == yellow:
                lightshow.append(yellow)

            elif current_selection == green:
                lightshow.append(green)

            elif current_selection == execute:
                print("Lightshow contents: {}".format(lightshow))
                for command in lightshow:
                    for colour, led in zip(pin_colours, command):
                        GPIO.output(colour, led)

            elif current_selection == clear:
                print("Clearing lightshow.")
                lightshow = []

            elif current_selection == shutdown:
                halt = True

            else:
                pass

        else:
            pass

finally:
    GPIO.cleanup()
