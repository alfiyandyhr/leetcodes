class Solution():
	def removeDuplicates(nums: list) -> int:
		dict_map = {}
		i = 0
		while i < len(nums):
			if nums[i] in dict_map:
				nums.pop(i)
			else:
				dict_map[nums[i]] = i
				i += 1
		return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]

print(Solution.removeDuplicates(nums))