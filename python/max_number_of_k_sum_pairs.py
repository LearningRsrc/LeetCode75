from typing import List

class Solution:
        def maxNumber(self, nums: List[int], k: int) -> int:
                n = len(nums)
                if n < 2: return 0
                nums.sort()
                left_pointer = 0
                right_pointer = n - 1
                num_ops = 0
                while left_pointer < right_pointer:
                        sum_pair = nums[left_pointer] + nums[right_pointer]
                        print(f"left: {left_pointer}, right: {right_pointer}")
                        print(f"sum: {sum_pair}, nums of ops: {num_ops}")
                        if sum_pair == k:
                                num_ops += 1
                                left_pointer += 1
                                if left_pointer == right_pointer:
                                        break
                                right_pointer -= 1
                        elif sum_pair < k:
                                left_pointer += 1
                        else:
                                right_pointer -= 1
                return num_ops
