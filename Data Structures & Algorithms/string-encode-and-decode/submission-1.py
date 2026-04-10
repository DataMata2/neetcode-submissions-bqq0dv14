class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ''
        for word in strs:
            code += str(len(str(len(word)))) + str(len(word)) + word
        return code
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s): 
            nlength = int(s[i])
            length = int(s[i+1:i+1+nlength])
            i += 1 + nlength
            res.append(s[i : i + length])
            i += length
        return res