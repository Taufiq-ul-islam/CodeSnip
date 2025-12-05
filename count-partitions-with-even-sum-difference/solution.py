class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        for x in nums :
            s += x
        if s % 2 == 0 :  # If sum of all elements is even, the difference of partition sums is even
            return len(nums) - 1
        return 0
