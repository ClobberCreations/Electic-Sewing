import time
from machine import Pin, ADC

led = Pin(14, Pin.OUT)
led2 = Pin(15, Pin.OUT)
led3 = Pin(16, Pin.OUT)
touchSensor = ADC(27)

while True:
    reading = touchSensor.read_u16()
    print("ADC: {}".format(reading))
    time.sleep(0.5)
    
    if reading == 65535:
        led.value(1)
        led2.value(0)
        led3.value(0)
        time.sleep(0.2)
        led.value(0)
        led2.value(1)
        led3.value(0)
        time.sleep(0.2)
        led.value(0)
        led2.value(0)
        led3.value(1)
        time.sleep(0.2)
        
    else:
        led.value(0)
        led2.value(0)
        led3.value(0)