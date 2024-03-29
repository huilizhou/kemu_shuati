# 希尔排序
"""
20190117 恪穆整理

希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。
希尔排序是非稳定排序算法。
希尔排序是基于插入排序的以下两点性质而提出改进方法的：

插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率
但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位。

所谓的基本有序，就是小的关键字基本在前面，大的关键字基本在后面，不大不小的基本在中间。

采取跳跃分割的策略：将相距某个“增量”的记录组成一个子序列，
这样才能保证在子序列内分别进行插入排序后得到的结果是基本有序而不是局部有序的。

希尔排序的关键并不是随便分组后各自排序，而是将相隔某个“增量”的记录组成一个子序列，
实现跳跃式移动，使得排序的效率提高。
"""


class Solution:
    def shell_sort(self, list):
        n = len(list)
        # 初始步长
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = list[i]
                j = i
                while j >= gap and list[j - gap] > temp:
                    list[j] = list[j - gap]
                    j -= gap
                list[j] = temp
            gap = gap // 2
        return list


print(Solution().shell_sort([2, 1, 3, 7, 5, 6, 4]))
