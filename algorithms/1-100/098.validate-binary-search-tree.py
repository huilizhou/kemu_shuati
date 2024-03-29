# 验证二叉搜索树
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 我的想法
        return self.validBST(root, -2**32, 2**32 - 1)

    def validBST(self, root, small, large):
        if root == None:
            return True
        if small >= root.val or large <= root.val:
            return False
        return self.validBST(root.left, small, root.val) and self.validBST(root.right, root.val, large)

        # 人家的解法
        # stack = []
        # prev = None
        # while root or stack:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     if prev and prev.val >= root.val:
        #         return False
        #     prev = root
        #     root = root.right
        # return True


tree = TreeNode(4)
tree.left = TreeNode(1)
tree.right = TreeNode(6)
tree.right.left = TreeNode(5)
tree.right.right = TreeNode(7)
print(Solution().isValidBST(tree))
