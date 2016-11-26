#Longest absolute path
#https://leetcode.com/problems/longest-absolute-file-path/

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        paths = input.split("\n")
        n = len(paths) + 1
        stack = [0] * n 
        maxLen = 0
        for s in paths:
            lev = s.rfind("\t") + 1
            currLen = stack[lev+1] = stack[lev] + len(s) - lev + 1
            #currLen = stack[lev+1]
            
            if "." in s:
                maxLen = max(maxLen,currLen-1)
        
        return maxLen