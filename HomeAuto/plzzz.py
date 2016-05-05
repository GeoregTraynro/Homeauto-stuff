# Import the required module. 
import RPi.GPIO as GPIO 
# Set the mode of numbering the pins. 
GPIO.setmode(GPIO.BCM) 
# GPIO pin 6 is the output. 
GPIO.setup(6, GPIO.OUT) 
#GPIO pin 12 is the input. 
GPIO.setup(13, GPIO.IN) 
# Initialise GPIO10 to high (true) so that the LED is off. 
GPIO.output(6, False) 
while 1: 
    if GPIO.input(13): 
        GPIO.output( 6, True) 
    else: 
        # When the button switch is not pressed, turn off the LED. 
        GPIO.output( 6, False)
