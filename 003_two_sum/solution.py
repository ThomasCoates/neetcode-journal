class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for index_a, a in enumerate(nums):
            for index_b, b in enumerate(nums):
                if nums[index_a] + nums[index_b] == target and index_a != index_b:
                    output.append(index_a)
                    output.append(index_b)
                    return output
