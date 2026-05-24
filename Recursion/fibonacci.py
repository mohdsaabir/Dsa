def fib(n):
    if n==0:
        print(0)
        return 0
    elif n==1:
        print(1)
        return 1
    
    x = fib(n-1)
    y = fib(n-2)
    print(x + y)
    return x + y

fib(5)