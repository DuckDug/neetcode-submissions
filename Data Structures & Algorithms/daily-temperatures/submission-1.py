class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][0] < temp:
                lastIndex = stack[-1][1]
                result[lastIndex] = index - lastIndex
                stack.pop()
            stack.append([temp, index])
        return result
