import time
from machine import Pin, ADC

#LEDs connected to the following pins
led = Pin(14, Pin.OUT)
led2 = Pin(15, Pin.OUT)
led3 = Pin(16, Pin.OUT)

#touch sensors connected to the following pins
touchSensor1 = ADC(26)
touchSensor2 = ADC(27)

#Value required for touch sensor to be seen as active
active = 65535

while True:
    #take readings from the touch sensors
    reading1 = touchSensor1.read_u16()
    reading2 = touchSensor2.read_u16()
    
    time.sleep(0.2)
    
    #Checks to see if both sensors are active
    if reading1 == reading2 == active:
        led.value(1)
        led2.value(1)
        led3.value(1)
        
    #Otherwise is the right sensor active
    elif reading1 == active:
        led.value(1)
        led2.value(0)
        led3.value(0)
    
    #Otherwise is the left sensor active 
    elif reading2 == active:
        led.value(0)
        led2.value(0)
        led3.value(1)
    
    #If neither sensors are active the LEDs are set of off. 
    else: 
        led.value(0)
        led2.value(0)
        led3.value(0)
        