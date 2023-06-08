class TreeNode():
	def __init__(self, val=0, right=None, left=None):
		self.val = val
		self.right = right
		self.left = left

	def __str__(self):
		return f'Node(val: {self.val}, left: {self.left}, right: {self.right})'

class Solution():
	def invertTreeBFS(root: TreeNode) -> TreeNode:
		currNode = root
		queue = [currNode]

		while len(queue) != 0:
			currNode = queue.pop()
			if not currNode:
				continue
			tmp = currNode.left
			currNode.left = currNode.right
			currNode.right = tmp
			if currNode.left:
				queue.append(currNode.left)
			if currNode.right:
				queue.append(currNode.right)

		return root

	def invertTreeDFS(root: TreeNode) -> TreeNode:
		if root is None:
			return None

		tmp = root.left
		root.left = root.right
		root.right = tmp

		Solution.invertTreeDFS(root.left)
		Solution.invertTreeDFS(root.right)

		return root
		

myTree = TreeNode(4)
myTree.left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
myTree.right = TreeNode(7, left=TreeNode(6), right=TreeNode(9))
print(myTree)

invertedTreeBFS = Solution.invertTreeBFS(myTree)
print(invertedTreeBFS)

myTree = TreeNode(4)
myTree.left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
myTree.right = TreeNode(7, left=TreeNode(6), right=TreeNode(9))

invertedTreeDFS = Solution.invertTreeDFS(myTree)
print(invertedTreeDFS)