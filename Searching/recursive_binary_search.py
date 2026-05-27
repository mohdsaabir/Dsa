def binary_search(low,high,a,key):
    # Can use low>high return false and then remaining logic 
    if low<=high:                         
        mid = (low+high)//2
        if a[mid]==key:
            return mid+1
        elif a[mid]<key:
            low = mid+1
        else:
            high = mid-1
        return binary_search(low,high,a,key)
    return False
       

a = [1,2,3,4,5,6]
key = 8
if b:= binary_search(0,len(a)-1,a,key):
    print("Found item at location "+ str(b) )
else:
    print("Item not found")