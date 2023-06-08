from collections import deque

class TreeNode():
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __str__(self):
		return f'Node(val: {self.val}, left: {self.left}, right: {self.right})'

class Solution():
	def maxDepthDFSRecursive(root:TreeNode) -> int:
		# O(n) space, O(n) time
		if root is None:
			return 0

		return 1 + max(Solution.maxDepthDFSRecursive(root.left), Solution.maxDepthDFSRecursive(root.right))

	def maxDepthBFS(root:TreeNode) -> int:
		# O(n) space, O(n) time
		queue = deque([root])
		level = 0
		while len(queue) != 0:
			for i in range(len(queue)):
				currNode = queue.popleft()
				if currNode.left:
					queue.append(currNode.left)
				if currNode.right:
					queue.append(currNode.right)
			level += 1
		return level

	def maxDepthDFSIterative(root:TreeNode) -> int:
		# O(n) space, O(n) time
		# stack = [[node, depth]]
		stack = [[root,1]]
		maxDepthCount = 0

		while len(stack) != 0:
			node, depth = stack.pop()
			if node:
				maxDepthCount = max(maxDepthCount, depth)
				stack.append([node.left, depth+1])
				stack.append([node.right, depth+1])
		return maxDepthCount

# Creating a tree [3,9,20,None,None,15,7]
myTree = TreeNode(3)
myTree.left = TreeNode(9)
myTree.right = TreeNode(20, TreeNode(15), TreeNode(7))

print(Solution.maxDepthDFSRecursive(myTree))
print(Solution.maxDepthBFS(myTree))
print(Solution.maxDepthDFSIterative(myTree))

