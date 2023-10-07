import random

class Hangman:

    #Initialise all class variables
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = None
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    
    # Creates string of _ for each letter in word
    def create_guesses(self, word):
        word_guessed = []
        for i in range(len(word)):
            word_guessed.append('_')
        self.word_guessed = word_guessed
    
    # Checks each valid guess if in word and provides output
    def check_guess(self, guess):
        # Convert guess to lower case
        guess = guess.lower()
        # If guessed letter is in the word
        if guess in self.word:
            print(f'Good guess, {guess} is in the word!')
            # Updates the Guessed Word
            i = 0
            for letter in self.word:
                if guess == letter:
                    self.word_guessed[i] = guess
                i += 1
            # Updates Remaining Letters
            self.num_letters -= 1
        # If guessed letter isn't in the word
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word')
            print(f'You have {self.num_lives} lives left')
    
    # Takes guess input
    def ask_for_input(self):
        # Initialises Guessed Word
        self.create_guesses(self.word)
        while True:
            guess = input('Pick a letter: ')
            if len(guess) != 1 or not guess.isalpha():
                print('Invalid Letter. Please enter a single alphabetical character')
            elif guess in self.list_of_guesses:
                print('You already tried that letter')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
    
game = Hangman(['apple', 'banana'])

game.ask_for_input()
