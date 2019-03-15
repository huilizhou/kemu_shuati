# 只出现一次的数字II
'''
人家的思路
如果能设计一个状态转换电路，使得一个数出现3次时能够自动抵消为0，最后剩下的就是只出现一次的数。
开始设计，一个二进制位只能表示0或者1。也就是天生可以记录一个数出现了一次还是两次。
需要记录出现3次，需要两个二进制位。我们需要两个变量，每个变量取一位。
'''


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # s = {}
        # for num in nums:
        #     if not num in s:
        #         s[num] = 1
        #     else:
        #         s[num] += 1
        # for key, value in s.items():
        #     if value == 1:
        #         return key

        # 只有1个数出现1次，余数均出现3次。
        return (sum(set(nums)) * 3 - sum(nums)) // 2

        # 人家的解法，没有明白
        a, b = 0, 0
        for num in nums:
            b = ~a & (b ^ num)
            a = ~b & (a ^ num)
        return b


print(Solution().singleNumber([2, 2, 2, 1]))
