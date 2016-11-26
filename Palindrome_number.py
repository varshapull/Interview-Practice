#Palindrome number
#https://leetcode.com/problems/palindrome-number/

class Solution:
	def isPalindrome(self,x):
		num = x
		rev_num = 0

		while(num > 0):
			digit = num % 10
			rev_num = rev_num * 10 + digit
			num = num / 10

		if rev_num == x:
			return True
		else: 
			return False