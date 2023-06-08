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
		prev, curr = None, head

		while curr:
			nxt = curr.next
			curr.next = prev
			prev = curr
			curr = nxt

		return prev

	def reverseList2(head:ListNode) -> ListNode:
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

print(originalList)

reverseList = Solution.reverseList(originalList)
print(reverseList)

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

reverseList2 = Solution.reverseList2(originalList)
print(reverseList2)