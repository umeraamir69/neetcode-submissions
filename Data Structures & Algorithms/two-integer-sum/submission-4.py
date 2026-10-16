class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSum = {} # key diff : value  index

        for i , num in enumerate (nums):
            diff = target - num
            if diff in hashSum:
                return [hashSum[diff] , i]
            else:
                hashSum[num] = i 

