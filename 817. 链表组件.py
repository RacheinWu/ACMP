from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        ans = 0
        numsSet = set(nums)
        while head:
            if head.val in numsSet:
                while head and head.val in numsSet:
                    head = head.next
                ans += 1
            else:
                head = head.next
        return ans
