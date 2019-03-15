class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        '''
        异或，这里可以看作是相加但是不显示进位。a^b
        相与为了把进位显示出来。

        '''

        # return sum([a,b])

        # 人家的解法
        while(b != 0):
            s = (a ^ b) & 0xFFFFFFFF
            jinwei = ((a & b) << 1) & 0xFFFFFFFF
            a = s
            b = jinwei
        return a if a < 0X7fffffff else ~(a ^ 0xFFFFFFFF)


print(Solution().getSum(2, 3))
