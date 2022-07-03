class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
		container = ListNode()
		carry = 0
		cur = container
		while l1 or l2 or carry > 0:
			v1 = l1.val if l1 else 0
			v2 = l2.val if l2 else 0
			v_sum = v1 + v2 + carry

			carry = v_sum // 10
			cur.next = ListNode(v_sum % 10)

			l1 = l1.next if l1 else None
			l2 = l2.next if l2 else None

			cur = cur.next

		return container.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

print(Solution.addTwoNumbers(l1,l2).val)