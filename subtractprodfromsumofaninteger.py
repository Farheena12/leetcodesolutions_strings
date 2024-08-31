#https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/submissions/1373954756/


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return (prod(map(int, str(n)))  - sum(map(int, str(n))))
        
