def merge_sort(arr, low, high, temp):
    if low < high:
        mid = (low+high)//2
        merge_sort(arr, low, mid, temp)
        merge_sort(arr, mid+1, high, temp)
        temp = merge(arr, low, mid, high, temp)
    return arr


def merge(arr, low, mid, high, temp):
    i = low
    j = mid+1
    k = low
    while i <= mid and j <= high:
        if arr[j] < arr[i]:
            temp[k] = arr[j]
            k += 1
            j += 1
        else:
            temp[k] = arr[i]
            k += 1
            i += 1
    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= high:
        temp[k] = arr[j]
        k += 1
        j += 1

    for x in range(low, high+1):
        arr[x] = temp[x]


arr = [6, 4, 1, 9, 8]
temp = [0] * len(arr)
print(merge_sort(arr, 0, len(arr)-1, temp))
