name = input("enter ur name: ")
print(f"welcome {name} to this adventure")

ans = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if ans == "left":
    ans = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

    if ans =="swim":
        print(f"u can swim but would be eaten by alligator")
    elif ans == "walk":
        print("u walked lot,ran out of water, lost the game")
    else:
        print("not valid option, u lose")
elif ans =="right":
    ans =input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if ans == "cross":
        ans = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
        if ans == "yes":
            print("u talk to stranger, he give gold, u won")
        elif ans == "no":
            print("u ignore stranger, u lose")
        else:
            print("not valid option, u lose")
    elif ans == "back":
        print("u go back and u lose")
    else:
        print("not valid option u lose")
else:
    print("not valid option,u lose")
print(f"thx for trying {name}")

