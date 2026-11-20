# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return None

        pos=0
        temp=head

        while temp:
            pos+=1
            temp=temp.next
        pos=pos//2
        curr=head
        prev=None
        count=0
        while count<pos:
            prev=curr
            curr=curr.next
            count+=1
        prev.next=curr.next
        return head       