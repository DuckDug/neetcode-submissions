class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}

        for x in strs:
            sorted_characters = sorted(x)
            sorted_string_asc = "".join(sorted_characters)
            
            if sorted_string_asc in myDict:
                dictValue = myDict[sorted_string_asc]
                dictValue.append(str(x))
                myDict[sorted_string_asc] = dictValue
            else:
                newList = [x]
                myDict[sorted_string_asc] = newList

        return list(myDict.values())
        # return myDict.values()

