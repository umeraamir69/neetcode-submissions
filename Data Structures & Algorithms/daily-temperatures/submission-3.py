class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0] * len(temp)
        stack = []  # [temp , index]

        for i, t in enumerate(temp):
            while stack and t> stack[-1][0]:
                tmp , index = stack.pop()
                res[index] = i- index
            stack.append([t,i])


        return res