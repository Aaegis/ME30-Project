import time
import random
from func import *
from classes import *
from adafruit_circuitplayground import cp

# This function handles getting user input for the amount of rounds they want to play.
# This function is here instead of in func.py because func.py throws a MemoryError (I'm too full...)
def getRounds():
    while True:
    # If the user enters a non-integer or a value of less than 1 then they will be asked to try again.
        try:
            userNumRounds = int(input("Enter # of rounds: "))
            if userNumRounds <= 0:
                raise Exception("# of rounds must be >0")
            break
        except Exception:
            print("Please enter valid number")
    return userNumRounds

# These are functions that were imported from func.py as well as classses that were imported from classes.py
# A second/third file is necessary because having all the code in one file would result in a memory error due to the sheer size of the file and also because it is more organized.
pixel = pixel()
audio = audio()

# This list will hold the user's inputs
userList = []

# Generate a list of random colors for the game by asking for user input
colorList = []
colors = ("red", "yellow", "green", "blue")
for i in range(getRounds()):
    colorList.append(colors[random.randint(0,3)])

# Output the list for debugging purposes DEBUG ONLY
# print(colorList)

### ALL OF THE FOLLOWING VARIABLES HELP DETERMINE THE GAME-STATE ###

# This status variable only changes when the switch is pushed. It is used for determining when the user turns the device on and off.
status = "off"

# This variable starts as False, and turns to True when the start button (left button) is pushed.
gameStart = False

# This variable determines how far the game should iterate down the list.
level = 0

# Adds a pause feature to the program, so that it doesn't loop infinitely without user input.
pause = False

### GAME LOOP ##
while True:

    # Check to see if the user pressed the start button (left button)
    if cp.button_b and cp.switch:
        gameStart = True
        print("Game Started!")
        audio.otherTone(0.2)
        time.sleep(0.1)
        audio.otherTone(0.4)

    # Reset the game
    if cp.button_a and cp.switch:
        print("Reset!")
        fail()
        gameStart = False
        pause = False
        level = 0
        userList = []
        colorList = []
        colors = ("red", "yellow", "green", "blue")
        for i in range(getRounds()):
            colorList.append(colors[random.randint(0,3)])

    # This runs if the game is started (button B is pressed)
    if gameStart == True and cp.switch and pause == False:
        level += 1
        for i in range(level):
            display(colorList[i])
        pause = True

    # The following code runs if the game is paused (if the game is waiting for a user input)
    if pause:
        userInput = checkForTouch()
        if userInput != "none":
            userList.append(userInput)
            print("Input detected!", userInput)

            # If the lists match, win. If the lists match up to a level, proceed to the next level. If the lists dont match, then fail.
            if userList == colorList:
                pause = False
                print("You win!")
                win()
                gameStart = False
                pause = False
                level = 0
                userList = []

            # If the list equals the list of all the generated colors up to the current level, then execute the following.
            # By executing the following, it "unpauses" the game and allows it to display the next level of colors
            elif userList == colorList[0:level] and len(userList) == len(colorList[0:level]):
                pause = False
                userList = []
                time.sleep(1)

            # If the length of the user's list and the current level list match in length but are not equal, then the user has inputted something wrong and therefore has lost the game.
            elif len(userList) == len(colorList[0:level]) and userList != colorList[0:level] or userInput != colorList[len(userList)-1]:
                print("Oops! You failed!")
                fail()
                gameStart = False
                pause = False
                level = 0
                userList = []

    # Start the game by turning on the switch (left = on, right = off).
    # Plays an audio cue that only runs the first time or if the switch was turned back off.
    if cp.switch and status == "off":
        audio.on()
        for i in range(3):
            pixel.colorAll("green")
            time.sleep(0.1)
            pixel.offAll()
            time.sleep(0.1)
        resetColors()
        status = "on"

    # Turn off the game by turning off the switch (left = on, right = off)
    # Plays an audio cue that only runs the first time or if the switch was turned on.
    elif cp.switch == False:
        if status == "on":
            audio.off()
            for i in range(3):
                pixel.colorAll("red")
                time.sleep(0.1)
                pixel.offAll()
                time.sleep(0.1)
            status = "off"
