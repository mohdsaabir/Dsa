def subset(index,current):
    if index == len(s):
        print(current)
        return
    
    subset(index+1,current+s[index])
    subset(index+1,current)

s = "abc"
subset(0,"")