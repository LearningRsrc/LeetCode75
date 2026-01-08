from typing import List

class Solution:
	def maxNumber(self, nums: List[int], k: int) -> int:
		n = len(nums)
		nums_copy = list(nums)
		if n < 2: return 0
		i = 0
		num_ops = 0
		while i < n:
			if i == (n - 1): break
			current = nums_copy[i]
			complement = k - current
			print(f"current: {current}, i: {i}, n: {n}")
			if complement in nums_copy[i+1:]:
				nums_copy.remove(current)
				nums_copy.remove(complement)
				n -= 2
				num_ops += 1
			else:
				i += 1
		return num_ops
