class Solution():
	def isValid(s: str) -> bool:
		hashMap = {'(':')', '{':'}', '[':']'}
		stack = []
		for char in s:
			if char in hashMap:
				stack.append(char)
			else:
				if len(stack) == 0:
					return False
				if hashMap[stack.pop()] != char:
					return False
		if len(stack) != 0:
			return False
		return True

s = "()"
# s = "(){}[]"
# s = "(]"
# s = "[{()}]"
# s = "[[["
# s = ")))"

print(Solution.isValid(s))