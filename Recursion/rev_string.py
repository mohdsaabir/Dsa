def rev(n):
    if n=="":
        return ""
    
    return n[-1] + rev(n[:-1])


print(rev("Muhammed Sabir"))