from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = {}
        for i in range(len(arr)):
            try:
                occurrences[arr[i]] += 1
            except KeyError:
                occurrences[arr[i]] = 1

        values = occurrences.values()
        if len(set(values)) != len(values):
            return False
        return True
