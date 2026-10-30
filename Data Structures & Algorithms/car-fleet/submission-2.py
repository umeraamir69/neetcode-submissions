class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(p,s) for p , s in zip(position , speed)]
        arr.sort(key=lambda x:x[0] ,reverse = True)

        stack = [] # Mono tonic Stack 

        for p , s in arr:
            diff = (target-p) / s
            if not(stack and stack[-1][2] >= diff ):
                stack.append((p,s,diff))
                
        return(len(stack))


