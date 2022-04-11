"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

Examples:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
"""
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None or root.left is None:
            return root 
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        
        self.connect(root.left)
        self.connect(root.right)
        
        return root