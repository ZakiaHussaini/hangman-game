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

    def get_user_input(self):
        user_input = input('\nPlease type a letter: ')
        return user_input

    def play(self):
        """
        this method prompt the user for a letter and plays the game until
        the user guesses the word or lose his attempts
        
        """
        while self.wrong_attempts <= len(HANGMAN):
            self.print_game_status()
            user_input = self.get_user_input()

            # Validate the user input
            if self.is_invalid_letter(user_input):
                print('¡The input is not a letter!')
                continue
            # Check if the letter is not already guessed
            if user_input in self.game_completion:
                print('You already have guessed that letter')
                continue

            if user_input in self.guess:
                indexes = self.find_indexes(user_input)
                self.update_progress(user_input, indexes)
                # If there is no letter to find in the word
                if self.game_completion.count('_') == 0:
                    print('\nCongrats, you guessed the word! You win!')
                    print('The word is: {0}'.format(self.guess))
                    quit()
            else:
                self.wrong_attempts += 1
        print("\nOMG! You lost!")
        print('The word is: {0}'.format(self.guess))


    

