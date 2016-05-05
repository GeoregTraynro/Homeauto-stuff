#!/usr/bin env python
import time
import RPi.GPIO as GPIO

from lcd1602 import LCD1602
from time import sleep

lcd = LCD1602()

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)

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
        if light_level(21) > 9000:
                GPIO.output(20 , True)
                lcd.lcd_string("LED:",lcd.LCD_LINE_1)
                lcd.lcd_string("ON",lcd.LCD_LINE_2)

        else:
                GPIO.output(20 , False)
                lcd.lcd_string("LED:",lcd.LCD_LINE_1)
                lcd.lcd_string("OFF",lcd.LCD_LINE_2)

