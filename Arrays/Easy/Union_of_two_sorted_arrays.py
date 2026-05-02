class Solution:
    def unionArray(self, nums1, nums2):
        new_set = set()
        for i in range(len(nums1)):
            new_set.add(nums1[i])
        for j in range(len(nums2)):
            new_set.add(nums2[j])
        new_list = sorted(list(new_set))
        return new_list
