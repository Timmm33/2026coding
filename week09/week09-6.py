## week09-6.py
## Definition for singly-linked list.
## class ListNode:
##     def __init__(self, val=0, next=None):
##         self.val = val
##        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        while head: ##逐一將 Linked List的值，放入陣列a
            a.append(head.val)
            head = head.next ## 記得要換下一筆

        N = len(a) ## 陣列的大小
        now = ans = ListNode() ## 答案，有個Node右邊會塞真的Nodes
        for i in range(0, N, 2): ##偶數堆
            now.next = ListNode(a[i]) ## 逐一塞過去
            now = now.next ## 串接下一個
        for i in range(1, N, 2): ## 奇數堆
            now.next = ListNode(a[i]) ## 逐一塞過去
            now = now.next ## 串接下一個
        return ans.next
