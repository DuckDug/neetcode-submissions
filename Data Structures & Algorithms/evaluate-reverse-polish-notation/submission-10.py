class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        mathSymbols = ['+', '-', '*', '/']

        for c in tokens: 
            if c not in mathSymbols:
                stack.append(int(c))
            else:
                a = stack.pop()
                b = stack.pop()
                if c == '+':
                    stack.append(a + b)
                elif c == '-':
                    stack.append(b - a)
                elif c == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(b / a))
        return stack.pop()