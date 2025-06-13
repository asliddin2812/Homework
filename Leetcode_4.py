class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        x = nums1 + nums2
        x.sort()

        if len(x) % 2 == 0:
            y = (x[len(x) // 2] + x[len(x) // 2 - 1]) / 2
        else:
            y = x[len(x) // 2]

        return round(y, 5)
nums1 = [1,3]
nums2 = [2]

print(Solution().findMedianSortedArrays(nums1, nums2))