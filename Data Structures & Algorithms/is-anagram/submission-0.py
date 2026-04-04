class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_dict = dict()
        for i in s:
            if i not in word_dict.keys():
                word_dict[i] = 1
            else:
                word_dict[i] += 1
        for i in t:
            if i not in word_dict.keys():
                return False
            word_dict[i] -= 1
        for i in word_dict.values():
            if i != 0:
                return False
        return True