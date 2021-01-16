# Project 1: The Game of Hog

![](../demo/CS61A.png)  [UCB CS61A (2020Fall)](https://inst.eecs.berkeley.edu/~cs61a/fa20/) [Project 1 The Game of Hog](https://inst.eecs.berkeley.edu/~cs61a/fa20/proj/hog/)

## Overview

This projects develops a simulator and multiple strategies for the dice game Hog.

**The Game of Hog** is a two-player dice game. Two players take turn to choose some number of dice to roll, up to 10 dices, to gain points. The player who gets at least 100 total points first wins the game.

There are some special rules:

- **Pig Out**. If any of the dice outcomes is a 1, the current player's score for the turn is 1.

- **Free Bacon**. A player who chooses to roll zero dice scores `k+3` points, where `k` is the `n`th digit of pi after the decimal point, and `n` is the total score of their opponent. As a special case, if the opponent's score is `n = 0`, then `k = 3` (the digit of pi before the decimal point).
- **Swine Align**. After points for the turn are added to the current player's score, if both players have a positive score and the Greatest Common Divisor (GCD) of the current player's score and the opponent's score is at least 10, take another turn.

- **Pig Pass**. After points for the turn are added to the current player's score, if the current player's score is lower than the opponent's score and the difference between them is less than 3, the current player takes another turn.

More examples could be found on the project page.

## Project Details

