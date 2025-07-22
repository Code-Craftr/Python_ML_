print('welocome to the coffee machine: ')

milk = 300
water = 200
coffee = 100
Money = 0


def money_giver():
    paise = 0
    print('Please Insert the coins')

    twenties = int(input('How many 20rs coin: '))
    tens = int(input('How many ten 10rs coin: '))
    fives = int(input('How mnay 5rs Coins: '))
    hundreds = int(input('How mnay 100rs Notes: '))


    paise += 20*twenties
    paise += 10*tens
    paise += 5*fives
    paise += 100*hundreds

    return paise



def not_enough_ingridents():
    print('Sorry But not enough Ingridens in the coffee machine to make you coffee, come back later or refill it.')


def Espresso():
    global water, coffee, Money
    if water>= 50 and coffee>= 18:

        money_esp = money_giver()

        if money_esp>=50:
            water = water - 50
            coffee = coffee - 18
            print('Your Espresso is ready')
            money_esp -= 50
            print(f'Here is your change: {money_esp}rs')
            Money+= 50
        else:
            print('Sorry Not Enogh Money Espresso Cost 50 Try again')


    else:
        not_enough_ingridents()

def Latte():
    global water, coffee, Money, milk
    if water>= 200 and coffee>= 24 and milk>=150:

        money_latte = money_giver()

        if money_latte>=150:
            milk = milk-150
            water = water-200
            coffee = coffee-24
            money_latte -= 150
            print('Your Latte is ready Enjoy❤️')
            print(f'Here is your change: {money_latte}')
            Money+= 150

        else:
            print('Sorry Not enough Money Latte cost 150')
    else:
        not_enough_ingridents()


def Cappuccino():
    global water, coffee, Money, milk
    if water>= 250 and coffee>=24 and milk>=100:

        money_capp = money_giver()

        if money_capp >= 99:
            milk -= 100
            coffee -= 24
            water -= 250
            money_capp -= 99
            print('Have a cappuccino😍')
            print(f'Here is your change: {money_capp}')
            Money+= 99

        else:
            print('Not enough Money for cappuccino cost 99')
    else:
        not_enough_ingridents()

def refill():
    global water, coffee, Money, milk
    water = 300
    milk = 200
    coffee = 100

def report():
    print(f'Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: {Money}')

keep_running = True
while keep_running:
    choice = input('Enter what you want to drink Espresso/Latte/Cappuccino: or exit').lower()


    if choice == 'report':
        report()
    elif choice == 'cappuccino':
        Cappuccino()
    elif choice == 'latte':
        Latte()
    elif choice == 'espresso':
        Espresso()
    elif choice == 'refill':
        refill()
    elif choice == 'exit':
        print('thanks for using our coffe machine')
        keep_running = False
    else:
        print('invalid choice')
    



