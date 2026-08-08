class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        myDict = {}
        stack = []

        for index, pos in enumerate(position):
            myDict[pos] = speed[index]
        position.sort(reverse=True)
        firstFleetTime = (target - position[0]) / myDict[position[0]]
        stack.append(firstFleetTime)
        firstIteration = True

        for car in position:
            carTimeToTarget = (target - car) / myDict[car]
            if carTimeToTarget > stack[-1]:
                stack.append(carTimeToTarget)

        return len(stack)