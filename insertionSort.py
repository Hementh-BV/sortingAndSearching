def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]

        j = i-1

        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key

    return arr

arr = [34,43,19,15,20,54,21]
print(insertion_sort(arr))
