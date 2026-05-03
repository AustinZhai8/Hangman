# Hangman Game

A command-line implementation of the classic Hangman word-guessing game.

## How to Play

1. Run the game:
   ```
   python main.py
   ```

2. Select a difficulty level: **easy**, **medium**, or **hard**

3. Guess letters or try to guess the entire word

4. You have **6 lives** to guess the word correctly

5. Win by guessing all the letters or the complete word before running out of lives

## Game Rules

- Guess one letter at a time, or guess the entire word
- Each incorrect guess costs you one life
- You cannot guess the same letter or word twice
- The game reveals your correct guesses and shows remaining blanks
- Win: Guess the word before losing all 6 lives
- Lose: Run out of lives before guessing the word

## Files

- **main.py** - Main game logic and gameplay loop
- **randomWords.py** - Word lists for each difficulty level:
  - Easy: Simple, short words
  - Medium: Standard vocabulary
  - Hard: Advanced and technical terms

## Requirements

- Python 3.x

## Example Gameplay

```
--------Welcome to Hangman!--------

Enter the difficulty of the word (easy, medium or hard): easy

You have 6 lives left
____

-----------------
        |       
                
                
                

Enter your guess: e
Good job, e is in the word!
Incorrect letters: []

You have 6 lives left
_e__

-----------------
        |       
                
                
                

Enter your guess: a
a is not in the word
Incorrect letters: ['a']

You have 5 lives left
_e__

-----------------
        |       
        O       
                
                

Enter your guess: g
Good job, g is in the word!
Incorrect letters: ['a']

You have 5 lives left
_eg_

-----------------
        |       
        O       
                
                

Enter your guess: g
You already guessed the letter g

Enter your guess: m
Good job, m is in the word!
Incorrect letters: ['a']

You have 5 lives left
meg_

-----------------
        |       
        O       
                
                

Enter your guess: o
Good job, o is in the word!
Incorrect letters: ['a']

You have 5 lives left
mego

Congratulations you guessed the word mego!
```
