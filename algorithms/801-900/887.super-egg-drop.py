# 鸡蛋掉落
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # 人家的解法
        dp = [0] * (K + 1)
        m = 0
        while dp[K] < N:
            m += 1
            for k in range(K, 0, -1):
                dp[k] = dp[k - 1] + dp[k] + 1
        return m


print(Solution().superEggDrop(1, 2))
