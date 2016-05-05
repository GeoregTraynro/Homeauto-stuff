# Import the required module. 
import RPi.GPIO as GPIO
from lcd1602 import LCD1602
from time import sleep

lcd = LCD1602() 
# Set the mode of numbering the pins. 
GPIO.setmode(GPIO.BCM) 
# GPIO pin 10 is the output. 
GPIO.setup(13, GPIO.OUT) 
#GPIO pin 8 is the input. 
GPIO.setup(6, GPIO.IN) 
# Initialise GPIO10 to high (true) so that the LED is off. 
GPIO.output(13, False) 
while 1: 
    if GPIO.input(6): 
        GPIO.output( 13, True)
        lcd.lcd_string("LED 1:",lcd.LCD_LINE_1)
        lcd.lcd_string("ON",lcd.LCD_LINE_2)

        sleep(3)

        lcd.cleanup() 
    else: 
        # When the button switch is not pressed, turn off the LED. 
        GPIO.output( 13, False)







