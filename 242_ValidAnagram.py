class Solution():
	def isAnagram(s:str, t:str) -> bool:
		# O(s+t) time and O(s+t) space
		if len(s) != len(t):
			return False

		mapT = {}
		mapS = {}

		for i in range(len(s)):
			if s[i] in mapS:
				mapS[s[i]] += 1
			else:
				mapS[s[i]] = 1
			if t[i] in mapT:
				mapT[t[i]] += 1
			else:
				mapT[t[i]] = 1

		for key_t in mapT.keys():
			if mapT[key_t] != mapS.get(key_t, 0):
				return False

		# # O(slogs + tlogt) time and O(1) space
		# if sorted(s) == sorted(t):
		# 	return True
		# else:
		# 	return False

		return True

s = 'anagram'
t = 'nagaram'

# s = 'rat'
# s = 'car'

print(Solution.isAnagram(s,t))