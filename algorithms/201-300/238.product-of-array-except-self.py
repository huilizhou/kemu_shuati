# 除自身以外的数组的乘积
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # res = [1] * len(nums)
        # for i in range(len(nums) - 2, -1, -1):
        #     res[i] = nums[i + 1] * res[i + 1]
        # for i in range(1, len(nums)):
        #     res[i] *= nums[i - 1]
        #     nums[i] *= nums[i - 1]

        # return res

        # 人家的想法
        dp1 = [1]
        dp2 = [1]
        for i in range(len(nums) - 1):
            dp1.append(dp1[i] * nums[i])
            dp2.append(dp2[i] * nums[-i - 1])
        res = []
        for i in range(len(dp2)):
            res.append(dp1[i] * dp2[-i - 1])
        return res


print(Solution().productExceptSelf([1, 2, 3, 4]))
