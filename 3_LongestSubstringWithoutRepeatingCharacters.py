class Solution:
	def lengthOfLongestSubstring(s:str) -> int:
		if len(s) == 1:
			return 1

		res = 0
		StringList = []

		for char in s:
			if char not in StringList:
				StringList.append(char)
				if res < len(StringList):
					res = len(StringList)
			else:
				idx = StringList.index(char)
				StringList = StringList[idx+1:] + [char]

		return res

s = 'abcabcbb'
# s = 'bbbbb'
# s = 'pwwkew'
# s = 'dvdf'
# s = ' '
# s = 'abcdefg'

print(Solution.lengthOfLongestSubstring(s))