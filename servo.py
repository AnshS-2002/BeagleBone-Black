import Adafruit_BBIO.PWM as PWM
servoPin="P9_14"
PWM.start(servoPin,2,50)
while(1):
        desiredAngle=input("What angle do you want? ")
        dutyCycle=1./18.*desiredAngle+2
        Pwm.set_duty_cycle(servoPin,dutyCycle)

