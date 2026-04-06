class Solution:
    def createWordDict(self, word: str):
        wordDict = dict()
        for i, j in enumerate(word):
            if j in wordDict:
                wordDict[j] += 1
            else:
                wordDict[j] = 1
        return wordDict

    # def isWordinWordDict(self, wordDict: dict, wordsDict: dict):
    #     for w in wordsDict.keys():
    #         if wordDict == w: 
    #             return True
    #     return False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordsDict = dict()
        for word in strs:
            wordTuple = tuple(sorted(self.createWordDict(word).items())) 
            if wordTuple in wordsDict:
                wordsDict[wordTuple].append(word)
            else:
                wordsDict[wordTuple] = [word]
        return list(wordsDict.values())