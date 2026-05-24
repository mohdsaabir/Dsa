print("Display from 1 to n")
def display(n):
    if n == 0:
        return
    else:
        display(n-1)
        print(n)

display(5)

print("Display from n to 1")
def displayrev(n):
    if n == 0:
        return
    
    print(n)
    displayrev(n-1)

displayrev(5)