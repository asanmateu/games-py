# Hangman Game
# -----------------------------------
import random
import string
import sys


WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("\nLoading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    """
    # FILL IN YOUR CODE HERE...
    counter = 0
    for char in secretWord:
        if char in lettersGuessed:
            counter += 1
    return True if counter == len(secretWord) else False


def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """
    # FILL IN YOUR CODE HERE...
    guessedWord = ""
    for char in secretWord:
        if char in lettersGuessed:
            guessedWord += char
        else:
            guessedWord += "_ "
    return guessedWord


def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    # FILL IN YOUR CODE HERE...
    availableLetters = ""
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            availableLetters += letter
    return availableLetters


def hangman(secretWord):
    """
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE...
    remainingGuesses = 8
    lettersGuessed = ""

    # Print welcome message ///
    print(f"Welcome to the game Hangman!\nI am thinking of a word that is {len(secretWord)} letters long.\n")
    print("_" * 50)

    # Start the game:
    while remainingGuesses > 0:
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            playAgain()
            sys.exit()
        else:
            while True:
                print(f"You have {remainingGuesses} guesses")
                print("Available letters:", getAvailableLetters(lettersGuessed))
                guess = input("Please guess a letter: ").lower()
                if guess not in string.ascii_lowercase:
                    print("Please enter a valid available letter : ", getGuessedWord(secretWord, lettersGuessed))
                    print("_" * 50)
                    continue
                if guess in lettersGuessed:
                    print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
                    print("_" * 50)
                    continue
                else:
                    break

            lettersGuessed += guess

            if guess in secretWord:
                print("Good guess: ", getGuessedWord(secretWord, lettersGuessed))
                print("_" * 50)
            elif guess not in secretWord:
                print("Oops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed))
                remainingGuesses -= 1
                print("_" * 50)

    print(f"Sorry, you ran out of guesses. The word was {secretWord}.")
    print("_" * 50)


def playAgain():
    """Allows player to choose if he wants to play again.
    :return: Runs the game again or exits.
    """
    while True:
        ans = input("Do you want to try again? (y/n): ")
        if ans.lower() == "y":
            print("_" * 50)
            wordlist = loadWords()
            secretWord = chooseWord(wordlist).lower()
            hangman(secretWord)
            playAgain()
        elif ans.lower() == "n":
            print("_" * 50)
            print("Have a great day!\n")
            break
        else:
            continue


if __name__ == "__main__":
    wordlist = loadWords()
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
    playAgain()
    sys.exit()
