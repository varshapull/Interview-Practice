"""
Write a function to find the longest common prefix string amongst an array of strings.

https://leetcode.com/problems/longest-common-prefix/
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        str1 = min(strs)
        str2 = max(strs)
        for index, word in enumerate(str1):
            if word != str2[index]:
                return str1[:index]
        return str1
                