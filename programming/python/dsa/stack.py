"""
Stack Data Structure.
"""
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

myStack = Stack()
myStack.push(1)
print(myStack.get_stack())
myStack.push(2)
print(myStack.get_stack())
myStack.pop()
print(myStack.get_stack())