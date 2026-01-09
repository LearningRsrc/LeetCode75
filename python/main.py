from maximum_average_subarray import Solution

if __name__ == "__main__":
	print("hello world")
	solution = Solution().maxAvrg([1,12,-5,-6,50,3], 4)
	solution2 = Solution().maxAvrg([5], 1)
	solution3 = Solution().maxAvrg([5,3], 9)
	print(f"Maximum area is: {solution}")
	print(f"Maximum area 3 is: {solution3}")
	print(f"Maximum area 2 is: {solution2}")
