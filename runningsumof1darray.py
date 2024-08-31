#https://leetcode.com/problems/running-sum-of-1d-array/submissions/1373877723/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            nums[i] = sum
        
        return nums
        
