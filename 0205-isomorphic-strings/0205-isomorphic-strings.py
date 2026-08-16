class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        store = {}
        store2 = {}

        num = 1
        for i in s:
            if i not in store:
                store[i] = num
                num += 1

        ginti = 1
        for i in t:
            if i not in store2:
                store2[i] = ginti
                ginti += 1
        pattern1 = [store[i] for i in s]
        pattern2 = [store2[i] for i in t]
        if pattern1 != pattern2:
            return False 
        else:
            return True 
