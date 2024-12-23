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


