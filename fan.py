import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(26, GPIO.IN)
state = GPIO.input(26)
if GPIO.input(26):
    print('Button Pressed')
    sleep(0.2)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, GPIO.HIGH)
    sleep(5)	# Waits for half a second
    GPIO.output(16, GPIO.LOW)

GPIO.cleanup()

