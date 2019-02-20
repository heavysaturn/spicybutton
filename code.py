from adafruit_circuitplayground.express import cpx
import sound

cpx.pixels.brightness = 0.01

# Play an Am7
sound.play_tone("A4", 0.03)
sound.play_tone("E5", 0.05)
sound.play_tone("Ab5", 0.02)
sound.play_tone("C#6", 0.03)
sound.play_tone("C#6", 0.07)

# COLORS
color = 0x00FF00

while True:
    if cpx.button_a:
        color = 0xFF00FF
        cpx.pixels.fill(color)
        sound.play_tone("A4", 0.5)
        sound.play_tone("F3", 0.5)
    elif cpx.button_b:
        color = 0x00FF00
        cpx.pixels.fill(color)
        cpx.play_file("cat.wav")
    elif cpx.shake(shake_threshold=20):
        color = 0x0000FF
        sound.play_tone("C#", 0.1)
        sound.play_tone("A", 0.1)
        sound.play_tone("Bb", 0.1)
        sound.play_tone("B", 0.1)
        sound.play_tone("C", 0.3)

    cpx.pixels.fill(color)
