class Solution():
	def climbStairsFiboIterative(n:int) -> int:
		# O(n) time, O(1) space
		a, b = 1, 1
		counter = 1
		# counter should be larger or equal to n
		while counter < n:
			a = a+b
			b = a+b
			counter += 2
		if n % 2 == 0:
			return a
		else:
			return b

	def climbStairsFiboAppendArray(n:int) -> int:
		# O(n) time, O(n) space
		array = [1,1]
		for i in range(2,n+1):
			array.append(array[i-1] + array[i-2])
		return array.pop()

	def climbStairsBruteRecursiveMemo(n:int) -> int:
		# O(n) time, O(n) space
		def func():
			cache = {}
			# cache = {i:f(i)}
			def f(i):
				if i in cache:
					return cache[i]
				if i == n:
					return 1
				elif i > n:
					return 0
				else:
					cache[i] = f(i+1) + f(i+2)
					return cache[i]
			return f

		ret = func()
		return ret(0)

# Possibility numbers
# 1,1,2,3,5,8,13,21,34,55
# n = 5 --> 8
n = 2
n = 3
n = 5

print(Solution.climbStairsFiboIterative(n))
print(Solution.climbStairsFiboAppendArray(n))
print(Solution.climbStairsBruteRecursiveMemo(n))