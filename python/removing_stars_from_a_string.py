from typing import List
from collections import deque

class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque()
        for c in s:
            if c == '*':
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
