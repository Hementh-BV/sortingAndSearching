def findKRotation(self, arr, n):
    # code here
    return arr.index(min(arr))


def findKRotation(self, arr, n):
    count = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            count += 1
            return count
        else:
            count += 1
    return 0
