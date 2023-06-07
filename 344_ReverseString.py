class Solution():
	def reverseString(s: list) -> None:
		"""
		Reverse a string, modifiy in-place
		"""
		i = 0
		j = len(s)-1
		while i < j:
			tmp = s[i]
			s[i] = s[j]
			s[j] = tmp
			i += 1
			j -= 1

s = ['h','e','l','l','o']
# s = ['H','a','n','n','a','h']

Solution.reverseString(s)

print(s)