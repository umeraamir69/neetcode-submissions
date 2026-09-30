class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # 1 -> 3 , 2->3 , 3->1
        freq = [[]for i in range(len(nums)+1)] #[[], []]

        for num in nums:
            count[num] = 1 + count.get(num , 0)

        for i , cnt in count.items():
            freq[cnt].append(i)

        res = []

        for i in range(len(freq)-1 , 0 ,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) ==k:
                    return res