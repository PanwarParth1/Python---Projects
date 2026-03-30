name = input("Type your name :")
print("Welcome ",name," to this adventure!")

answar = input("You are on a dirt road, it has come to an end and you can go left or right, Which way you like to go? :").lower()
if answar == "left":
    answar = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: :").lower()
    if answar == "swim":
        print("You swam acrross and were eaten by a alligator ")
    elif answar == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")
elif answar == "right":
    answar = input("You come to a bridge, it look wobbly , do you want to cross it or head back(cross/back)? :")
    if answar == "back":
        print("You go back and lose.")
    elif answar == "cross":
        answar = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? :")
        if answar == "yes":
            print("You talk to the stanger and they give you gold. You win. ")
        elif answar == "no":
            print("You ignore hte stranger and they are offended and you.")
        else:
            print("No a valid option. You lose.")
else:
    print("Not a valid option. You lose.")


print("Thank you for trying ", name)