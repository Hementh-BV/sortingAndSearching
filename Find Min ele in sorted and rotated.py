def findMin(self, arr, n):
    min = 0
    for i in range(1, n):
        if arr[i] < arr[min]:
            min = i
    return arr[min]


# 2) Using Python INBUILD method: -

# return min(arr)
def findMin(self, nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]
