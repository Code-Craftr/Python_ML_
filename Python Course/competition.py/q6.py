import random
print('welcome to number guessing game:')

difficulty = int(input('Please enter the difficulty level you hand to have 1 for easy 2 for hard'))

if difficulty == 1:
    lives = 10
elif difficulty == 2:
    lives = 5

number = random.randint(1, 100);

while lives>0:
    Guess = int(input('Enter the number you have gussed: '))
    if Guess>number:
        print('Too High')
        lives-=1
    elif Guess<number:
        print('Too Low')
        lives-=1
    elif Guess == number:
        print('You have guessed the correct number')
        print(f'The lives remaing for you are: {lives}')
