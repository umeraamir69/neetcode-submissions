class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        check = 0 
        for i in nums:
            if i==0:
                check+=1
        res = [0]*(len(nums))

        if check >= 2:
            return res



        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]   
        
        postfix = 1
        for i in range(len(nums)-1 , -1 ,-1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res