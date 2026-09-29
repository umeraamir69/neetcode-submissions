class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOne = 0
        streak = 0
        for i in nums:
            if i == 1 :
                streak += 1
                maxOne = max(streak , maxOne)
            else:
                maxOne = max(streak , maxOne)
                streak = 0
        return maxOne   
