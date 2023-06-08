# This is a guess the number game

import random

print('Hello. What is your name?')
name = input()

print('Well, ', name,'I am thinking of number between 1 and 20.')
secretnumber = random.randint(1,20)

#print(secretnumber)

for guessesTaken in range(1,7):
    print('Take a quess.')
    guess = int(input())
    
    if guess < secretnumber:
        print('Your quess is too low.')
    elif guess > secretnumber:
        print('Your quess is too high.')
    else:
        break; #This condition is for the correct guess!

print('You took ' + str(guessesTaken)+ ' quesses.')

if guess ==  secretnumber:
    print('Good job,' + name + '! You guessed my number in ' + str(secretnumber) + ' guesses')

elif guess !=  secretnumber:
    print('Nope,' + name + '! The number I was thinkig of was ' + str(secretnumber))
