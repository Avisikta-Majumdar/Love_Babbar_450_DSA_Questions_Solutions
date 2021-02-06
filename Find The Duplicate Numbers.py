class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a=[]
        for i in nums:
            if not(i in a):
                a.append(i) 
            else:
                return i
