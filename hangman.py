import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly choose word from list

    return word 

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #letters used
    return ((word_letters, used_letters, alphabet, word))

lives = 6

(word_letters, used_letters, alphabet, word) = hangman()


#user
while len(word_letters) > 0 and lives > 0:
    # letters used

    print('You have', lives, 'lives left and Your used letters are: ', ' '.join(used_letters))

    # what the current word is
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('current word: ', ' '.join(word_list))

    user_letter = input ('guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters: 
            word_letters.remove(user_letter)

        else:
            lives = lives - 1 #lose a life
            print('letter is not in word')

    elif user_letter in used_letters:
        print('You used this letter already')

    else:
        print('invalid character, try again')

    # arrive here when len(word_letters) == 0 OR lives == 0
    if lives == 0:
        print('You died')
    else:
        print('you guessed the word', word, '!!')



user_input = input('type a letter')
print(user_input)

