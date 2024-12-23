'''roll the dice? (y/n): a
Invalid Choice!
roll the dice? (y/n): b
Invalid choice!
Roll the dice? (y/n): y
(5, 2)
Roll the dice? (y/n): Y 
(1,4)
Roll the dice? (y/n): n
Thanks for playing!'''


#Can handle multiple rolls in a loop
#Ask the user to roll the dice?
#If user says yes
#  Generate two random numbers
#  Print Them
#If user says no
#  Print thanks for playing!
#else
#  print invalid choice

import random

while True:

    choice = input("Roll the dice? (y/n):  ").lower()
    if choice ==  'y':
        die1 = (random.randint(1,6))
        die2 = (random.randint(1,6))
        print(f'({die1},{die2})')
    elif choice == 'n':
        print('Thanks for playing!')
        break
    else:
        print('Invalid choice!')

#Modify the program so the user can specify how many dice they want to roll

import random

while True:

    choice = input("Roll the dice? (y/n):  ").lower()
    if choice ==  'y':
        try:
            num_dice = int(input('How many dice would you like to roll? ')) 
            if num_dice < 1:
                print('Please enter a positive number of dice')
                continue

            
            die_roll = [random.randint(1,6) for _ in range(num_dice)]
            print(f'roll {num_dice} dice: {die_roll}')

        except ValueError:
            print('Invalid input! Please enter a number')

    elif choice == 'n':
        print('Thanks for playing!')
        break
    else:
        print('Invalid choice!')


#Add a feature that keeps track of how many times the user has rolled the dice 
#this will require a counter that increments each time the dice are rolled

import random

roll_count = 0

while True:

    choice = input("Roll the dice? (y/n):  ").lower()
    if choice ==  'y':
        try:
            num_dice = int(input('How many dice would you like to roll? ')) 
            if num_dice < 1:
                print('Please enter a positive number of dice')
                continue

            
            die_roll = [random.randint(1,6) for _ in range(num_dice)]
            print(f'roll {num_dice} dice: {die_roll}')

            #increment the rol count
            roll_count += 1

        except ValueError:
            print('Invalid input! Please enter a number')

    elif choice == 'n':
        print('Thanks for playing!')
        print(f'You rolled the dice {roll_count} times')
        break
    else:
        print('Invalid choice!')

