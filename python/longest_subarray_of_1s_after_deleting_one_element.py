from typings import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = end = answer = winSum = 0
        for i in range(len(nums)):
            end += 1
            answer += 1
            if nums[i] == 1:
                winSum += 1

            isValidWindow = (end - start - winSum) <= 1
            if not isValidWindow:
                if nums[start] == 1:
                    winSum -= 1
                start += 1
                answer -= 1

        return answer - 1
