class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLength = 0
        length = 0
        for i , num in enumerate(nums):
            if num == 1:
                length +=1
            else:
                length =0 
            maxLength = max(maxLength , length)
        
        return maxLength