from random import randint

import board
from digitalio import DigitalInOut, Direction, Pull
from adafruit_circuitplayground.express import cpx

from utils import play_file

# Play a Dm11
cpx.play_tone(293.66, 0.08)  # D
cpx.play_tone(523.25, 0.05)  # C
cpx.play_tone(783.99, 0.10)  # G

# Set up the button
button = DigitalInOut(board.A4)
button.direction = Direction.INPUT
button.pull = Pull.UP

while True:

    # If the big arcade button is pressed, play the sound effect.
    if not button.value:
        selection = randint(1, 32)
        filename = "sfx/spicybutton{0}.wav".format(selection)
        play_file(filename)
