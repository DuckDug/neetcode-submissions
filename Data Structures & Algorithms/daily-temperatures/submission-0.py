class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        resultArray = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                poppedValue = stack.pop()
                poppedIndex = poppedValue[1]
                resultArray[poppedIndex] = index - poppedIndex
            stack.append([temp, index])

        return resultArray