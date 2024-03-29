class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 人家的解法
        # return 2 ** (len(bin(num)) - 2) - 1 - num

        # # 我的解法
        # z = bin(num)[2:]
        # z1 = ''
        # for i in z:
        #     if i == '1':
        #         z1 += '0'
        #     else:
        #         z1 += '1'
        # res = int(z1, 2)
        # return res

        # 人家的解法
        # n = 2
        # while n < num:
        #     n <<= 1
        # return n - 1 - num

        i = 1
        while num >= i:
            num ^= i
            i <<= 1
        return num


print(Solution().findComplement(5))
