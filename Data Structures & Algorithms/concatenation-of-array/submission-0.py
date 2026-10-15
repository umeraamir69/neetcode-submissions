class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [] *len(nums)*2
        
        ans = ans + nums
        ans = ans + nums

        return ans