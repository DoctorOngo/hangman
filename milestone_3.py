
def ask_for_input():
    # User inputs a letter as a guess
    while True:
        guess = input('Enter a Letter: ')
        # check if guess is valid (must be one alphabetic character)
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print('Invalid Letter. Please input a single alphabetical character')
    check_guess(guess)

def check_guess(guess):
    # Convert guess to lower case
    guess = guess.lower()
    # Check if guess is in the word
    if guess in word:
        print(f'Good guess, {guess} is in the word')
    else:
        print(f'Sorry, {guess} is not in the word')

word = 'apple'
ask_for_input()
