class Solution():
	def rob(nums:list) -> int:

		def maxRob(array):
			rob1, rob2 = 0, 0
			for rob3 in array:
				tmp = max(rob1+rob3, rob2)
				rob1 = rob2
				rob2 = tmp
			return rob2

		if len(nums) == 1:
			return nums[0]

		else:
			return max( maxRob(nums[1:]), maxRob(nums[:-1]) )

nums = [2,3,2]
# nums = [1,2,3]
# nums = [1,2,3,1]

print(Solution.rob(nums))