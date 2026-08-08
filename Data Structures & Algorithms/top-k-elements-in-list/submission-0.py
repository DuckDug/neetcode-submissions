class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        for x in nums:
            if x in myDict:
                myDict[x] += 1
            else:
                myDict[x] = 1
        print(myDict)
        frequencies = list(myDict.values())
        frequencies.sort(reverse=True)
        kFreqs = frequencies[:k]
        print(kFreqs)
        result = []
        for key, value in myDict.items():
            if value in kFreqs:
                result.append(key)
        return result
