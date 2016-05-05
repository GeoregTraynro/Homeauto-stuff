import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4, GPIO.OUT)
GPIO.output(4, GPIO.HIGH)
sleep(0.5)	# Waits for half a second
GPIO.output(4, GPIO.LOW)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
state = GPIO.input(26)
while True:    
    if state == False:
        print('Button Pressed')
        time.sleep(0.2)


