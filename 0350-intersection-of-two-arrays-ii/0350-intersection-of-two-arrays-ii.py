class Solution(object):
    def intersect(self, nums1, nums2):
        output = []
        for i in nums1:
            if i in nums2:
                output.append(i)
                nums2.remove(i)
            
        return output


        