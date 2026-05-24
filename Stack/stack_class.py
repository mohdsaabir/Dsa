class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Removed item:", self.items.pop())
    def peek(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            print("Top item:", self.items[-1])
    def is_empty(self):
        return len(self.items) == 0
    def display(self):
        print(self.items)       

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display() 
stack.peek()
stack.pop()
stack.display()