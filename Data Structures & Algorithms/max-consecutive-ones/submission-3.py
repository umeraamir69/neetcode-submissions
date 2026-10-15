class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLength = 0
        length = 0
        for i , num in enumerate(nums):
            if num == 1:
                length +=1
            else:
                maxLength = max(maxLength , length)
                length =0 
            
        
        return max(maxLength , length)