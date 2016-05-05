#LCD IMPORT
from lcd1602 import LCD1602
from time import sleep
#LCD 
lcd = LCD1602()
# Import the required module. 
import RPi.GPIO as GPIO
# Set the mode of numbering the pins. 
GPIO.setmode(GPIO.BCM)
# GPIO pin 10 is the output. 
GPIO.setup(10, GPIO.OUT)
# GPIO pin 6 is the output. 
GPIO.setup(6, GPIO.OUT)
#GPIO pin 9 is the input. 
GPIO.setup(9, GPIO.IN)
#GPIO pin 13 is the input. 
GPIO.setup(13, GPIO.IN)
# Initialise GPIO to high (true) so that the LED is off. 
GPIO.output(10, False)
GPIO.output(13, False)
while 1:
    if GPIO.input(9):
        GPIO.output( 10, True)
        lcd.lcd_string("LED 1:",lcd.LCD_LINE_1)
        lcd.lcd_string("ON",lcd.LCD_LINE_2)

        sleep(3)

        lcd.cleanup()

    if GPIO.input(13):
        GPIO.output( 6, True)
        lcd.lcd_string("LED 2:",lcd.LCD_LINE_1)
        lcd.lcd_string("ON",lcd.LCD_LINE_2)

        sleep(3)

        lcd.cleanup()
    else:
        # When the button switch is not pressed, turn off the LED. 
        GPIO.output( 10, False)
        GPIO.output( 6, False)
