class Solution():
	def maxAreaBrute(height:list) -> int:
		# O(n^2) time, O(1) space
		maxVol = 0
		for i in range(0,len(height)-1):
			for j in range(i+1,len(height)):
				vol = (j-i) * min(height[i], height[j])
				maxVol = max(maxVol, vol)
		return maxVol

	def maxAreaEfficient(height:list) -> int:
		# O(n) time, O(1) space
		maxVol = 0
		l, r = 0, len(height)-1
		while l < r:
			vol = (r-l) * min(height[l], height[r])
			maxVol = max(maxVol, vol)
			if height[l] > height[r]:
				r -= 1
			else:
				l += 1
		return maxVol

height = [1,8,6,2,5,4,8,3,7]
# height = [1,1]

print(Solution.maxAreaBrute(height))
print(Solution.maxAreaEfficient(height))