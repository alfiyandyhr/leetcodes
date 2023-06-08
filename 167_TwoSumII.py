class Solution():
	def twoSum(numbers:list, target:int) -> list:
		idx1 = 0
		idx2 = len(numbers)-1
		while idx1 < idx2:
			sumVal = numbers[idx1] + numbers[idx2]
			if sumVal > target:
				idx2 -= 1
			elif sumVal < target:
				idx1 += 1
			else:
				return [idx1+1,idx2+1]

numbers = [2,7,11,15]
target = 9
# numbers = [2,3,4]
# target = 6
# numbers = [-1,0]
# target = -1

print(Solution.twoSum(numbers, target))