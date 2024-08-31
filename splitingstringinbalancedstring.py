#https://leetcode.com/problems/split-a-string-in-balanced-strings/submissions/1373969277/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = balance = 0
        for char in s:
            balance +=1 if char == 'R' else -1
            if balance == 0:
                cnt +=  1
        return cnt
        
