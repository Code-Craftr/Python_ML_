print('Password Strength Checker')
upperletter = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
numericals = ("1234567890")

numbers = 0
uppercase = 0

password = input('Enter the password: ');

for i in password :
    if i in numericals:
        numbers +=1

for i in password:
    if i in upperletter:
        uppercase+=1
    
length_pass = len(password);


if length_pass>8 and numbers>0 and uppercase>0:
    print('Your password is a strong password')
else:
    print('your password is a weak password')


print(numbers)
print(uppercase)