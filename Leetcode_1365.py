class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:

        k = []
        for i in nums:
            g = 0
            for j in nums:
                if i > j:
                    g += 1
            k.append(g)
        return k

nums = [8,1,2,2,3]

print(Solution().smallerNumbersThanCurrent(nums))