class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openings = ['(', '[', '{']
        closings = [')', ']', '}']
        for char in s: 
            if char in openings: 
                stack.append(char)
            if len(stack) == 0:
                    return False
            if char in closings and len(stack) > 0:
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                    continue
                if char == ']' and stack[-1] == '[':
                    stack.pop()
                    continue
                if char == '}' and stack[-1] == '{':
                    stack.pop()
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
                