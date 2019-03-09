import time
from random import random, randint

import board
from adafruit_circuitplayground.express import cpx
from digitalio import DigitalInOut, Direction, Pull
import audioio
import neopixel

# audio files
AUDIOFILE = "electrons.wav"

# colors
BLACK = 0x000000
BLUE = 0x130663
PURPLE = 0x500082
PINK = 0x910046

# Set up the button
button = DigitalInOut(board.A4)
button.direction = Direction.INPUT
button.pull = Pull.UP


def fire_circle(wait, clear=False):

    fire = [
        BLUE,
        PURPLE,
        PINK
    ]

    # random.shuffle isn't available for CircuitPy, so
    # we have to shuffle in an old-school way.
    indexes = range(len(cpx.pixels))
    indexes = sorted(indexes, key=lambda x: random())

    for i in indexes:
        if not clear:
            cpx.pixels[i] = fire[i % len(fire)]
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
                fire_circle(.07)
            fire_circle(.05, clear=True)
    print("Finished")


while True:

    if not button.value:
        selection = randint(1, 32)
        filename = "sfx/spicybutton{0}.wav".format(selection)
        play_file("spicybutton1.wav")
