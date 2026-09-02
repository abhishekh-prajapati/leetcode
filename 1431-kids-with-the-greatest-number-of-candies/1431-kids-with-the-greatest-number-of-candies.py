class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maximum = max(candies)
        result = []
        for i in candies:
            if i + extraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)
        return result



