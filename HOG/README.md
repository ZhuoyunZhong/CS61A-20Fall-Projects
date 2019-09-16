## The Game of HOG

In this project, a simulator and multiple strategies for the dice game Hog is programmed. The control statements and higher-order functions techniques are used in this project.

#### Game Rules

In Hog, two players alternate turns trying to be the first to end a turn with at least 100 total points. On each turn, the current player chooses some number of dice to roll, up to 10. That player's score for the turn is the sum of the dice outcomes.

To spice up the game, we will play with some special rules: *Pig Out*, *Free Bacon*, *Feral Hogs*, *Swine Swap*. Refer to [Project 1: The Game of Hog](https://cs61a.org/proj/hog/#phase-1-simulator) for more information.

#### Files

- `hog.py`: Implementation of strategies
- `dice.py`: Functions for rolling dice
- `hog_gui.py`: A graphical user interface for Hog
- `ucb.py`: Utility functions for CS 61A
- `images`: A directory of images used by `hog_gui.py`

#### Graphical User Interface

In order to render the graphics, make sure you have Tkinter, Python's main graphics library, installed on your computer. Once you've done that, you can run the GUI from your terminal:

```
python3 hog_gui.py
```

Play against the final strategy with the graphical user interface

```
python3 hog_gui.py -f
```

