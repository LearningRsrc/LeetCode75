from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        diff1 = list(set(nums1) - set(nums2))
        diff2 = list(set(nums2) - set(nums1))
        answer = [diff1, diff2]

        return answer
