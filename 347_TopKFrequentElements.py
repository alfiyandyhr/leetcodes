class Solution():
	def topKFrequent(nums:list, k:int) -> list:
		# O(n) time, O(n) space
		counter = {}
		stack = [[] for i in range(len(nums))]

		for num in nums:
			if num in counter:
				counter[num] += 1
			else:
				counter[num] = 1

		for num, freq in counter.items():
			stack[freq-1].append(num)

		answer = []
		while len(answer) != k:
			answer += stack.pop()

		return answer

	def topKFrequent2(nums:list, k:int) -> list:
		# O(nlogn) time, O(n) space
		hashMap = {key: [] for key in range(1,len(nums)+1)}

		nums.sort()

		counter = 1
		for i in range(len(nums)):
			if i != len(nums)-1 and nums[i] == nums[i+1]:
				counter += 1
			else:
				hashMap[counter].append(nums[i])
				counter = 1
		
		answer = []
		i = len(nums)
		while len(answer) != k:
			answer += hashMap[i]
			i -= 1

		return answer



nums = [1,1,1,2,2,3]
k = 2

print(Solution.topKFrequent(nums, k))
print(Solution.topKFrequent2(nums, k))