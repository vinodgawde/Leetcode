class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = None
        count = 0
        for i in range(len(nums)):
            if count == 0:
                count = 1
                majority = nums[i]
            elif nums[i] == majority:
                count+=1
            else:
                count -=1
        
        count1=0
        for i in range(len(nums)):
            if nums[i] == majority:
                count1 +=1

        if count1 > (len(nums)//2):
            return majority
        return -1
        