class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c != '+' and c != '-' and c != '*' and c != '/':
                stack.append(c)
            else:
                a = int(stack.pop())
                lastSum = int(stack.pop())

                if c == '+':
                    lastSum += a
                elif c == '-':
                    lastSum -= a
                elif c == '*':
                    lastSum *= a
                elif c == '/':
                    lastSum /= a
                stack.append(lastSum)
        return int(stack.pop())