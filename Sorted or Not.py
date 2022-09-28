def arraySortedOrNot(self, arr, n):
    for i in range(n - 1):
        if arr[i] <= arr[i + 1]:
            continue
        else:
            return 0

    return 1

def arraySortedOrNot(self, arr, n):
        a=arr[:]
        arr.sort()
        return a == arr
