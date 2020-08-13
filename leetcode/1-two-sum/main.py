
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = {}
        for i, n in enumerate(nums):
            D[n] = i
        for i, n in enumerate(nums):
            k = target - n
            if k in D and i != D[k]:
                return [i, D[k]]
