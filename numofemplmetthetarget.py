#https://leetcode.com/problems/number-of-employees-who-met-the-target/submissions/1374429892/

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return (sum(1 for w in hours if w >= target))

        
