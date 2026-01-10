from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = end = answer = winSum = 0
        for i in range(len(nums)):
            end += 1
            answer += 1
            if nums[i] == 1:
                winSum += 1
            else:
                isWindowValid = (end - start - winSum) <= k
                if not isWindowValid:
                    if nums[start] == 1:
                        winSum -= 1
                    start += 1
                    answer -= 1
        return answer
