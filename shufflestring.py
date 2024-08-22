#https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res =''.join([j for i, j in sorted(zip(indices, s))])
        return res
