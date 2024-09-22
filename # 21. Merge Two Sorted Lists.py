# 21. Merge Two Sorted Lists

# Work
# Merge two sorted linked lists and return it as a new sorted list.
# The new list should be made by splicing together the nodes of the first two lists.

# Function Signature:
# def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:

# Input:
# - Two linked lists l1 and l2 where the nodes are sorted in non-decreasing order.
# - Each list can be empty (null).

# Output:
# - Return a new linked list that is the result of merging the two input lists.

# Definition for a singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def p(self):
        
        while self:
            print(self.val,end = " -> ")
            self = self.next
        print("None")
# Solution

def mergeTwoLists(l1, l2):
    if l1 == None and l2 == None:
        return []
    elif l1 == None:
        return [l2.val]
    elif l2 == None:
        return [l1.val]

    if l1.val > l2.val:
        head = l2
        l2 = l2.next
    else:
        head = l1
        l1 = l1.next

    result = head
    
    while l1 and l2:
        if l1.val > l2.val:
            result.next = l2
            l2 = l2.next
        else:
            result.next = l1
            l1 = l1.next
        result = result.next

    if l1:
        result.next = l1
    else:
        result.next = l2
      
    return head.val

# Example 1:
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
output = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
print(f"Input: l1 = [1,2,4], l2 = [1,3,4]\nOutput: [1,1,2,3,4,4] ==>", mergeTwoLists(l1, l2))

# Example 2:
# Input: l1 = [], l2 = [0]
# Output: [0]
l1 = None
l2 = ListNode(0)
output = ListNode(0)
print(f"Input: l1 = [], l2 = [0]\nOutput: [0] ==>", mergeTwoLists(l1, l2))

# Example 3:
# Input: l1 = [], l2 = []
# Output: []
l1 = None
l2 = None
output = None
print(f"Input: l1 = [], l2 = []\nOutput: [] ==>", mergeTwoLists(l1, l2))

# Boundary Example 1:
# Input: l1 = [1,2,3], l2 = [4,5,6]
# Output: [1,2,3,4,5,6]
l1 = ListNode(1, ListNode(2, ListNode(3)))
l2 = ListNode(4, ListNode(5, ListNode(6)))
output = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
print(f"Input: l1 = [1,2,3], l2 = [4,5,6]\nOutput: [1,2,3,4,5,6] ==>", mergeTwoLists(l1, l2))

# Boundary Example 2:
# Input: l1 = [1], l2 = [2]
# Output: [1,2]
l1 = ListNode(1)
l2 = ListNode(2)
output = ListNode(1, ListNode(2))
print(f"Input: l1 = [1], l2 = [2]\nOutput: [1,2] ==>", mergeTwoLists(l1, l2))

