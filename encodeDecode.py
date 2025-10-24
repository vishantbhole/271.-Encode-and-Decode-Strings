from typing import List


# 271. Encode and Decode Strings
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            # find '#'
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res

if __name__ == "__main__":
    sol = Solution()
    s = ["neet","code","love","you"]

    outputEncoded = sol.encode(s)

    print("Output for encode is : ", outputEncoded)
    print("Output for decode is : ", sol.decode(outputEncoded))
