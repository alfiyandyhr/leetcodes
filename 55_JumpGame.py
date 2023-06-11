class Solution():
	def canJump(nums:list) -> bool:
		# O(n) time greedy
		furthestIDX = 0

		for i in range(len(nums)):
			IDX = i + nums[i]
			furthestIDX = max(furthestIDX, IDX)
			if furthestIDX < i+1:
				break

		if furthestIDX < len(nums)-1:
			return False
		return True

	def canJump2(nums:list) -> bool:
		# O(n^2) time dynamic programming
		cache = {}
		
		def canReachLastIdx(idx):
			if idx in cache:
				return cache[idx]

			if idx == len(nums)-1:
				return True

			for i in range(nums[idx]):
				if canReachLastIdx(idx + i + 1):
					cache[idx] = True
					return cache[idx]

		if canReachLastIdx(0):
			return True
		return False

nums = [2,3,1,1,4]
# nums = [3,2,1,0,4]

print(Solution.canJump(nums))
print(Solution.canJump2(nums))