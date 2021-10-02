import random
import array

max_range = 16

digits =['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lcase =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
ucase =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
symbls =['@', '#', '$', '%', '=', ':', '?', '.', '/', '|']
cmbned_list = digits+lcase+ucase+symbls

# pick random character from each
rndm_digit = random.choice(digits)
rndm_lcase = random.choice(lcase)
rndm_ucase = random.choice(ucase)
rndm_symbls = random.choice(symbls)

tmp_pass = rndm_digit+rndm_lcase+rndm_ucase+rndm_symbls

for x in range(max_range-4):
    tmp_pass = tmp_pass +random.choice(cmbned_list)
##    print(tmp_pass)
    # convert into array & shuffle to get uniform pattern
    tmp_pass_lst = array.array('u',tmp_pass)
    random.shuffle(tmp_pass_lst)

final_paswd = ""
for x in tmp_pass_lst:
    final_paswd = final_paswd + x

print(f"final password is {final_paswd}")