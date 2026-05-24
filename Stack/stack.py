

stack = []

def push(item):
    stack.append(item)
def pop():
    if not stack:
        print("Stack is empty")
    else:
        print("Top item:", stack[-1])
def peek():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top item:", stack[-1])
def size():
    print("Stack size:", len(stack))
def display():
    print(stack)


push(1)
push(2)
push(3)
display()
peek()
pop()
display()