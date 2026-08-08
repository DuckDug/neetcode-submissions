class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s: 
            if char == '{' or char == '(' or char == '[':
                stack.append(char)
            if char == '}' or char == ')' or char == ']':
                if len(stack) == 0:
                    return False
                else:
                    poppedValue = stack.pop();
                print(poppedValue)
                if poppedValue == '{' and char != '}':
                    return False
                if poppedValue == '[' and char != ']':
                    return False
                if poppedValue == '(' and char != ')':
                    return False
        if len(stack) != 0:
            return False
        else:
            return True