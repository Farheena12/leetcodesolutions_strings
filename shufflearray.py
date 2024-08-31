#https://leetcode.com/problems/shuffle-the-array/submissions/1374415100/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n1 = nums[:len(nums[n:])]
        n2 = nums[len(nums[n:]):]
        result = []

        for i, j in zip(n1, n2):
            result.append(i)
            result.append(j)

        return (result)
                
