#https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/submissions/1373997088/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            if nums[i] < k:
                cnt += 1
        return cnt
        
