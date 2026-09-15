class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # value : couunt
        freq = [[] for i in range(len(nums)+1)]  # index treated as frequency & values are []

        for n in nums:
            count[n] = count.get(n ,0 ) + 1

        for v , c in count.items():
            freq[c].append(v)
        
        res = []

        for i in range(len(freq) -1, 0 , -1):
            for x in freq[i]:
                res.append(x)
            if len(res) == k:
                return res
