class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 人家的解法
        pos = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
        return nums

        # 这种解法是先将非零项全部提取出来，最后接上为0的元素。
        # 直观的解法是建立新的数组，不符合题意的要求。

        # n = len(nums)
        # i = -1
        # j = 0
        # # nums[0...i]表示非零元素的数列，初始值为i=-1
        # while j <= n - 1:
        #     if nums[j] != 0:
        #         i += 1
        #         nums[i] = nums[j]
        #     j += 1
        # for k in range(i + 1, n):
        #     nums[k] = 0
        # return nums

        # 人家的解法，很巧妙
        # for i in range(len(nums) - 1, -1, -1):
        #     if nums[i] == 0:
        #         del nums[i]
        #         nums.append(0)
        # return nums


print(Solution().moveZeroes([1, 0, 2, 0, 3, 5, 9]))
