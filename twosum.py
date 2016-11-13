#Leetcode problem 1 : Two sum 
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

"""


def twoSum(nums, target):
    numbers = {number : index for index, number in enumerate(nums)}
        
    for i in range(0,len(nums)):
        second_num = target - nums[i]
        if second_num in numbers.keys() and numbers[second_num] != i:
            return [i , numbers[second_num]]

"""
Sample test case : 

nums = [2,7,11,15]
target = 9
output = [0,1]
"""

#print twoSum([0,4,3,0],0)
