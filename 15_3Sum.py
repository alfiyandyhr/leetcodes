class Solution():
	def threeSum(nums:list) -> list:
		# Big O of n^2
		answer = []
		nums.sort()

		for k in range(0,len(nums)-2):
			i = k+1
			j = len(nums)-1

			if k != 0 and nums[k] == nums[k-1]:
				continue

			while i < j:
				sumVal = nums[i] + nums[j] + nums[k]
				if sumVal > 0:
					j -= 1
				elif sumVal < 0:
					i += 1
				else:
					answer.append([nums[i],nums[j],nums[k]])
					i += 1
					while nums[i] == nums[i-1] and i < j:
						i += 1

		return answer

	def threeSumBrute(nums:list) -> list:
		# Big O of n^3
		answer = {}
		for i in range(0,len(nums)-2):
			for j in range(i+1,len(nums)-1):
				for k in range(j+1,len(nums)):
					if nums[i] + nums[j] + nums[k] == 0:
						ans = [nums[i],nums[j],nums[k]]
						if tuple(ans) in answer:
							continue
						else:
							answer[tuple(ans)] = ans
		return list(answer.values())

nums = [-1,0,1,2,-1,-4]
# nums = [0,1,1]
# nums = [0,0,0]

print(Solution.threeSum(nums))
print(Solution.threeSumBrute(nums))