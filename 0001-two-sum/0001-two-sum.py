class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevHas={}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevHas:
                return [prevHas[diff],i]
            prevHas[n]=i
        