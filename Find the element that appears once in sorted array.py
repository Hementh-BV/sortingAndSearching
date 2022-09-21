def findOnce(self, arr: list, n: int):
    ans = 0
    for i in arr:
        ans ^= i
    return ans
