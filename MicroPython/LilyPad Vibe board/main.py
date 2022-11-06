#Pico 

from machine import Pin
import time

button = Pin(8, Pin.IN)
vibe = Pin(2, Pin.OUT)

while True:
    
    buttonCheck = button.value()
    
    if buttonCheck == True:
        vibe.value(1)
        time.sleep(60)
        
        
    else:
        vibe.value(0)