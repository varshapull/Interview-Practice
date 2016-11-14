"""
Check if two strings are anagrams
"""

def check_anagram(s,t):
	pos1 = 0
    found = True
        
    while pos1 < len(s) and found:
        found_anagram = False
        pos2 = 0
        while pos2 < len(t) and not found_anagram:
            if s[pos1] == t[pos2]:
                found_ana = True
            else:
                pos2 = pos2 + 1
            

        if found_anagram:
            t[pos2] = None
        else:
            found = False
        pos1 = pos1 +1
    return found