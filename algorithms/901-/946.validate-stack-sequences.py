class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        i = 0
        for temp in pushed:
            stack.append(temp)
            while stack and popped[i] == stack[-1]:
                stack.pop()
                i += 1
        return len(stack) == 0


print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
