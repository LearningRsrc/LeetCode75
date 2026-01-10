from typing import List
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        maxVow = currVow = sum(c in vowels for c in s[:k])
        for i in range(k, len(s)):
            if s[i-k] in vowels:
                currVow -= 1
            if s[i] in vowels:
                currVow += 1

            maxVow = max(currVow,maxVow)
        return maxVow
