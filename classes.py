from adafruit_circuitplayground import cp
class pixel:
    # This function handles the colors of the pixels

    # It works by taking two arguments: the ID of the pixel (0 through 9) and the color you want it to be.
    # Only 4 colors are accepted, as that is all the colors that are necessary for the game to function (traditionally).

    # The four colors are: red, yellow, green, and blue.

    # Example:
    # pixel.color(5, "blue") will set the SIXTH pixel on the CPX board to turn blue.


    def color(pixelID: int, color: str):

        forceLower = (
            color.lower()
        )  # for flexibility, set the string argument to be all lowercase.

        # valid inputs for the color argument are "red", "yellow", "green", "blue"
        colorDict = {
            "red": (255, 0, 0),
            "yellow": (255, 255, 0),
            "green": (0, 255, 0),
            "blue": (0, 150, 255)
        }

        cp.pixels[pixelID] = colorDict[forceLower]

    # Works the same as color(), but doesn't take an input for the pixelID and just sets all pixels to the inputted color.
    # This is good for flashing the board in the case of a win/loss.

    def colorAll(self, color: str):
        forceLower = (
            color.lower()
        )  # for flexibility, set the string argument to be all lowercase.

        # valid inputs for the color argument are "red", "yellow", "green", "blue"
        colorDict = {
            "red": (255, 0, 0),
            "yellow": (255, 255, 0),
            "green": (0, 255, 0),
            "blue": (0, 150, 255)
        }

        cp.pixels.fill(colorDict[forceLower])

    # Exact same as color(), but just uses darker colors. Useful for showing the available colors on the board.

    def colorDark(pixelID: int, color: str):

        forceLower = (
            color.lower()
        )  # for flexibility, set the string argument to be all lowercase.

        # valid inputs for the color argument are "red", "yellow", "green", "blue"
        colorDict = {
            "red": (20, 0, 0),
            "yellow": (20, 20, 0),
            "green": (0, 20, 0),
            "blue": (0, 7, 20)
        }

        cp.pixels[pixelID] = colorDict[forceLower]

    # This function is simple; it just handles turning off pixels.
    # It works by setting their RGB value to (0, 0, 0).

    def off(self, pixelID: int):
        cp.pixels[pixelID] = (0, 0, 0)

    # Similar to off(), but doesn't take any arguments and just turns all the pixels off (sets their RGB value to 0, 0, 0)

    def offAll(self):
        cp.pixels.fill((0, 0, 0))

class audio:
    # Plays a little jig. This is implemented when the switch is turned to the ON position (pushed to the left)
    def on(self):
        cp.play_tone(262, 0.2)
        cp.play_tone(330, 0.2)
        cp.play_tone(392, 0.2)

    # Plays a little jig. This is implemented when the switch is turned to the OFF position (pushed to the right)
    def off(self):
        cp.play_tone(392, 0.2)
        cp.play_tone(330, 0.2)
        cp.play_tone(262, 0.2)

    # Plays a C note. (Red)
    def redTone():
        cp.play_tone(262, 0.3)

    # Plays a D note. (Yellow)
    def yellowTone():
        cp.play_tone(294, 0.3)

    # Plays an E note. (Green)
    def greenTone():
        cp.play_tone(330, 0.3)

    # Plays an F note. (Blue)
    def blueTone():
        cp.play_tone(349, 0.3)

    # Plays a G note. (Other)
    def otherTone(self, duration: float):
        cp.play_tone(392, duration)
