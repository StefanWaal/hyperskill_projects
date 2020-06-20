from random import choice

name = input('Enter your name:')
rating = 0
with open('rating.txt', 'r') as f:
    for line in f:
        line = line.split()
        if line[0] == name:
            rating = int(line[1])
            break
print(f'Hello, {name}')

options = input().split(',')
if options == ['']:
    options = ['rock', 'paper', 'scissors']
halfway = len(options) // 2
print("Okay, let's start")

while True:
    player = input()
    if player == '!exit':
        print('Bye!')
        break
    elif player == '!rating':
        print(f'Your rating: {rating}')
    elif player in options:
        index = options.index(player)
        options_comp_win = (options[index + 1:] + options[:index])[:halfway]
        comp = choice(options)
        if player == comp:
            print(f'There is a draw ({comp})')
            rating += 50
        elif comp in options_comp_win:
            print(f'Sorry, but computer chose {comp}')
        else:
            print(f'Well done. Computer chose {comp} and failed')
            rating += 100
    else:
        print('Invalid input')
