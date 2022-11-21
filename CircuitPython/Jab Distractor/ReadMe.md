# Jab Distractor

The initial idea came from exploring ways to make Chloe's experience of self injecting her new medicine better. A product on the market claims the benefit of vibration and cold compress to improve the patient experience.

## Lillypad Vibe Board

The vibration motor being used is a sewable electronics friendly breakout board. The Lillypad vibe board can be run from 3 volts to 5 volts. The greater the voltage the more powerful the vibration generated. The Gemma 0 board only has a 3.3 volt output. To improve the strength of the vibration motor we have used a 5V step up board to convert the 3.3V to 5V.

## Gemma 0 Board

The Gemma 0 Board has been selected for the small size of the board and the connection pads make it easy for electric sewing projects. The board is preloaded with Circuit Python.

## code.py

The A2 connection pad has been defined as *vibeBoard* and set as an output. This provides the 3.3V of power as an output.

> vibeBoard = digitalio.DigitalInOut(board.A2)
> vibeBoard.direction = digitalio.Direction.OUTPUT

While the Gemma 0 board is on the vibeBoard is set to True for 60 seconds. After 60 seconds it will pause and activate to notify that 60 seconds has passed.

> vibeBoard.value = True
> time.sleep(60)
> vibeBoard.value = False
> time.sleep(2)
> vibeBoard.value = True
> time.sleep(2)
> vibeBoard.value = False
> time.sleep(2)
