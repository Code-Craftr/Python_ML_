def greet_with (name, location):
    print(f'Hello {name}')
    print(f'How is the weather at {location}')

name_in = input('Hello What is your name ')
location_in = input('Where do you live?')

greet_with(name_in, location_in)

greet_with(location='Manhaten', name='Manan')