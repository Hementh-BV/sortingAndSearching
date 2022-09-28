def searchInsertK(self, Arr, N, k):
    if k not in Arr:
        Arr.append(k)
    Arr.sort()
    return Arr.index(k)

# Use binary search to optimize the code

def searchInsertK(self, Arr, N, k):
       # code here
       if k in Arr:
           return Arr.index(k)
       else:
           if Arr[N-1]<k:
               return N
           else:
               for i in Arr:
                   if i>k:
                       return Arr.index(i)


def searchInsert(nums, target):
    if not nums:
        return 0

    for i, num in enumerate(nums):
        if num >= target:
            return i

    return len(nums)

# https://leetcode.com/problems/search-insert-position/discuss/15378/A-fast-and-concise-python-solution-40ms-binary-search
