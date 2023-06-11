class Solution():
	def insert(intervals:list, newInterval:list) -> list:
		res = []

		for i in range(len(intervals)):
			if newInterval[1] < intervals[i][0]:
				res.append(newInterval)
				res += intervals[i:]
				return res
			elif newInterval[0] > intervals[i][1]:
				res.append(intervals[i])
			else:
				newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

		res.append(newInterval)
		return res

intervals = [[1,3],[6,9]]
newInterval = [2,5]

# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval = [4,8]

print(Solution.insert(intervals, newInterval))