def sod(n):
    if n==0:
        return 0
    
    return n%10 + sod(n//10)


print(sod(1234))
    