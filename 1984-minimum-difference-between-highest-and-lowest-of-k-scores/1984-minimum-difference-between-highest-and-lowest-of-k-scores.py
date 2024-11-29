class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0  
        nums.sort()  
        min_diff = nums[-1]
        
        for i in range(len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i] 
            if diff < min_diff:
                min_diff = diff
            
        return min_diff