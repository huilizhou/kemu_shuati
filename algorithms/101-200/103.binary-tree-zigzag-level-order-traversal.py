# 二叉树的锯齿形层次遍历
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 我的想法
        # if root is None:
        #     return []
        # result, current, level = [], [root], 1
        # while current:
        #     next_level, vals = [], []
        #     for node in current:
        #         vals.append(node.val)
        #         if node.left:
        #             next_level.append(node.left)
        #         if node.right:
        #             next_level.append(node.right)
        #     if level % 2:
        #         result.append(vals)
        #     else:
        #         result.append(vals[::-1])
        #     level += 1
        #     current = next_level
        # return result

        # 人家的解法
        if not root:
            return []
        res, queue = [], [root]
        index = 1
        while queue:
            templist = []
            length = len(queue)
            for _ in range(length):
                node = queue.pop(0)
                templist.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if index < 0:
                templist.reverse()
            index *= -1
            res.append(templist)
        return res


tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print(Solution().zigzagLevelOrder(tree))
