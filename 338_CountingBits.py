class Solution():
	def countBits(n: int) -> list:

		def hammingWeight(i):
			res = 0
			while i != 0:
				res += i % 2
				i = i >> 1
			return res

		retArray = []
		for i in range(n+1):
			retArray.append(hammingWeight(i))

		return retArray

n = 2
# n = 5

print(Solution.countBits(n))