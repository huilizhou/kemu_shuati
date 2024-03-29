# 乘积最大的子序列
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划
        # 最大的连续子序列乘积可以是正数*正数得到，也可以是负数*负数得到
        # 人家的想法
        # maximum = big = small = nums[0]
        # for n in nums[1:]:
        #     big, small = max(n, n * big, n * small), min(n, n * big, n * small)
        #     maximum = max(maximum, big)
        # return maximum

        # 人家的想法
        A = nums
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(max(A), max(B))


print(Solution().maxProduct([-3, -1, -4]))
