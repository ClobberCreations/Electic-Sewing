import board
import digitalio
import time

vibeBoard = digitalio.DigitalInOut(board.A2)
vibeBoard.direction = digitalio.Direction.OUTPUT

while True:
    vibeBoard.value = True
    time.sleep(60)
    vibeBoard.value = False
    time.sleep(2)
    vibeBoard.value = True
    time.sleep(2)
    vibeBoard.value = False
    time.sleep(2)
