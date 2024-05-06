#Excercises for dictionaries

#1

pets = [ 'Reina', {'animal': 'cat' , 'owner': 'Juan Hung'},
        'Milo', {'animal': 'dog', 'owner': 'daniela peralta'},
        'Peluche', {'animal': 'cat', 'owner': 'daniela navarro'}]

for pets, info in enumerate(pets):
    name = info
    if isinstance(info, dict):
        print('Animal: ',info['animal'].title())
        print('Owner: ',info['owner'].title())
        print('\n')
    else:
        print('Name: ',info)

#2

favorite_place = {'Juan': ['Bookstore', 'my bed', "dyana's arms"],
                  'Dyana': ['Bookstore', 'Publix', 'Smoothie king'], 
                  'Brandon': ['My ass', 'my balls', 'my gooch']}
for people, places in favorite_place.items():
    print(f"{people}'s favorite place's include:")
    for place in places:
        print(place.title())
    print('\n')

#3

cities = {'miami': {'country': 'USA',
                    'population': '449514',
                    'fun fact' : 'Miami is a hub for street art.'},
            'rome': {'country': 'italy',
                     'population': '2800000',
                     'fun fact': 'Rome has more fountains than any other city on the planet.'},
            'tokyo': {'country': 'japan',
                      'population': '13900000',
                      'fun fact': 'Tokyo was called Edo for a very long time'}}
for city, facts in cities.items():
    print(city.title(), 'facts:\n')
    for category, info in facts.items():
        print(f'{category.title()}: \t {info.title()}')
    print('\n\n')


#   WHILE LOOPS AND USER INPUT
    # USER INPUT
        #7.1
wanted_Car = input("Please tell me what car you would like: \n")
print(f"\n Let's see if we can find you a {wanted_Car}\n")

        #7.2
dining_Guests = input('How many guests will there be this evening? \n')

dining_Guests = int(dining_Guests)

if dining_Guests > 8:
    print('\nI am sorry but you will have to wait for a table\n')
else:
    print("\nRight this way sir\n")

        #7.3
mod_10 = input("Give me a number and I will tell you if it's divisible by 10:\n")
mod_10 = int(mod_10)
if mod_10 % 10 == 0:
    print(f"\n{mod_10} is divisable by 10\n")
else:
    print(f"\n{mod_10} is not divisable by 10\n")
