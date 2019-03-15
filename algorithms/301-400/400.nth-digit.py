class Solution:
    def findNthDigit(self, n: int) -> int:
        '''
        我们要得到第N位数字，正确的做法是：个位数字有9个，2位数字有90个，3位数字有900个。
        所以我们先求出n是第几位数字，然后判断第n个数字应该落在哪个自然数上。
        最后求出这个自然数会落在自然数的哪一位上。
        '''
        # 人家的解法
        digit = 1
        while n > digit * 9 * 10**(digit - 1):
            n -= digit * 9 * 10**(digit - 1)
            digit += 1
        if digit == 1:
            return n
        a = (n - 1) // digit
        b = (n - 1) % digit
        c = 10**(digit - 1) + a
        d = str(c)
        return int(d[b])

        # _len = 1
        # cnt = 9
        # start = 1
        # while n > _len * cnt:
        #     n -= _len * cnt
        #     _len += 1
        #     cnt *= 10
        #     start *= 10
        # start += (n - 1) // _len
        # return int(str(start)[(n - 1) % _len])


print(Solution().findNthDigit(3))
