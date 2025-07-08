def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1, -1, -1):
        swapped = False
        for j in range(0, i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


arr = [6, 4, 1, 9, 8]
print(bubble_sort(arr))
