from typings import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        lSum = 0
        rSum = sum(nums[1:])
        for i in range(length):
            if lSum == rSum:
                return i
            if i + 1 < length:
                lSum += nums[i]
                rSum -= nums[i + 1]
        return -1
