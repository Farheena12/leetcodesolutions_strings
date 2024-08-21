#https://leetcode.com/problems/sort-the-people/submissions/1363224873/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [j for i,j in sorted(zip(heights,names), reverse=True)]
        

