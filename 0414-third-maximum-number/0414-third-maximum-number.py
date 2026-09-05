class Solution(object):
    def thirdMax(self, nums):

        first = None
        second = None
        third = None

        for i in nums:

            if i == first or i == second or i == third:
                continue

            if first is None or i > first:
                third = second
                second = first
                first = i

            elif second is None or i > second:
                third = second
                second = i

            elif third is None or i > third:
                third = i

        if third is None:
            return first

        return third