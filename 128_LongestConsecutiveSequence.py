class Solution():
	def longestConsecutive(nums:list) -> int:
		# O(n) time, O(n) space
		hashSet = set(nums)

		maxCount = 0
		for num in nums:
			if num - 1 not in hashSet:
				counter = 1
				consecutiveNum = num + 1
				while consecutiveNum in hashSet:
					counter += 1
					consecutiveNum += 1
				maxCount = max(maxCount, counter)
		return maxCount

nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]

print(Solution.longestConsecutive(nums))