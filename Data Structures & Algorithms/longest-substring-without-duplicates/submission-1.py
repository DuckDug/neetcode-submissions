class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = 0
        maxLength = 0
        leftPointer = 0
        rightPointer = 0
        mySet = set()

        while rightPointer < len(s):
            print(counter)
            while s[rightPointer] in mySet:
                character = str(s[leftPointer])
                mySet.remove(character)
                leftPointer += 1
                counter -= 1

            mySet.add(s[rightPointer])
            counter += 1
            maxLength = max(counter, maxLength)
            rightPointer += 1
            print(counter)
        return maxLength

        