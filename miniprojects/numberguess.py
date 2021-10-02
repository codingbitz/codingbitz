import random as rand

max_range = input("input the no:")

# check if its digit/less than zero

if max_range.isdigit():
    max_range = int(max_range)
    if max_range <=0:
        print("something greater than zero")
        quit()
else:
    print(f"type a no next time")
    quit()
rnd_no = rand.randint(0,max_range)
guess = 0

while True:
    guess+= 1
    usr_guess = input("input ur guess")
    if usr_guess.isdigit():
        usr_guess=int(usr_guess)
    else:
        print(f"enter no next time")
        continue

    if usr_guess == rnd_no:
        print("u guessed it")
        break
    elif usr_guess > rnd_no:
        print(f"no is above the range")
    else:
        print(f"no was less than range")
print("no of correct guesses",guess)
