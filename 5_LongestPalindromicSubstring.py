class Solution():
	def longestPalindrome(s:str) -> str:
		# O(n^2) time
		ret = ''
		for i in range(len(s)):
			# Odd case
			l, r = i, i
			while l >= 0 and r < len(s) and s[l] == s[r]:
				if len(ret) < len(s[l:r+1]):
					ret = s[l:r+1]
				l -= 1
				r += 1
			# Even case
			l, r = i, i+1
			while l >= 0 and r < len(s) and s[l] == s[r]:
				if len(ret) < len(s[l:r+1]):
					ret = s[l:r+1]
				l -= 1
				r += 1
		return ret

	def longestPalindrome2(s:str) -> str:
		# O(n^2*n) time
		def isPalindrome(x):
			if len(x) == 1:
				return True
			l, r = 0, len(x)-1
			while l < r:
				if x[l] != x[r]:
					return False
				l += 1
				r -= 1
			return True

		ret = ''
		for l in range(len(s)):
			for r in range(len(s)):
				subString = s[l:r+1]
				if isPalindrome(subString) and len(subString)>len(ret):
					ret = subString

		return ret	

s = 'babad'
# s = 'cbbd'

print(Solution.longestPalindrome(s))
print(Solution.longestPalindrome2(s))