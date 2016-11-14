"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Link : https://leetcode.com/problems/valid-anagram/

Solution accounts for unicode

"""
char_set = 256

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
         # Create two count arrays and initialize all values as 0
        counter1 = [0] * char_set
        counter2 = [0] * char_set
 
    # For each character in input strings, increment count
    # in the corresponding count array
        for i in s:
            counter1[ord(i)]+=1
 
        for i in t:
            counter2[ord(i)]+=1
 
    # If both strings are of different length. Removing this
    # condition will make the program fail for strings like
    # "aaca" and "aca"
        if len(s) != len(t):
            return False
 
    # Compare count arrays
        for i in xrange(char_set):
            if counter1[i] != counter2[i]:
                return False
 
        return True
