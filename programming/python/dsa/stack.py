#Creating Stack

def crt_stack():
    stck=[]
    return stck

# Adding items to stack

def push(stck,item):
    stck.append(item)
    print("item pushed to stack" + item)

# removing items froms tack

def chck_empty(stck):
    return len(stck) == 0

def pop(stck):
    if chck_empty(stck):
        return "stack is empty"
    return stck.pop()


stck = crt_stack()
push(stck, str(1))
push(stck, str(2))
print("stack before popping an element: " + str(stck))
print("pop: " + pop(stck))
print("stack after popping an element: " + str(stck))