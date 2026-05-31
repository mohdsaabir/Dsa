def perm(current,remaining):
    if len(remaining)==0:
        print(current)
        return
    
    for i,v in enumerate(remaining):
        perm(current+v,remaining[:i]+remaining[i+1:])
         
    



s = "abcd"
perm("",s)