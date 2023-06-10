class Solution():
	def rob(nums:list) -> int:
		rob1, rob2 = 0, 0
		for rob3 in nums:
			tmp = max(rob1+rob3, rob2)
			rob1 = rob2
			rob2 = tmp
		return rob2

	def robRecursive(nums:list) -> int:
		
		def f(array):
			if len(array) == 0:
				return 0
			if len(array) == 1:
				return array[0]

			return max( f([array[0]])+f(array[2:]), f(array[1:]) )

		return f(nums)


nums = [1,2,3,1]
# nums = [2,7,9,3,1]
# nums = [2,1,1,2]

print(Solution.rob(nums))
print(Solution.robRecursive(nums))