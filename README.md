# ME30-Project
Sec 04
- A simon says game intended for use on a CPX board. Final project for ME30 Lab at SJSU. Made by Kenny, Heidi, and Jairus.

# DEVELOPERS
- Kenny
- Heidi
- Jairus
- (AI was **NOT** used in this project in any capacity.)

# INITIALIZATION
- Upload the 3 .py files (code.py, func.py, classes.py) to your CPX board.
- Run code.py using the CircuitPy option on Mu editor

# GAMEPLAY
- When you first run the code, it will ask for an input in the terminal. Enter a positive non-zero integer. This will be the amount of rounds you want to play.
- You must turn the board "on" via the switch. If the switch is on the right, it is OFF. If the switch is on the left, it is on. A little jingle will play if the board is on and then the Neo-pixels will flash green. The board is capable of starting in the ON position.
- NOTE: Turning the switch back off will play that same jingle backwards and then flash the lights red. The board will then have none of the Neo-pixels illuminated.
- The right button (D5) will start the game.
- The left button (D4) will reset the game.
- If you win the game (see the GOALS section for more details), the board will play a nice-sounding high pitched sound and flash the lights green.
- If at any point an incorrect sequence is entered, the board will play a bad-sounding low pitched sound and flash the lights red. The game will then reset.
- NOTE: Failing the game does not generate a new sequence of colors. You must press RESET (D4) if you wish to play with a new sequence.

# GOALS
- The objective of the game is to repeat the pattern the board displays back into the board.
- The pattern will get longer every round.
- After a certain amount of rounds (The amount of rounds can be changed in code.py), if the user has successfully inputted the correct sequence of colors, then they win the game.
- The user can input colors into the board by touching the sensors near them (**Blue: A1, Red: A2 A3, Green: A4 A5, Yellow: A6 A7** [Note that Blue only uses one touch sensor. This is due to the hardware limitations of the CPX board itself. There may be a workaround, but A0 is not implemented in the code as a valid input for blue.]).
