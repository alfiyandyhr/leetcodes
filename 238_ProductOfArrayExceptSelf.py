class Solution():
	def productExceptSelf(nums:list) -> list:
		# O(n) time, O(1) space
		pref = 1
		post = 1
		res = [1] + [1] * len(nums) + [1]

		for i in range(len(nums)):
			pref *= nums[i]
			res[i+2] *= pref

		for i in range(len(nums)):
			post *= nums[-(i+1)]
			res[-(i+3)] *= post

		return res[1:-1] 


	def productExceptSelf2(nums:list) -> list:
		# O(n) time, O(n) space
		pref = [1] + [1] * len(nums) + [1]
		post = [1] + [1] * len(nums) + [1]
		for i in range(1,len(nums)+1):
			pref[i] = pref[i-1] * nums[i-1]
			post[len(nums)+1-i] = post[len(nums)+2-i] * nums[len(nums)-i]
		res = []
		for i in range(1,len(nums)+1):
			res.append(pref[i-1]*post[i+1])
		return res

nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]

print(Solution.productExceptSelf(nums))
print(Solution.productExceptSelf2(nums))