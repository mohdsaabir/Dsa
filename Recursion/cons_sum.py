def ConsSum(n):
    if n==0:
        return 0
    return n + ConsSum(n-1)


print(ConsSum(5))