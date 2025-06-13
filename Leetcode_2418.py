class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        n = len(names)
        index = list(range(n))

        index.sort(key=lambda i: heights[i], reverse=True)

        result = [names[i] for i in index]
        return result

names = ["Mary","John","Emma"]
heights = [180,165,170]

print(Solution().sortPeople(names, heights))