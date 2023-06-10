class Solution():
	def combinationSum(candidates:list, target:int) -> list:
		res = []

		def dfs(i, cur, total):
			if total == target:
				res.append(cur.copy())
				return
			if total > target or i >= len(candidates):
				return

			cur.append(candidates[i])
			dfs(i, cur, total+candidates[i])
			cur.pop()
			dfs(i+1, cur, total)

		dfs(0, [], 0)

		return res


candidates = [2,3,6,7]
target = 7

print(Solution.combinationSum(candidates, target))