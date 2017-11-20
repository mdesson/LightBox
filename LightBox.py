import time
from itertools import cycle
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)

input_command = GPIO.input(12)
input_cycle = GPIO.input(25)

blue = [1,0,0,0]
red = [0,1,0,0]
yellow = [0,0,1,0]
green = [0,0,0,1]
execute = [1,1,1,1]
clear = [1,0,0,1]
shutdown = [0,0,0,0]

commands = cycle([blue, red, yellow, green, execute, clear, shutdown])
selection = blue
halt = False

while halt == False:


GPIO.cleanup()

GPIO.output(i, 1)