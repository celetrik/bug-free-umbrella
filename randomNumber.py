# import random() feature from global module
from sys import argv
import random


 script, player_name = argv

# set secret number range
secret_number = random.randint(1, 20)

print (f"Hello , {player_name}")
print("i'm thinking of a number between 1 and 20")

for guessed_num in range(1, 6):  #set number of tries
    print("Take a guess ")
    guess = [int(input())]

    if guess < secret_number:
        print("Your guess is to low")
    elif guess > secret_number:
        print("your guess is too high")
    else:
        break

if guess == secret_number:
    print("You guessed the right number in" + ( str(guessed_num) ))
else: 
    print("The number was " + ( str(guessed_num) ))



    



