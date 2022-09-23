def findFloor(self, A, N, X):
    low = 0
    high = N - 1
    if X < A[0]:
        return -1

    while low <= high:
        mid = (low + high) // 2
        if A[mid] == X:
            return mid
        elif A[mid] > X:
            high = mid - 1
        else:
            low = mid + 1
    return high
