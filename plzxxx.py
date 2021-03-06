# Import the required module. 
import RPi.GPIO as GPIO
# Set the mode of numbering the pins. 
GPIO.setmode(GPIO.BCM)
# GPIO pin 10 is the output. 
GPIO.setup(13, GPIO.OUT)
#GPIO pin 8 is the input. 
GPIO.setup(6, GPIO.IN)
# Initialise GPIO10 to high (true) so that the LED is off. 
GPIO.output(13, True)

ledState = False
buttonPressed = False;

while 1:
    if GPIO.input(6): 
         if not buttonPressed: 
            buttonPressed = False
            ledState = not ledState
            GPIO.output(13, ledState)
    else: 
         buttonPressed = False
