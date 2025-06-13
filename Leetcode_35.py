class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        a = 0
        for i in range(len(nums)):
            if nums[i] == target:
                a = i
            elif nums[i] < target:
                a = i + 1
        return a

nums = [1,3,5,6]
target = 5
print(Solution().searchInsert(nums, target))