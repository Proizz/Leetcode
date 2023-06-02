"""def middleNode(self, head: ListNode) -> ListNode:
#Solution works, but it is hurting the use of a linked list when creating a normal List to keep track of the Nodes.
    length = 0
    l_head = []
    while head is not None:
        length += 1
        l_head.append(head)
        head = head.next
    return l_head[int(length / 2)]"""


"""def middleNode(self, head: ListNode) -> ListNode:
# Solution works but it can be programmed leaner
    middle = head
    end = head
    counter = 0
    while end:
        counter += 1
        end = end.next
        if counter == 2:
            counter = 0
            middle = middle.next
    return middle"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # Solution works by iterate the end pointer by 2 every step, so the middle pointer can be increased every step
        middle = end = head
        while end and end.next:
            end = end.next.next
            middle = middle.next
        return middle


head = [1, 2, 3, 4, 5]
s = Solution()
ll_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print(head)
print(s.middleNode(ll_head))
print()
