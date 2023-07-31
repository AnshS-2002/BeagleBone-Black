import Adafruit_BBIO.ADC as ADC
from time import sleep
ADC.setup()
analogPin="P9_33"
while(1):
        potVal=ADC.read(analogPin)
        potVolt=potVal*1.8
        print("reading of potentiometer: ",potvalue)
        sleep(0.5)
