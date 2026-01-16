from typing import  List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        answer = 0
        rows = {}
        n = len(grid)
        for i in range(n):
            rows[i] = grid[i]
        for j in range(n):
            col = list(list(zip(*grid))[j])
            answer += list(rows.values()).count(col)
        return answer 
