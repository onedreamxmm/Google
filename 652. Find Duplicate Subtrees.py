'''
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.
'''

from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def dfs(node):
            if not node:
                return 'null'
            rep = '%s,%s,%s' % (node.val, dfs(node.left), dfs(node.right))
            trees[rep].append(node)
            return rep

        trees = defaultdict(list)
        dfs(root)
        # print(trees)
        return (trees[rep][0] for rep in trees if len(trees[rep]) > 1)

#I used a preorder traversal and each traversal funciton trv wil return the the values of subtree. Then I saved the the subtree as a key in the hashmap nodes. Finally I returned the first node for every key in the nodes if there are at least 2 values.