def pal(n):
    if len(n) <= 1:
        print("Palindrome")
        return True

    if n[0] != n[-1]:
        print("Not a Palindrome")
        return False
    
    return pal(n[1:-1])


pal("madam")
pal("hello")
pal("sabir")