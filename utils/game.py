import random
"""
Import random
This module provides functions for generating random numbers
"""
class Hangman:
    possible_words = ['becode', 'learning', 'mathematics', 'sessions', 'peace', 'world']
    """
    Class Hangman

    Attributes:
        possible_words : list
            attribute that contains a list of words. Out of these words, one will be selected as 
            the word to find.
        random_word : string
            attribute that contains a words from the possible_words list with function random.choice()
            from the module random
        word_to_find : list
            attribute that contains a list of strings from random_word string.
            Each element is a letter of the word
        lives : int
            attribute that contains the number of lives that the player still has left. It  start at 5
        correctly_guessed_letters : list
            attribute that contains a list of strings where each element will be a letter guessed by the user. 
            At the start,  equal to: `_ _ _ _ _`, with the same number of `_` as the length of the word to find.
        wrongly_guessed_letters : list
            attribute that contains a list of strings where each element will be a 
            letter guessed by the user that is not in the `word_to_find`
        turn_count : int
            attribute that contain the number of turns played by the player.
        error_count : int
            attribute that contains the number of errors made by the player
    """
    def __init__(self):
        """
        Function which ititialis object of class Hangman
        and assign the value to them
        """
        self.random_word = random.choice(Hangman.possible_words) #random for get random word from possible_words
        self.word_to_find = list(self.random_word) #list of strings. Each element is a letter of the word
        self.lives = 5
        self.correctly_guessed_letters = ['_'] * len(self.word_to_find)   #`P _ P _ R`
        self.wrongly_guessed_letters = list() 
        self.turn_count = 0 #number of turns played by the player.
        self.error_count = 0 # number of errors made by the player

    def play(self):
        """
        Contains loops and conditions for a one try in game.
        We use while loop for get correct inside letter
        It should be a single character from english alphabet
        """
        letter = input("Enter a letter ")
        while len(letter) != 1 or letter not in 'abcdefghijklmnopqrstuvwxyz':
            print("Enter just a single letter")
            letter = input("Enter a letter ")
        if letter in self.word_to_find:
            indices = [i for i, x in enumerate(self.word_to_find) if x == letter] #indexes with finding letters
            for index in indices:
                self.correctly_guessed_letters[index] = letter  
        elif letter not in self.word_to_find and letter not in self.wrongly_guessed_letters:
            self.wrongly_guessed_letters.append(letter)
            self.error_count+=1
            self.lives-=1
    
    def start_game(self):
        """
        Contains loops and conditions for start separate game.
        Game will continue until variable lives greater than 0 or until 
        user guessed the word
        """
        print(self.correctly_guessed_letters)
        while True:
            self.play()
            print(f" \ncorrectly guessed letters = {self.correctly_guessed_letters}, \nbad guessed letters = {self.wrongly_guessed_letters}, \nlife = {self.lives}, \nerror count = {self.error_count} \nand turn_count = {self.turn_count}")
            if self.lives == 0:
                self.game_over()
                break
            if "_" not in self.correctly_guessed_letters:
                self.well_played()
                break
            self.turn_count += 1

    def game_over(self):
        """
        Contains action "print "Game over"" for gameower condition
        """
        print("Game over")

    def well_played(self):
        '''
        Contains action print: for well_played condition
        it print current value of variable 
        word_to_find
        turn_count
        error_count
        '''
        print(f"\nYou found the word: {self.word_to_find} \nin {self.turn_count} turns with \n{self.error_count} errors!")
