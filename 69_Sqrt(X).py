class Solution:
	def mySqrt(x: int) -> int:
		i = 1
		while i*i <= x:
			i += 1
		return i-1

x = 4
# x = 8
print(Solution.mySqrt(x))