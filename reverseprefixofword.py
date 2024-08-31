#https://leetcode.com/problems/reverse-prefix-of-word/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        return (word[:word.find(ch)+1][::-1]+word[word.find(ch)+1:] or word)
        

