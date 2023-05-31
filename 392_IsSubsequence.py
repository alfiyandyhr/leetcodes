class Solution():
	def isSubsequence(s: str, t:str) -> bool:
		i, j = 0, 0
		while i < len(s) and j < len(t):
			if s[i] == t[j]:
				i += 1
				j += 1
			else:
				j += 1
		if i == len(s):
			return True
		else:
			return False

s = 'abc'
# s = 'axc'
t = 'ahbgdc'

print(Solution.isSubsequence(s, t))