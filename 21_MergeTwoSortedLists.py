# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

    def __str__(self):
        ret = f'Node(val: {self.val}, next: {self.next})'
        return ret


class Solution:
    def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
        mergedList = ListNode()
        tail = mergedList

        while list1 and list2:
            if list1.val <= list2.val:
                newNode = ListNode(list1.val)
                list1 = list1.next
            else:
                newNode = ListNode(list2.val)
                list2 = list2.next
            tail.next = newNode
            tail = newNode
        
        while list1:
            newNode = ListNode(list1.val)
            tail.next = newNode
            tail = newNode
            list1 = list1.next
        while list2:
            newNode = ListNode(list2.val)
            tail.next = newNode
            tail = newNode
            list2 = list2.next

        return mergedList.next

# Creating a list1
list1 = ListNode(1)
tail = list1

newNode = ListNode(2)
tail.next = newNode
tail = newNode

newNode = ListNode(4)
tail.next = newNode
tail = newNode

# Creating a list2
list2 = ListNode(1)
tail = list2

newNode = ListNode(3)
tail.next = newNode
tail = newNode

newNode = ListNode(4)
tail.next = newNode
tail = newNode

print('list1: ', list1)
print('list2: ', list2)

# Merging two lists
mergedList = Solution.mergeTwoLists(list1, list2)
print('mergedList: ', mergedList)