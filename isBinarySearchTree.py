""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check_binary_search_tree_(root):
    return check_binary_search_tree_recursive(root,float("-inf"),float("inf"))

def check_binary_search_tree_recursive(root,min,max):
    if root is None:
        return True
    if root.left <= min or root.right >= max:
        return False
    check = check_binary_search_tree_recursive(root.left,min,root.val) and check and                              check_binary_search_tree_recursive(root.right, root.val,max)
    #check = check and check_binary_search_tree_recursive(root.right, root.val,max )
    
    return check
  