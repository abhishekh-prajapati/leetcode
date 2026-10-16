class Solution(object):
    def search(self, nums, target):
        answer = -1
        for i in range(len(nums)):
            if nums[i] == target:
                answer = i
        return answer
