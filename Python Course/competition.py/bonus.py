import random
uppercase = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
number = ('0123456789')
specialCharacter= ('!@##$%^&*()')
Lowercase = ('abcdefghijklmnopqrstuvwxyz')

print('welcome to random pass generator')

passwo = []
uper = int(input('Enter how manyu upaer case letter you wnat'))
numbeer = int(input('Enter how many nnumber you want'))
specialChara = int(input('Enter the amountof special character you want'))
Lowerca = int(input('Enter the how many lower case you want: '))

for _ in range(0, uper):
    new = random.choice(uppercase)
    passwo.extend(new)

for _ in range(0, numbeer):
    new_num = random.choice(number)
    passwo.extend(new_num)

for _ in range(0, specialChara):
    new_char = random.choice(specialCharacter)
    passwo.extend(new_char)

for _ in range(0, Lowerca):
    new_lower = random.choice(Lowercase)
    passwo.extend(new_lower)

random.shuffle(passwo)

print(passwo)

