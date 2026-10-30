class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(p,s) for p , s in zip(position , speed)]
        arr.sort(key=lambda x:x[0] ,reverse = True)

        stack = [] # Mono tonic Stack 

        for p , s in arr:
            stack.append((target-p) / s)
            if len(stack) >=2 and stack[-2] >= stack[-1]:
                stack.pop()
                
        return(len(stack))


