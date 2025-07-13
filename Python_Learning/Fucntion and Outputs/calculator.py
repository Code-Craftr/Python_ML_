def add(a , b):
    return a+b;

def sub(a , b):
    return a-b;

def multiply(a, b):
    return a*b;

def devide(a,b):
    return(a/b);

print(' welcome to my calculator ')

calculate_more = 1
result = 0.0
while calculate_more:
    if calculate_more == 1:
        first_no = float(input('Please enter the first number: '))

    operation = input('+\n-\n*\n/\nPick an operation tu start with:');

    Second_no = float(input('Please enter the second number you want to use: '))

    if operation == '+':
        result = add(first_no, Second_no)
        print(result)
    elif operation == '-':
        result = sub(first_no, Second_no)
        print(result)
    elif operation == '*':
        result = multiply(first_no, Second_no)
        print(result)
    elif operation == '/':
        result = devide(first_no, Second_no)
        print(result)
    else:
        print('Function not supported')

    check = int(input('Do you want to further calculate with the result or leave, enter 2 to calculate with the result and 0 if you want to leave: '))

    if check == 2:
        first_no = result
        calculate_more = 2;
        continue;
    else:
        break;
