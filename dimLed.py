import Adafruit_BBIO.PWM as PWM
tLED="P9_14"
bLED="P9_22"
PWM.start(tLED, 0, 1000)
PWM.start(bLED, 0, 1000)
num=input("enter number of tests: ")
for i in range(0,num):
    tLED=input("enter brightness level(0-7): ")
    bLED=input("enter brightness level(0-7): ")
// duty cycle=brightness level to the power 2    
    tDC=tLED**2 
    bDC=bLED**2
    if tDC>100:
        tDC=100
    if bDC>100:
        bDC=100
    PWM.set_duty_cycle(tLED, tDC)
    PWM.set_duty_cycle(bLED, bDC)
PWM.stop(tLED)
PWM.stop(bLED)
PWM.cleanup()
