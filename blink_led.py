import Adafruit_BBIO.GPIO as GPIO
// step 1: name and setup your pins
ledTop="P9_12"
ledBottom="P9_11"
GPIO.setup(ledTop,GPIO.OUT)
GPIO.setup(ledBottom,GPIO.OUT)
delay=input("enter time of delay between blinks: )
num=input("how many blinks do you want? ")
from time import sleep //from time library sleep is imported
//looping for blinking purpose(setting voltage high and low)
// here both leds blinks together
for i in range(0,num):
            GPIO.output(ledTop,GPIO.HIGH)
            GPIO.output(ledBottom,GPIO.HIGH)
            sleep(delay)
            GPIO.output(ledTop,GPIO.LOW)
            GPIO.output(ledBottom,GPIO.LOW)
            sleep(delay)
//here led top will blink first and then led bottom
/*  for i in range(0,num):
            GPIO.output(ledTop,GPIO.HIGH)
            sleep(delay)
            GPIO.output(ledTop,GPIO.LOW)
            sleep(delay)
/*  for i in range(0,num):
            GPIO.output(ledBottom,GPIO.HIGH)
            sleep(delay)
            GPIO.output(ledBottom,GPIO.LOW)
            sleep(delay)
            
GPIO.cleanup()            
            
