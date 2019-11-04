# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:42:26 2019

@author: davidbabbs
"""
#helper code

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """checks if all letters in secret_word have been guessed - if so returns True otherwise returns False"""
    
    for letter in secret_word:
       if letter not in letters_guessed:
           return False
    
    return True
            

def get_guessed_word(secret_word, letters_guessed):
    
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word=""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += " _ "
    
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    available_letters=""
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in letters_guessed:
            available_letters+=letter
    return available_letters


def input_and_validate_guess(warnings_left, guesses_left):
    while True:
        guess=input("please enter a letter: ")
        guess=str.lower(guess)
        if str.isalpha(guess)==True and len(guess)==1:
            break
        else:
            if warnings_left>0:
                warnings_left +=-1
                print ("That wasn't a valid guess. You lose a warning. You now have ", warnings_left,"warnings left")
            else:
                guesses_left +=-1
                print ("That wasn't a valid guess. You lose a guess. You now have ", guesses_left,"guesses left")
    
    return guess, warnings_left, guesses_left    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print ("Welcome to the game Hangman!")
    print ("You need to guess a word that is", str(len(secret_word)), "letters long.")
    print ("""**************************************************
           
    
    """)
    guesses_left=6
    warnings_left=3
    letters_guessed=""
  
    while guesses_left >=1:
        print ("You have", guesses_left, "guesses left")
        print (get_guessed_word(secret_word, letters_guessed))
        print ("Available letters: ", get_available_letters(letters_guessed))
        while True:
            if guesses_left<=0:
                        break
            guess=input("please enter a letter: ")
            guess=str.lower(guess)
            if str.isalpha(guess)==True and len(guess)==1 and guess not in letters_guessed:
                break
            else:
                if guess in letters_guessed:
                    reason = "You have already guessed that letter."
                if str.isalpha(guess)==False:
                    reason = "You must enter a letter of the alphabet."
                if len(guess)>1:
                    reason= "You may only guess 1 letter at a time."
                if warnings_left>0:
                    warnings_left +=-1
                    print ("That wasn't a valid guess.", reason, "You lose a warning. You now have ", warnings_left,"warnings left")
                else:
                    guesses_left +=-1
                    print ("That wasn't a valid guess.", reason, "You lose a guess. You now have ", guesses_left,"guesses left")
        letters_guessed += guess
        if(is_word_guessed(secret_word, letters_guessed))is True:
            print("word guessed!")
            break
        if guess in secret_word:
            print("Good guess!")
        if guess not in secret_word:
            if guess in "aeiou":
                print ("Bad Luck. That vowel is not in my word. Lose 2 guesses.")
                guesses_left +=-2
            else:
                print ("Bad Luck. That consonant is not in my word. Lose 1 guess.")
                guesses_left +=-1
            
    
    if (is_word_guessed(secret_word, letters_guessed))is True:
        print ("Congratualations, you won! The secret word was", secret_word)
        print ("Your score for the game was", len(secret_word)*guesses_left)
    else: print ("""sorry. You've run out of guesses. You've lost. 
                 
    The secret word was""", secret_word, """
    Better Luck next time""")
            
    
secret_word = choose_word(wordlist)
hangman(secret_word)
    
