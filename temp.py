import time
import RPi.GPIO as GPIO

#LCD IMPORT
from lcd1602 import LCD1602
from time import sleep
#LCD 
lcd = LCD1602()

GPIO.setmode(GPIO.BCM)

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
        print light_level(19)
        if light_level(19) > 40000:
                lcd.lcd_string("FAN:",lcd.LCD_LINE_1)
                lcd.lcd_string("ON",lcd.LCD_LINE_2)
        else:
                lcd.lcd_string("FAN:",lcd.LCD_LINE_1)
                lcd.lcd_string("OFF",lcd.LCD_LINE_2)



