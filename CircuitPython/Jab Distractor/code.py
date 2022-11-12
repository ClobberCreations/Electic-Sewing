import board
import digitalio
import time

vibeBoard = digitalio.DigitalInOut(board.A2)
vibeBoard.direction = digitalio.Direction.OUTPUT

while True:
    vibeBoard.value = True
    time.sleep(2)
    vibeBoard.value = False
    time.sleep(2)
    
'''
#Demo code
# Gemma IO demo
# Welcome to CircuitPython 5 :)

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn, AnalogOut
from touchio import TouchIn
import adafruit_dotstar as dotstar
import microcontroller
import board
import time

# One pixel connected internally!
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)

# Built in red LED
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# Analog output on A0
aout = AnalogOut(board.A0)

# Analog input on A1
analog1in = AnalogIn(board.A1)

# Capacitive touch on A2
touch2 = TouchIn(board.A2)

# The keyboard object! Used if we do HID output, see below
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

######################### HELPERS ##############################

# Helper to convert analog input to voltage
def getVoltage(pin):
    return (pin.value * 3.3) / 65536

# Helper to give us a nice color swirl
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0):
        return [0, 0, 0]
    if (pos > 255):
        return [0, 0, 0]
    if (pos < 85):
        return [int(pos * 3), int(255 - (pos*3)), 0]
    elif (pos < 170):
        pos -= 85
        return [int(255 - pos*3), 0, int(pos*3)]
    else:
        pos -= 170
        return [0, int(pos*3), int(255 - pos*3)]

######################### MAIN LOOP ##############################

i = 0
while True:
  # spin internal LED around!
  dot[0] = wheel(i)
  dot.show()

  # set analog output to 0-3.3V (0-65535 in increments)
  aout.value = i * 256

  # once every 256 ticks, so it doesnt rush by!
  if i == 0:
      # Read analog voltage on A1
      print("A1: %0.2f" % getVoltage(analog1in))
      # Print the temperature
      print("Temp: %0.1f" % microcontroller.cpu.temperature)

  # use A2 as capacitive touch to turn on internal LED
  if touch2.value:
        print("A2 touched!")
        # optional! uncomment below & save to have it sent a keypress
        #keyboard.press(Keycode.A)
        #keyboard.release_all()
  led.value = touch2.value

  i = (i+1) % 256  # run from 0 to 255
'''