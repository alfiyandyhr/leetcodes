class Solution():
	def merge(intervals:list) -> list:
		# O(nlogn)
		if len(intervals) == 1:
			return intervals

		intervals.sort()
		res = []

		i = 1
		first = intervals[0]
		second = intervals[1]

		while i < len(intervals):
			if second[0] < first[1]:
				first = [min(first[0], second[0]), max(first[1], second[1])]

			else:
				res.append(first)
				first = second

			if i+1 < len(intervals):
				second = intervals[i+1]
			else:
				res.append(first)
				return res

			i += 1

intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]]

print(Solution.merge(intervals))