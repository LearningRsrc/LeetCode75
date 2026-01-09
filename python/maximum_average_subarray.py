from typing import List

class Solution:
	def maxAvrg(self, nums: List[int], k: int)-> float:
		if len(nums) < k:
			return 0
		averages = []
		i = 0
		while len(nums[i:]) >= k:
			sum_subarray = sum(nums[i:k+1])
			avrg = sum_subarray / k
			averages.append(avrg)
			i += 1
		return max(averages)
