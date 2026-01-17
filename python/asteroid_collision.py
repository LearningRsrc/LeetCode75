from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = list()
        for i in asteroids:
            stack.append(i)
            
            if i > 0:
                continue
            else:
                for j in range(len(stack)):
                    if len(stack) < 2:
                        break
                    top = stack[-1]
                    second_top = stack[-2]
                    if second_top < 0 or top > 0:
                        break
                    else:
                        abs_current = abs(top)
                        abs_second_top = abs(second_top)
                        if abs_current == abs_second_top:
                            stack.pop()
                            stack.pop()
                        elif abs_current < abs_second_top:
                            stack.pop()
                            break
                        else:
                            stack.pop(-2)
                    
                    
        return list(stack)
        
