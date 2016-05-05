import RPI.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
led = int(7)
powerinput = int(11)
status = int(1)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(11, GPIO.IN)
while time:
    if GPIO.input(11) == False:
        if status == 0
            GPIO.output(7, False)
            print'off'
            status = 1
            time.sleep(0.3)
            continue
        if status == 1
            GPIO.output(7, true)
            print 'on'
            status = 0
            time.sleep(0.3)
            continue
                    
