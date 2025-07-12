auction = {}

print('Thanks for Choosing blind auction')

another_guest = True


while another_guest == True:
    name = input('Please Enter you name for the auction: ')
    amount = int(input('Please enter the amount you want to bid on: '))
    auction[name] = amount;
    ask = input('Any other bidder? yes or no')
    print('\n'*100)
    if ask == 'no':
        break;

bid_amt = 0
name = ''

for key in auction:
    if auction[key]>bid_amt:
        bid_amt = auction[key]
        name = key

print(f'the auction is won by{name} and the amount is {bid_amt}')
#print(auction)


