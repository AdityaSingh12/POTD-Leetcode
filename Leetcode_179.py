"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.


"""

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        
        nums.sort(reverse=True, key=lambda x: (x*10))

        try:
            return str(int("".join(nums)))
        except:
            return "".join(nums)