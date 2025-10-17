from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # We want the product of the values to the left and right of the index we are computing

        # Start : Stop : Step

        # We are at a number with i, we calculate the total for all numbers with j != i   
        
        result = []
        for i in range(len(nums)):
            total = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                else:
                    total *= nums[j]
            result.append(total)            
        return result

# Brute force method, not optimal but I did this with no help. Proud of myself on this one.
# Time Complexity = O(n^2) -> two nested loops
# Space Complexity = O(n) -> output list grows with input size 