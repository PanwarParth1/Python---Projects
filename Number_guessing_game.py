# Number Guessing Game

print("Welcome to Number Guessing Game! ")
print("====== Game Rules ======")
print("1. The computer chooses a random number (between 1 to 100)")
print("2. player tries to guess the correct number")
print("3. After each guess, the program gives a hint : \nLower number plese (If your guess is bigger then the number)\nHigher number plese (If your guess is smaller then the number)")
print("4. The player keeps guessing until they find the correct number")

import random
Attampt=0
random_number=random.randint(1,100)
while(True):
    try:
        user_input=int(input("Enter a number :"))
    except ValueError:
        print("Enter a vaild number!")
        continue

    Attampt += 1
    if user_input == random_number:
        print("Correct!")
        break
    elif user_input > random_number:
        print("Lower number plese!")
    elif user_input < random_number:
        print("Higher number plese!")
    else:
        print("Invalid!")
    
print("Number of attamp is :",Attampt)


