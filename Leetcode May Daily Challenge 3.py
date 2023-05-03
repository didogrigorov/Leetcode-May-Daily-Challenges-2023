class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_1 = set(nums1)
        set_2 = set(nums2)
        result_first = set_1 - set_2
        result_second = set_2 - set_1

        return [list(result_first), list(result_second)]
