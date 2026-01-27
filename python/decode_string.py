import re
import itertools
from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        answer = deque()
        for c in s:
            print(f"Outer loop: {c}, stack before append: {stack}")
            if c != ']':
                stack.append(c)
            else:
                chars =''
                for i in range(len(stack)):
                    print(f"Inner loop: {i}, chars before append: {chars}")
                    char = stack[-1]
                    print(f"Char is: {char}")
                    if char != '[':
                        newChar = stack.pop()
                        chars = newChar + chars
                        print(f"chars after append: {chars}")
                    else:
                        print("Multiplying")
                        match = re.search(r'(\d+){}$'.format(re.escape(char)), ''.join(stack))
                        num = match.group(1)
                        print(f"num: {num}")
                        char_len = len(num)
                        num = int(num)
                        chars *= num
                        print(f"chars after multiply: {chars}")
                        stack.pop()
                        stack = deque(itertools.islice(stack, 0, len(stack) - char_len))
                        print(f"stack after removing number: {stack}")
                        stack.append(chars)
                        print(f"final stack value: {stack}")
                        break
        return ''.join(stack)
