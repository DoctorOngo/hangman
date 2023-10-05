import random

word_list = ['apple', 'banana', 'pineapple', 'kiwi', 'tomato']

print(word_list)

word = random.choice(word_list)

print(word)

guess = input('Enter a Letter: ')

if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops that\'s not a valid input')