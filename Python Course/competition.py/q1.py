import random

print('Welcome to the number guessing game')
number = random.randint(1,10)
total_attempt = 0

game = True
while game == True:
    guess = int(input('Please enter the number you have guessed: '))

    if guess>number:
        print('Too High')
        total_attempt +=1
    elif guess<number:
        print('Too Low')
        total_attempt +=1
    elif guess == number:
        print('The number you have entered is Correct')
        game = False
        print(f'The total attempt it took you to guess the number are: {total_attempt}')