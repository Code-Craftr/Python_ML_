import random
import game_data


def pick_random():
    random_pick = random.choice((game_data.data))
    return random_pick    

print('Welcome to the Higher and Lower Game Designed by the Manan: ')
Score = 0

start_game = input('Enter yes to start the game: ')

if start_game == 'yes':
    first_set = pick_random()
    second_set = pick_random()

    gamelost = 1

    while gamelost:
        #if gamelost == 2:
            ##second_set = pick_random()

        print(f' Name: {first_set['name']}\nDescription: {first_set['description']}\nCountry: {first_set['country']}\n')
        print(f'Name: {second_set['name']}\nDescription: {second_set['description']}\nCountry: {second_set['country']}\n')


        choiced = input('Which is higher: Enter A for the first and B for the Second')

        if choiced == 'a' or choiced == 'A':
            if first_set['follower_count']>second_set['follower_count']:
                print('You are correct')
                Score += 1
                gamelost = 2
                second_set = pick_random()
            else:
                print('you lost the game')
                print(Score)
                gamelost = 0
                break
        elif choiced == 'b' or choiced == 'B':
            if second_set['follower_count']>first_set['follower_count']:
                print('You won the game:')
                Score += 1
                gamelost = 2
                first_set = second_set
                second_set = pick_random()
            else:
                print('You lost the game')
                print(f'your score is {Score}')
                gamelost = 0
                break

