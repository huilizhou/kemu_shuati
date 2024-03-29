# 合并区间
# Definition for an interval.


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda x: x.start)
        l = intervals[0].start
        r = intervals[0].end
        ans = []
        for i in intervals:
            if r >= i.start:
                r = max(r, i.end)
            else:
                ans.append(Interval(l, r))
                l = i.start
                r = i.end
        ans.append(Interval(l, r))
        return ans


# print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
