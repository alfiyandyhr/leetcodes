class Solution():
	def isPalindrome(x: int) -> bool:
		
		if x < 0: return False

		x = str(x)

		if len(x) == 1:
			return True

		# Iterate through chars from start and end
		i, j = 0, len(x)-1
		while i < j:
			if x[i] != x[j]:
				return False
			i += 1
			j -= 1
		return True

x = 121
# x = -121
# x = 10
# x = 1234321

print(Solution.isPalindrome(x))


