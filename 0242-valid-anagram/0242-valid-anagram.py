class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        for saloni in s:
            if s.count(saloni) != t.count(saloni):
                return False
        return True 