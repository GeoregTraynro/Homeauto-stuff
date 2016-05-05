import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(5, GPIO.OUT)
GPIO.output(5, GPIO.HIGH)
sleep(0.5)	# Waits for half a second
GPIO.output(5, GPIO.LOW)

GPIO.cleanup()

