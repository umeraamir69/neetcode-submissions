class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0 : 
            return False
        
        stack = []

        pairs = {"(" : ")" , "{" : "}" ,  "[" : "]"}  # key : opeing , value: closing
        for i in s:
            if i in pairs:
                stack.append(i)
            elif i in pairs.values():
                if stack and pairs[stack[-1]] == i:
                    stack.pop()
                else: 
                    return False


        return True if not stack else False