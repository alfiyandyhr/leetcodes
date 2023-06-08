class Solution():
	def groupAnagrams(strs: list) -> list:
		# Big O of m*n
		hashMap = {}
		
		for s in strs:
			counterKey = [0] * 26 # a-z
			for c in s:
				counterKey[ord(c)-ord('a')] += 1
			counterKey = tuple(counterKey)
			if counterKey in hashMap:
				hashMap[counterKey].append(s)
			else:
				hashMap[counterKey] = [s]
		
		return list(hashMap.values())

	def groupAnagramsInefficient(strs: list) -> list:
		# Big O of m*n*logn
		answer = []
		while len(strs) != 0:
			i = len(strs)-1
			j = i - 1
			currStr = strs.pop()
			answer.append([currStr])
			# [['bat']]
			while j >= 0:
				if sorted(currStr) == sorted(strs[j]):
					answer[-1].append(strs[j])
					strs.pop(j)
				j -= 1
		return answer


strs = ["eat","tea","tan","ate","nat","bat"]
# strs = [""]
# strs = ["a"]


print(Solution.groupAnagrams(strs))
print(Solution.groupAnagramsInefficient(strs))