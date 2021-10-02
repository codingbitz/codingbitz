user_input = input("Enter the phrase: ")

# split the input and remove the of word to construct the acronym
phrase = user_input.replace("of","").split()

# acronym building

acronym =""

for word in phrase:
    acronym = acronym + word[0].upper()

print(f'Acronym of {user_input} is {acronym}')
