def getFloorAndCeil(arr, n, x):
    high = 100000000
    low = 0
    lc = 0
    hc = 100000000000
    for i in range(n):
        if arr[i] <= x:
            lc = arr[i]
        if arr[i] >= x:
            hc = arr[i]
        low = max(low, lc)
        high = min(high, hc)

    if low == 0:
        return -1, high
    elif high == 100000000:
        return low, -1
    else:
        return low, high


def getFloorAndCeil(arr, n, x):
    # code here
    arr.sort()
    low, high = 0, n - 1
    floor = -1
    ceil = -1
    while (low <= high):
        mid = (low + high) // 2

        if (arr[mid] == x):
            return [x, x]
        elif (arr[mid] > x):
            ceil = arr[mid]
            high = mid - 1
        else:
            floor = arr[mid]
            low = mid + 1
    return [floor, ceil]
