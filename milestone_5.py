import random

class Hangman:

    #Initialise all class variables
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)[:-1]
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
            print(self.word_guessed)
        # If guessed letter isn't in the word
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word')
            print(f'You have {self.num_lives} lives left')
    
    # Takes guess input
    def ask_for_input(self):
        # Initialises Guessed Word
        while True:
            guess = input('Pick a letter: ')
            if len(guess) != 1 or not guess.isalpha():
                print('Invalid Letter. Please enter a single alphabetical character')
            elif guess in self.list_of_guesses:
                print('You already tried that letter')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def generate_word_list():
    word_list = []
    with open('wordlist.txt', 'r') as f:
        print('Loading Wordlist...')
        for line in f:
            if 4 < len(line) < 12 and line[:-1].isalpha():
                word_list.append(line)
        print(f'{len(word_list)} total words')
    return word_list

def play_game():
    num_lives = 5
    word_list = generate_word_list()
    game = Hangman(word_list, num_lives)
    game.create_guesses(game.word)
    print(game.word_guessed)
    while True:
        if game.num_lives == 0:
            print(f'You Lost, the word was {game.word}')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations! You have won')
            break

play_game()