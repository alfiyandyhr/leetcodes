class Solution():
	def containsDuplicate(nums: list) -> bool:
		dict_map = {}
		for num in nums:
			if num in dict_map:
				return True
			else:
				dict_map[num] = num
		return False

nums = [1,2,3,1]
# nums = [1,2,3,4]
# nums = [1,1,1,3,3,4,3,2,4,2]

print(Solution.containsDuplicate(nums))