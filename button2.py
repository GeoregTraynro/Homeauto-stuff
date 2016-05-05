import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)#button
GPIO.setwarnings(False)

try:
    while True:
        print(GPIO.input(20))

except KeyboardInterrupt:
    GPIO.cleanup()
