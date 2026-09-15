class Solution(object):
    def uniqueOccurrences(self, arr):
        count = {}

        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        values = []

        for num in count:
            if count[num] in values:
                return False
            values.append(count[num])

        return True