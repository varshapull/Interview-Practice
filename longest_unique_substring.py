
class Solution(object):

	def longest_unique_substring(self,s):
        max_length = 0
        counter = 0
        char_dict = {}
    
        for idx,char in enumerate(s):
            if char in char_dict:
                counter = max(counter,char_dict[char]+1)
        
            char_dict[char] = idx
            max_length = max(max_length,idx-counter+1)
    
        return max_length