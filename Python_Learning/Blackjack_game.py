
import random
card = [11, 2,3,4,5,6,7,8,9,10,10,10,10]

def addition_card (listings):
    total = 0;
    for n in listings:
        total += n;
    return total

def extra_card_draw():
    players_card.append(random.choice(card))

def check_result():
    if player_value > computer_value:
        print(f"The computer score is {computer_value}")
        print(f'and you score is {player_value}')
        print('Player Won')
    elif player_value == computer_value:
        print('It is a tie ')
    else:
        print(f'the score of computer is {computer_value}')
        print(f'and your score is {player_value}')
        print('Computer won')
    
play_another_game = True
while play_another_game == True:
    choice = input('Do you want to play the black jack game? type y for yes and n for no');

    if choice == 'y':
        players_card = []
        computer_card = []


        players_card.extend(random.choices(card, k=2))
        computer_card.extend(random.choices(card, k=2))

        player_value = addition_card(players_card)
        computer_value = addition_card(computer_card)

        
    
        print(f' Your cards are: {players_card} and the total is {player_value}')
        print(f' Computers first card is: {computer_card[0]}')

        more_card = True

        while more_card == True:
            Card_want = input('Want an extra card?: type y for yes and N for no: ')
            if Card_want == 'y':
                extra_card_draw();
                player_value = addition_card(players_card)
                print(players_card)
                for cari in players_card:
                    if cari == 11 and player_value>21:
                        index = players_card.index(11)
                        players_card[index] = 1
                    else:
                        continue
                if player_value>21:
                    print('You lost as you value goes above 21')
                    break
            else:
                more_card = False
                check_result()
            #  break

    check_game = input('DO you want to play it again? type y for yes and n for no: ')
    if check_game == 'y':
        continue
    else:
        play_another_game = False

    


    

    
        
        





        # if player_value>=21:
        #     print("You lost the game")
        # else:
        #     print(players_card)



    # while player_value<=21:

    #     
    #     if more_card == 'y':
    #         players_card.append(random.choice(card))
    #         player_value = addition_card(players_card)
    #         if player_value>=21:
    #             print("You lost the game")
    #             break
    #         else:
    #             print(players_card)
    #     

