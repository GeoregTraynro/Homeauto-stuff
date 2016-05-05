import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)

def RCtime (PiPin):
  measurement = 0
  
  GPIO.setup(PiPin, GPIO.OUT)
  GPIO.output(PiPin, GPIO.LOW)
  time.sleep(0.1)

  GPIO.setup(PiPin, GPIO.IN)
  

  while (GPIO.input(PiPin) == GPIO.LOW):
    measurement += 1

  return measurement

while True:
  print RCtime(35)
  GPIO.setup(17, GPIO.OUT)
  if RCtime(35) > 600:
      GPIO.output(17, True)
  else:
      GPIO.output(17, False)


