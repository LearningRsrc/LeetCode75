from max_number_of_k_sum_pairs import Solution

if __name__ == "__main__":
	print("hello world")
	solution = Solution().maxNumber([1,2,3,4], 5)
	solution2 = Solution().maxNumber([3,1,3,4,3], 6)
	solution3 = Solution().maxNumber([5,4,8,3,7,5,9,4,6], 9)
	print(f"Maximum area is: {solution}")
	print(f"Maximum area 3 is: {solution3}")
	print(f"Maximum area 2 is: {solution2}")
