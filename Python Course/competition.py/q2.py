print('Welcome to the table printer')

number = int(input('please enter the number whose table you want to get printed: '))

for n in range(1, 11):
    print(number*n)
    print('\n')