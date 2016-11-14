# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 17:15:50 2016

@author: varshapullabhotla
"""
import sys
def rev_int(x):
    int_str = str(x)
    rev_str = ""
    overflow = 2147483648
    for i in int_str:
        if not i.isdigit():
            rev_str = rev_str + i
        else:
            rev_str = rev_str + int_str[-1]
            int_str = int_str[:-1]
    int_newstr = int(rev_str)
    if -overflow <= int_newstr <= overflow:
        return int_newstr
    else:
        return 0

print rev_int(-100)

print sys.maxint

#%%
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        int_str = str(x)
        rev_str = ""
        overflow = 2147483648
        for i in int_str:
            if not i.isdigit():
                rev_str = rev_str + i
            else:
                rev_str = rev_str + int_str[-1]
                int_str = int_str[:-1]
        int_newstr = int(rev_str)
        if -overflow <= int_newstr <= overflow:
            return int_newstr
        else:
            return 0
            
s = Solution()
print s.reverse(-123)


#%%

#Longest common prefix

def lcp(s1,s2):
    first = 0
    while first < min(len(s1),len(s2)):
        if s1[first] != s2[first]:
            break
        first= first +1
    
    return s1[:first]

list1 = ['catch','cat']

for i in range(1,len(list1)):
    print lcp(list1[i-1],list1[i])
    
#%%
new_str = ""

list1 = ["c","c",'b']
    
for i in range(1,len(list1)):
    if len(list1[i]) == 0:
        continue
    j = 0
    while j < min(len(list1[i-1]),len(list1[i])):
        if list1[i-1][j] != list1[i][j]:
            break
        
        new_str = new_str + list1[i-1][j]
        j = j + 1 
        
        
print new_str

#%%
    
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        str1 = min(strs)
        str2 = max(strs)
        
        for index, word in enumerate(str1):
            if word != str2[index]:
                return str1[:index]
        return str1

s = Solution()
s.longestCommonPrefix(['aa','a'])
#%%
        
def isValid(s):
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            if s[i] == ')':
                if stack == [] or stack.pop() != '(':
                    return False
            if s[i] == ']':
                if stack == [] or stack.pop() != '[':
                    return False
            if s[i] == '}':
                if stack == [] or stack.pop() != '{':
                    return False
        if stack:
            return False
        else:
            return True

str1 = "()"

isValid(str1)


#%%

def parChecker(symbolString):
    s = []
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(" or symbol == '[' or symbol == '{':
            s.append(symbol)
        else:
            if len(s) == 0: 
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and len(s) == 0:
        return True
    else:
        return False

print(parChecker('[({})]'))
print(parChecker('([)]'))

