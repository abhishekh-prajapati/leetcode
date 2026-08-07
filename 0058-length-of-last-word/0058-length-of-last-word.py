class Solution(object):
    def lengthOfLastWord(self, s):
        last = len(s) - 1

        while last >= 0 and s[last] == ' ':
            last -= 1

        count = 0

        while last >= 0 and s[last] != ' ':     
            count += 1
            last -= 1

        return count