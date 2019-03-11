import time
from random import random

import audioio
import board
from adafruit_circuitplayground.express import cpx

# colors
BLACK = 0x000000
BLUE = 0x130663
PURPLE = 0x500082
PINK = 0x910046

COLORS = [
    BLUE,
    PURPLE,
    PINK
]


def splatter_pixels(wait, colors, clear=False):
    """
    Makes the pixels on the CPX light up in random order.

    If `clear` is set to True, makes the pixels instead
    turn off in random order.

    `colors` should be a list of colors of any length.
    """

    # random.shuffle isn't available for CircuitPy, so
    # we have to shuffle in an old-school way.
    indexes = range(len(cpx.pixels))
    indexes = sorted(indexes, key=lambda x: random())

    # Now we either light up or put out the pixels
    for i in indexes:
        if not clear:
            cpx.pixels[i] = colors[i % len(colors)]
        else:
            cpx.pixels[i] = BLACK
        time.sleep(wait)


def play_file(filename):
    """
    Plays a specified filename, and
    blinks the neopixels in a fun pattern.
    """
    print("Playing file: " + filename)
    wave_file = open(filename, "rb")
    with audioio.WaveFile(wave_file) as wave:
        with audioio.AudioOut(board.A0) as audio:
            audio.play(wave)
            while audio.playing:
                splatter_pixels(.07, COLORS)
            splatter_pixels(.05, COLORS, clear=True)
    print("Finished")
