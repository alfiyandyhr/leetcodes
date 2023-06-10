class Solution():
	def maxSubArray(nums:list) -> int:
		# O(n) time, Kadene's algorithm
		best_sum = nums[0]
		curr_sum = 0
		for num in nums:
			if curr_sum < 0:
				curr_sum = 0
			curr_sum += num
			best_sum = max(best_sum, curr_sum)
		return best_sum

	def maxSubArray2(nums:list) -> int:
		# O(n^2) time
		largestSum = float('-inf')

		for i in range(len(nums)):
			# Odd case
			l, r = i, i
			sumVal = 0
			while l >= 0 and r <len(nums):
				if l==r:
					sumVal += nums[l]
				else:
					sumVal += nums[l] + nums[r] 
				largestSum = max(largestSum, sumVal)
				l -= 1
				r += 1

			# Even case
			l, r = i, i + 1
			sumVal = 0
			while l >= 0 and r <len(nums):
				if l==r:
					sumVal += nums[l]
				else:
					sumVal += nums[l] + nums[r] 
				largestSum = max(largestSum, sumVal)
				l -= 1
				r += 1

		return largestSum

	def maxSubArray3(nums:list) -> int:
		# O(n^2*n) time
		largestSum = nums[0]

		for l in range(0,len(nums)):
			for r in range(l,len(nums)):
				subArray = nums[l:r+1]
				sumVal = 0
				for subVal in subArray:
					sumVal += subVal
				largestSum = max(largestSum, sumVal)

		return largestSum


nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1]
# nums = [5,4,-1,7,8]

print(Solution.maxSubArray(nums))
print(Solution.maxSubArray2(nums))
print(Solution.maxSubArray3(nums))