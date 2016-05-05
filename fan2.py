import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(16, GPIO.OUT)
GPIO.output(16, GPIO.HIGH)
sleep(30)	# Waits for half a second
GPIO.output(16, GPIO.LOW)

GPIO.cleanup()
