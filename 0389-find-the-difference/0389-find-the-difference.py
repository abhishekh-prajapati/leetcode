class Solution(object):
    def findTheDifference(self, s, t):
        k ={}
        
        for i in s:
            if i in k:
                k[i] += 1
            else:
                k[i] = 1
        l = {}
        for i in t:
            if i in l:
                l[i] += 1
            else:
                l[i] = 1
        for i in l:
            if i not in k:
                return i
            if l[i] > k[i]:
                return i
            