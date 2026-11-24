from adafruit_circuitplayground import cp
from classes import *

# This function handles user touches.
def checkForTouch():
    # If the user touches the blue side
    if cp.touch_A1:
        # Make the lights brighter
        pixel.color(5, "blue")
        pixel.color(6, "blue")
        audio.blueTone()
        resetColors()
        return "blue"

    # If the user touches the red side
    elif cp.touch_A2 or cp.touch_A3:
        pixel.color(8, "red")
        pixel.color(9, "red")
        audio.redTone()
        resetColors()
        return "red"

    # If the user touches the green side
    elif cp.touch_A4 or cp.touch_A5:
        pixel.color(0, "green")
        pixel.color(1, "green")
        audio.greenTone()
        resetColors()
        return "green"

    # If the user touches the yellow side
    elif cp.touch_A6 or cp.touch_A7:
        pixel.color(3, "yellow")
        pixel.color(4, "yellow")
        audio.yellowTone()
        resetColors()
        return "yellow"

    else:
        return "none"

# This function allows the program to play its own colors and tones without user input.
def display(color):
    if color == "red":
        pixel.color(8, "red")
        pixel.color(9, "red")
        audio.redTone()
    elif color == "blue":
        pixel.color(5, "blue")
        pixel.color(6, "blue")
        audio.blueTone()
    elif color == "yellow":
        pixel.color(3, "yellow")
        pixel.color(4, "yellow")
        audio.yellowTone()
    else:
        pixel.color(0, "green")
        pixel.color(1, "green")
        audio.greenTone()
    resetColors()

# Sets all the colors back to dim in case some of them were stuck on bright
def resetColors():
    pixel.colorDark(0, "green")
    pixel.colorDark(1, "green")
    pixel.off(None, 2)
    pixel.colorDark(3, "yellow")
    pixel.colorDark(4, "yellow")
    pixel.colorDark(5, "blue")
    pixel.colorDark(6, "blue")
    pixel.off(None, 7)
    pixel.colorDark(8, "red")
    pixel.colorDark(9, "red")

# runs if the user fails or resets the game.
def fail():
    pixel.colorAll(None, "red")
    cp.play_tone(200, 0.1)
    cp.play_tone(200, 0.3)
    resetColors()

def win():
    pixel.colorAll(None, "green")
    cp.play_tone(520, 0.1)
    cp.play_tone(520, 0.3)
    resetColors()





