def fibonacci(n):
    # Base cases: F(0) = 0, F(1) = 1
    if n <= 1:
        return n
  
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(4)) 