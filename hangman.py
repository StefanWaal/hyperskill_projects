from random import choice
from string import ascii_lowercase


class Hangman:
    """Play the hangman game."""

    word_list = ['python', 'java', 'kotlin', 'javascript']

    def __init__(self):
        self.greeting()
        self.word = None
        self.lives = None
        self.clue = None
        self.letters_guessed = None
        self.menu()

    @staticmethod
    def greeting():
        """Print the greeting."""
        print('H A N G M A N')

    def guess_letter(self):
        """Ask for a letter and handle the input."""
        print()
        print(''.join(self.clue))
        letter = input('Input a letter:')
        if letter in self.letters_guessed:
            print('You already typed this letter')
        elif len(letter) != 1:
            print('You should input a single letter')
        elif letter not in ascii_lowercase:
            print('It is not an ASCII lowercase letter')
        elif letter not in self.word:
            print('No such letter in the word')
            self.lives -= 1
            self.letters_guessed.add(letter)
        else:
            self.letters_guessed.add(letter)
            for index, letter2 in enumerate(self.word):
                if letter == letter2:
                    self.clue[index] = letter

    def play(self):
        """Start the game."""
        self.word = choice(Hangman.word_list)
        self.lives = 8
        self.clue = ['-'] * len(self.word)
        self.letters_guessed = set()
        while True:
            self.guess_letter()
            if self.lives <= 0:
                print('You are hanged!')
                break
            elif self.clue.count('-') == 0:
                print('', self.word, 'You guessed the word!',
                      'You survived!', sep='\n')
                break
    
    def menu(self):
        """Manage the menu."""
        while True:
            inp = input('Type "play" to play the game, "exit" to quit:')
            if inp == 'play':
                self.play()
            elif inp == 'exit':
                break        


Hangman()
