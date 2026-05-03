import random

from randomWords import easyWordlist, mediumWordlist, hardWordlist

def chooseDificulty():
    while True:
        difficulty = input('Enter the difficulty of the word (easy, medium or hard): ').lower()
        if difficulty == "easy":
            return random.choice(easyWordlist)
        elif difficulty == "medium":
            return random.choice(mediumWordlist)
        elif difficulty == "hard":
            return random.choice(hardWordlist)
        else:
            print ('Invalid response please try again')

def hangman (lives):
    if lives == 6:
        print ("-----------------")
        print ("        |       ")
        print ("                ")
        print ("                ")
        print ("                ")

    elif lives == 5:
        print ("-----------------")
        print ("        |       ")
        print ("        O       ")
        print ("                ")
        print ("                ")

    elif lives == 4:
        print ("-----------------")
        print ("        |       ")
        print ("        O       ")
        print ("        |       ")
        print ("                ")

    elif lives == 3:
        print ("-----------------")
        print ("        |       ")
        print ("        O       ")
        print ("       /|       ")
        print ("                ")

    elif lives == 2:
        print ("-----------------")
        print ("        |       ")
        print ("        O       ")
        print ("       /|\\     ")
        print ("                ")

    elif lives == 1:
        print ("-----------------")
        print ("        |       ")
        print ("        O       ")
        print ("       /|\\     ")
        print ("       /        ")
        


lives = 6
guessedLetters = []
guessedWords = []
incorrectLetters = []
correct = False


print('\n--------Welcome to Hangman!--------\n')
word = chooseDificulty()

lettersinWord = '_' * len(word)

print(f'\nYou have {lives} lives left')
print(lettersinWord)

while not correct and lives > 0:
    print('\n')
    hangman(lives)
    guess = input('Enter your guess: ').lower()

    if len(guess) == 1 and guess.isalpha():
        if guess in guessedLetters:
            print(f'You already guessed the letter {guess}')
        elif guess in word:
            print(f'Good job, {guess} is in the word!')
            guessedLetters.append(guess)
            wordAsList = list(lettersinWord)
            for i in range(len(word)):
                if word[i] == guess:
                    wordAsList[i] = guess
            lettersinWord = ''.join(wordAsList)
            if '_' not in lettersinWord:
                correct = True
        else:
            print(f'{guess} is not in the word')
            lives -= 1
            guessedLetters.append(guess)
            incorrectLetters.append(guess)
        
        print(f'Incorrect letters: {incorrectLetters}')

    elif len(guess) == len(word) and guess.isalpha():
        if guess in guessedWords:
            print(f'You already guessed the word {guess}')
        elif guess != word:
            print(f'{guess} is not the word')
            lives -= 1
            guessedWords.append(guess)
        else:
            correct = True
            lettersinWord = word
    else:
        print('Invalid guess, try again')

    print(f'\nYou have {lives} lives left')
    print(lettersinWord)

if correct and lives > 0:
    print(f'Congratulations you guessed the word {word}!')

else:
    print ("-----------------")
    print ("        |       ")
    print ("        O       ")
    print ("       /|\\     ")
    print ("       / \\     ")
    print(f'Sorry you ran out of lives the word was {word}')