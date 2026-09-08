class Solution:
    def firstUniqChar(self, s):
        count = {}

        # Count every character
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        # Find the first character whose count is 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1