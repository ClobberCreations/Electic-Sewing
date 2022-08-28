from machine import Pin, ADC
import time
#Initialising the pins
led1 = Pin(14, Pin.OUT)
touchSensor = ADC(27)

# while True for an endless loop
while True:
    #takes a reading from ADC pin which will be a number between 0 and 65535
    reading = touchSensor.read_u16() 
    #prints touchsensor reading 
    print("ADC : {}".format(reading))
    #if the touchSensor is pressed down:
    if reading == 65535:
        led1.value(1)
        time.sleep(0.5)
    #else the LED will be off
    else:
        led1.value(0)
        time.sleep(0.5)


