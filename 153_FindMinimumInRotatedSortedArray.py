class Solution():
	def findMin(nums:list) -> int:
		l, r = 0, len(nums)-1
		minVal = float('inf')

		while l <= r:
			if nums[l] < nums[r]:
				minVal = min(minVal, nums[l])
				break

			# Pivot
			mid = (l+r)//2
			minVal = min(minVal, nums[mid])
			if nums[mid] >= nums[l]:
				l = mid + 1
			else:
				r = mid - 1
		return minVal


nums = [3,4,5,1,2]
# nums = [4,5,6,7,0,1,2]
# nums = [11,13,15,17]

print(Solution.findMin(nums))