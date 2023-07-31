import Adafruit_BBIO.PWM as PWM
myPWM="P8_13"
PWM.start(myPWM,0,1000) // (pin, original duty cycle, frequency)
for i in range(0,5):
    DC=input("what duty cycle would you like? )
    PWM.set_duty_cycle(myPWM, DC)
PWM.close(myPWM)
PWM.cleanup()

// Duty cycle is the ratio of time a load
   or circuit is ON compared to the time the load or circuit is OFF
