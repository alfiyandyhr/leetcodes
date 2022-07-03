class Solution:
	def twoSum(self, nums, target):
		dict_map = {} # keys: elements in nums, values: indices
		for i, val in enumerate(nums):
			diff = target - val
			print(f'i={i}, val={val}, diff={diff}')
			if diff in dict_map:
				return [i, dict_map[diff]]
			else:
				dict_map[val] = i
			print(f'dict_map={dict_map}')
		return []

# a = {0:1}
# b = 0
# print(b in a)
nums = [2,7,4,9]
target = 13
ans = Solution().twoSum(nums,target)
print(ans)