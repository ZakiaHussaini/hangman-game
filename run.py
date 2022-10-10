import random
from words import word_list

menu = """
=========================================================================================================================  
=========================================================================================================================
         |                                                                                                      |
         O              {}    {}    {}{}     {}    {}    {}}}}}    {}      {}    {}{}     {}    {}              O 
         |              {}    {}   {}  {}    {}}}  {}   {}    {}   {}}}  {{{}   {}  {}    {}}}  {}              |                  
        /|\             {}{{}}{}  {}{{}}{}   {} {} {}   {}         {} {{}} {}  {}{{}}{}   {} {} {}             /|\                 
         |              {}    {}  {}    {}   {}  {{{}   {}  {{{{   {}  {}  {}  {}    {}   {}   {{}              |
        / \             {}    {}  {}    {}   {}    {}    {}}}}}    {}      {}  {}    {}   {}    {}             / \                 

=========================================================================================================================  
=========================================================================================================================
   
"""
print(menu)
print("let's play Hangman game!")

HANGMAN = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]


class Hangman():
    """
    The hangman game class and it's methods.
    """

    def __init__(self, guess):
        self.wrong_attempts = 0
        self.guess = guess
        self.game_completion = list('_' * len(self.guess))

    def find_indexes(self, letter):
        """
        this method take a letter and return a list with its index in the 
        word to guess.
        """
        return [i for i, char in enumerate(self.guess) if letter == char]

    def is_invalid_letter(self, input_):
        """
        this method validate the user input to check the input is just a letter
        not number or text with more than 1 char
        """
        return input_.isdigit() or (input_.isalpha() and len(input_) > 1)

    def print_game_status(self):
        """
        this method print blankspaces to word for guessing with remaining 
        attempts and guessed letters
        """
        print('\n')
        print('\n'.join(HANGMAN[:self.wrong_attempts]))
        print('\n')
        print(' '.join(self.game_completion))
    
    def update_progress(self, letter, indexes):
        """
        this method update the game progress with guessed letters

        """
        for index in indexes:
            self.game_completion[index] = letter

