class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]
        for i in tokens:
            if i in operations:
                b = int(stack.pop())
                a = int(stack.pop())

                match i:
                    case "+":
                        res =  a+b
                    case "-":
                        res =  a-b
                    case "*":
                        res =  a*b
                    case "/":
                        res= a/b
                stack.append(res)
            else:
                stack.append(i)

        return int(stack.pop())
