import time

import board
from adafruit_circuitplayground.express import cpx
from digitalio import DigitalInOut, Direction, Pull
import audioio
import neopixel

AUDIOFILE = "electrons.wav"

# Set up the button
button = DigitalInOut(board.A4)
button.direction = Direction.INPUT
button.pull = Pull.UP
#
# # Enable the speaker
# spkrenable = DigitalInOut(board.A0)
# spkrenable.direction = Direction.OUTPUT
# spkrenable.value = True

# Set up pixels
color = 0xFF00FF
#cpx.pixels.brightness = 0.01


def simple_circle(wait):
    PURPLE = (0x10, 0, 0x10)
    BLACK = (0, 0, 0)

    for i in range(len(cpx.pixels)):
        cpx.pixels[i] = PURPLE
        time.sleep(wait)

    for i in range(len(cpx.pixels)):
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
                simple_circle(.05)
                pass
    print("Finished")


while True:
    cpx.pixels.fill(color)

    if not button.value:
        color = 0xFF0000
        play_file("electrons.wav")


    elif cpx.button_b:
        color = 0x00FF00
        cpx.pixels.fill(color)


# # Play an Am7
# sound.play_note("A4", 0.03)
# sound.play_note("E5", 0.05)
# sound.play_note("Ab5", 0.02)
# sound.play_note("C#6", 0.03)
# sound.play_note("C#6", 0.07)
#
# # What pad our button is connected to:

#
# # COLORS
# color = 0x00FF00
#
# while True:
#     if cpx.button_a:
#         color = 0xFF00FF
#         cpx.pixels.fill(color)
#         sound.play_note("A4", 0.5)
#         sound.play_note("F3", 0.5)
#     elif cpx.button_b:
#         color = 0x00FF00
#         cpx.pixels.fill(color)
#         cpx.play_file("cat.wav")
#     elif cpx.shake(shake_threshold=20):
#         color = 0x0000FF
#         sound.play_note("C#", 0.1)
#         sound.play_note("A", 0.1)
#         sound.play_note("Bb", 0.1)
#         sound.play_note("B", 0.1)
#         sound.play_note("C", 0.3)
#     # elif not button.value:
#     #     audio = audioio.AudioOut(board.SPEAKER, open(AUDIOFILE, "rb"))
#     #     audio.play()
#     #     while audio.playing:
#     #         pass   # wait for audio to finish
#
#     cpx.pixels.fill(color)
