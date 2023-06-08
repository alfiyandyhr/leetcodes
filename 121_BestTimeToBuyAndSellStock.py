class Solution():
	def maxProfit(prices:list) -> int:
		# O(n) solution using sliding window technique
		maxReturn = 0
		i = 0
		j = 1
		while j < len(prices):
			if prices[j] < prices[i]:
				i = j
				j = i + 1 
			else:
				gain = prices[j] - prices[i]
				if maxReturn < gain:
					maxReturn = gain
				j += 1
		return maxReturn

	def maxProfitBrute(prices:list) -> int:
		# O(n^2) solution using brute force technique
		maxReturn = 0
		for i in range(0,len(prices)-1):
			for j in range(i+1,len(prices)):
				gain = prices[j] - prices[i]
				if maxReturn < gain:
					maxReturn = gain
		return maxReturn


prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]

print(Solution.maxProfit(prices))
print(Solution.maxProfitBrute(prices))