from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        output, sequence = 0, 0
        
        if len(setNums) == 1:
            return 1
        elif len(setNums) == 0:
            return 0

        for i in setNums:
            if i - 1 in setNums:
                continue
            elif i - 1 not in setNums:
                sequence = 1
                j = 1
                while i + j in setNums:
                    sequence += 1
                    j +=1
                    if sequence > output:
                        output = sequence
        return output

