class Solution():
	def validPalindrome(s:str) -> bool:
		s = ''.join(char for char in s if char.isalnum())
		s = s.lower()

		i = 0
		j = len(s)-1

		while i < j:
			if s[i] != s[j]:
				return False
			i += 1
			j -= 1

		return True

s = "A man, a plan, a canal: Panama"
# s = "race a car"
# s = " "

print(Solution.validPalindrome(s))
