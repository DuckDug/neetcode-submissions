class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        myDict = {}
        numberOfFleets = 1

        for index, pos in enumerate(position):
            myDict[pos] = speed[index]
        
        position.sort(reverse=True)
        
        fleetTime = (target - position[0]) / myDict[position[0]]
        for pos in position:
            currTime = (target - pos) / myDict[pos]
            if currTime > fleetTime:
                numberOfFleets += 1
                fleetTime = currTime


        return numberOfFleets