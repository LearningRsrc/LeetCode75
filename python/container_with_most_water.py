from typing import List

class Solution:
        def maxArea(self, height: List[int]) -> int:
                n = len(height)
                if n<2: return 2
                if n==2: return min(height[0], height[1])
                answer_bucket = []
                right_pointer = n - 1
                left_pointer = 0
                while(n >= 2):
                        area = min(height[right_pointer], height[left_pointer]) * (n - 1)
                        print(f"N is {n} and area is {area}")
                        print(f"Min is {min(height[right_pointer], height[left_pointer])}")
                        answer_bucket.append(area)
                        if height[right_pointer] < height[left_pointer]:
                                right_pointer -= 1
                        else:
                                left_pointer += 1
                        n -= 1
                return max(answer_bucket)
