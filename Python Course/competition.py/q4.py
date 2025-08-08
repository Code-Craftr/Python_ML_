import random

print('Welcome to random character replacer: ')

word = input('Enter the word: ');

length = int(len(word))

word[2] = "*"

# random_word = random.randint(1, length)
# print(random_word)

print(word)
