# Definition for singly-linked list:
class ListNode():
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = None

	def __str__(self):
		ret = f'Node(val: {self.val}, next: {self.next})'
		return ret

class Solution():
	def reverseList(head:ListNode) -> ListNode:
		if head is None:
			return None

		reverseList = ListNode(head.val)

		while head.next:
			newNode = ListNode(head.next.val)
			newNode.next = reverseList
			reverseList = newNode
			head = head.next

		return reverseList

# Creating a list [1,2,3,4,5]
originalList = ListNode(1)
tail = originalList

newNode = ListNode(2)
tail.next = newNode
tail = newNode

newNode = ListNode(3)
tail.next = newNode
tail = newNode

newNode = ListNode(4)
tail.next = newNode
tail = newNode

newNode = ListNode(5)
tail.next = newNode
tail = newNode

reverseList = Solution.reverseList(originalList)

print(originalList)
print(reverseList)