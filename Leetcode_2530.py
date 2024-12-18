"""
Maximal Score After applying k operations

You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.

In one operation:

choose an index i such that 0 <= i < nums.length,
increase your score by nums[i], and
replace nums[i] with ceil(nums[i] / 3).
Return the maximum possible score you can attain after applying exactly k operations.

The ceiling function ceil(val) is the least integer greater than or equal to val.
"""

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heapify(pq:=[-x for x in nums])
        score=0
        for i in range(k):
            x=-heappop(pq)
            score+=x
            if x==1:
                score+=k-1-i
                break
            heappush(pq, -((x+2)//3))
        return score
        