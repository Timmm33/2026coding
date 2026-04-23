##week09-5.py
## Definition for singly-linked list.
## class ListNode:
##     def __init__(self, val=0, next=None):
##         self.val = val
##         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None: return None

        prev = fast = slow = head
        while fast != None and fast.next != None: ##兔子還沒到終點
            fast = fast.next.next ##兔子跳兩格
            prev = slow ##烏龜在走之前，先記下前一格的位子
            slow = slow.next ##烏龜走一格
        prev.next = slow.next
        return head
