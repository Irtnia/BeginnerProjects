import random

number = random.randint(1, 20)
tries = 0

print('This is the Guessing Game ^_^')
print('Hi there, what is your name? ')
player = input()

print('hello ' + player + ', can you guess the number')

guess = int(input())

while tries <= 7:
    if number > guess:
        print('Your number is too low!' + ' try again')
        guess = int(input())

    elif number < guess:
        print('Your number is too high!' + 'keep going..')
        guess = int(input())

    elif number == guess:
        print('Congratulations, you got it, the number is ' + str(guess) +' and you were able to guess it in just ' + str(tries+1) + ' tries!')
        break
    tries += 1


if number!=guess:
    print("I'm sorry, the number you were looking for was..." + str(number) + ' good luck next time!')


