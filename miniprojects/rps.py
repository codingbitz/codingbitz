import random as rand

user_wins = 0
comp_wins = 0
options =['rock','paper','scissors']

while True:
    uinput = input("type rock/paper/scissors or q to quit:  ").lower()

    if uinput =='q':
        break
    if uinput not in options:
        continue
    randNum = rand.randint(0,2)
    cpick = options[randNum]
    print("cpick is : ", cpick)

    if uinput=="rock" and cpick =="paper":
        print("u won")
        user_wins +=1

    elif uinput=="paper" and cpick =="scissors":
        print("u won")
        user_wins +=1

    elif uinput=="scissors" and cpick =="rock":
        print("u won")
        user_wins +=1

    else:
        print("u lost")
        comp_wins +=1

print(f"u won {user_wins} times")
print(f"comp won {comp_wins} times")
print("goodBye")

