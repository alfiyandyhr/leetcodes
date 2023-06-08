class ListNode():
	def __init__(self, val, next=None):
		self.val = val
		self.next = None

	def __str__(self):
		return f'Node(val: {self.val}, next: {self.next})'

class Solution():
	def hasCycle(head: ListNode) -> bool:
		# O(n) time, O(n) space
		curr = head
		hashSet = {}
		while curr:
			if curr in hashSet:
				return True
			else:
				hashSet[curr] = curr.val
		return False

	def hasCycle2(head: ListNode) -> bool:
		# O(n) time, O(1) space
		fast, slow = head, head

		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
			if fast == slow:
				return True
		return False

myLinkedList = ListNode(3)
tail = myLinkedList

newNodePos = ListNode(2)
tail.next = newNodePos
tail = newNodePos

newNode = ListNode(0)
tail.next = newNode
tail = newNode

newNode = ListNode(-4)
tail.next = newNode
tail = newNode

tail.next = newNodePos
tail = newNodePos

print(Solution.hasCycle(myLinkedList))
print(Solution.hasCycle2(myLinkedList))