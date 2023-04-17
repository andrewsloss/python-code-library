import random

random_num = int(random.random() * 100)

num_guesses = 0

while(True):
    guess = int(input('Enter a number between 0 and 100: '))
    num_guesses += 1
    if guess == random_num:
        print('Good job the number was ' + str(random_num) + '!')
        break
    elif guess > random_num:
        print('Guess Lower!')
    elif guess < random_num:
        print('Guess Higher!')
        
print('It took you ' + str(num_guesses) + ' guesses!')