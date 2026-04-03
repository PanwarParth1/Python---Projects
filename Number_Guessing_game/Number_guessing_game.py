# Number Guessing Game

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


