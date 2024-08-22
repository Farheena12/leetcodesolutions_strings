#https://leetcode.com/problems/count-asterisks/submissions/1364335298/

class Solution:
    def countAsterisks(self, s: str) -> int:
        return sum(1 for i,char in enumerate(s) if char == "*" and s[:i].count("|") % 2== 0)
