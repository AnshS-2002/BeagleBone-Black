import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
from time import sleep
LED="P9_14"
but1="P9_23"
but2="P9_27"
GPIO.setup(but1,GPIO.IN)
GPIO.setup(but2,GPIO.IN)
PWM.start(LED,0,1000)
BP=0  //buttonpush for brightness
while(1):
        if GPIO.input(but1)
            BP=BP+1
            print ("Button 1 was pressed")
        if GPIO.input(but2)
            BP=BP-1
            print ("Button 2 is pressed")
        if GPIO.input(but1) and GPIO.input(but2)
            break;
        if BP>10:
            BP=10
        if BP<0:
            BP=0
        DC=1.5864**(BP)-1
        PWM.set_duty_cycle(LED,DC)
        sleep(0.2)
print("GoodBye!!try again and press one button at a time")        
        
