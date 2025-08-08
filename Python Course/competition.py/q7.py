print('welocme to the pattern print')

number = int(input('enter the number of time you want to print the pattern'))

counter = 0
for i in range(0, number+1):
    print('*'*i)
    counter +=1 

while counter>0:
    print('*'*counter)
    counter-=1