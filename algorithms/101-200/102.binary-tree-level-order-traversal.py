# 二叉树的层次遍历
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        if self:
            serial = []
            queue = [self]

            while queue:
                cur = queue[0]

                if cur:
                    serial.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    serial.append("#")

                queue = queue[1:]

            while serial[-1] == "#":
                serial.pop()

            return repr(serial)

        else:
            return None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 人家的解法
        # if root is None:
        #     return []
        # result, current = [], [root]
        # while current:
        #     next_level, vals = [], []
        #     for node in current:
        #         vals.append(node.val)
        #         if node.left:
        #             next_level.append(node.left)
        #         if node.right:
        #             next_level.append(node.right)
        #     current = next_level
        #     result.append(vals)
        # return result

        if not root:
            return []
        res, queue = [], [root]
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
            res.append(templist)
        return res


tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print(Solution().levelOrder(tree))
