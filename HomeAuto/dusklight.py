#LCD IMPORT
from lcd1602 import LCD1602
from time import sleep
#LCD 
lcd = LCD1602()
# Import the required module. 
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(26, GPIO.IN)

def light_level(pin):
	level = 0
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)
	time.sleep(0.2)
	GPIO.setup(pin, GPIO.IN)
	while (GPIO.input(pin) == GPIO.LOW):
		level += 1
	return level

while True:
	print light_level(21)
        if light_level(21) > 2500:
                GPIO.output(20 , True)
        
        if GPIO.input(26):
            GPIO.output( 20, True)
            lcd.lcd_string("LED 1:",lcd.LCD_LINE_1)
            lcd.lcd_string("ON",lcd.LCD_LINE_2)

            sleep(3)

            lcd.cleanup()

        else:
                GPIO.output(20 , False)
