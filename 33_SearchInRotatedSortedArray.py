class Solution():
	def search(nums:list, target:int) -> int:
		l, r = 0, len(nums)-1

		while l <= r:
			mid = (l+r)//2

			if nums[mid] == target:
				return mid

			# Leftsorted portion
			if nums[mid] >= nums[l]:
				if target > nums[mid] or target < nums[l]:
					l = mid + 1
				else:
					r = mid - 1

			# Righsorted portion
			else:
				if target < nums[mid] or target > nums[r]:
					r = mid - 1
				else:
					l = mid + 1

		return -1

nums = [4,5,6,7,0,1,2]
target = 0

# nums = [4,5,6,7,0,1,2]
# target = 3

# nums = [1]
# target = 0

print(Solution.search(nums, target))