def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i+1
    return -1







arr=[1,4,2,7,8]
target=10
print(linear_search(arr,target))