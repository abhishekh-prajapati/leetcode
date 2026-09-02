class Solution(object):
    def runningSum(self, nums):
        num = 0
        output = []
        for i in nums:
            num += i
            output.append(num)
        return output