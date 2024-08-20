#https://leetcode.com/problems/truncate-sentence/submissions/1362319292/

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        char_sent = s.split()
        res = " ".join(char_sent[:k])
        return res
        
