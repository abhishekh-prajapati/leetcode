class Solution(object):
    def majorityElement(self, nums):
        count = None
        max = 0
        for i in nums:
            if max == 0:
                count = i
            if i == count:
                max += 1
            else:
                max -= 1
        return count 