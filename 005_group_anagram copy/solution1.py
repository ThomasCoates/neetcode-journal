class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        freqMap = {}
        amount = k

        for i in range(len(nums)):
            if nums[i] in freqMap:
                freqMap[nums[i]] += 1
            else:
                freqMap[nums[i]] = 1
       
        while amount >= 1:
            max_key = max(freqMap, key=freqMap.get)
            output.append(max_key)
            freqMap.pop(max_key)
            amount -= 1

        return output