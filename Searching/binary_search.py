def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + (high-low) // 2
        if arr[mid] > target:
            high = mid-1
        elif arr[mid] < target:
            low = mid+1
        else:
            return mid+1
    return -1


arr = [1, 2, 3, 10, 15, 16, 17, 18, 29]
print(binary_search(arr,29))
