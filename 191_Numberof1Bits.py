class Solution():
	def hammingWeight(n: int) -> int:
		res = 0
		while n != 0:
			if n % 2 == 1:
				res += 1
			n = n >> 1
		return res

n = 11
# n = 128
# n = 4294967293

print(Solution.hammingWeight(n))