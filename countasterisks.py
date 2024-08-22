#https://leetcode.com/problems/count-asterisks/submissions/1364335298/

class Solution:
    def countAsterisks(self, s: str) -> int:
        cnt = 0
        inside_bar = False
        for char in s:
            if char == "|":
                inside_bar = not inside_bar
            elif char == "*" and not inside_bar:
                cnt += 1
        return cnt
