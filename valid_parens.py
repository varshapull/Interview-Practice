"""

"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paren_list = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                paren_list.append(s[i])
            if s[i] == ')':
                if paren_list == [] or paren_list.pop() != '(':
                    return False
            if s[i] == ']':
                if paren_list == [] or paren_list.pop() != '[':
                    return False
            if s[i] == '}':
                if paren_list == [] or paren_list.pop() != '{':
                    return False
        if paren_list:
            return False
        else:
            return True