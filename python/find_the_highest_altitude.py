from typings import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxValue = rollingSum = 0
        for i in range(len(gain)):
            rollingSum += gain[i]
            maxValue = max(maxValue, rollingSum)

        return maxValue
