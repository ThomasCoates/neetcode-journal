from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s  # "noob" -> 4#noob
        return result

    def decode(self, s: str) -> List[str]:
        result, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#": 
                j += 1 
            length = int(s[i:j]) # from i to j, excluding index j
            result.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return result