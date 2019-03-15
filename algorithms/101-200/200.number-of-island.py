# 岛屿的个数
'''
每次遇到“1”之后，开始左右上下搜索把访问过的都变为1

'''


# class Solution:
# def numIslands(self, grid):
#     """
#     :type grid: List[List[str]]
#     :rtype: int
#     """
#     def helper(grid, i, j):
#         grid[i][j] = "0"
#         # 进入左边，把左边的1置为0
#         if j > 0 and grid[i][j - 1] == "1":
#             helper(grid, i, j - 1)
#         # 进入右边，把右边的1置为0
#         if j < len(grid[0]) - 1 and grid[i][j + 1] == "1":
#             helper(grid, i, j + 1)
#         # 进入上边，把上边的1置为0
#         if i > 0 and grid[i - 1][j] == "1":
#             helper(grid, i - 1, j)
#         # 进入下边，把下边的1置为0
#         if i < len(grid) - 1 and grid[i + 1][j] == "1":
#             helper(grid, i + 1, j)

#     count = 0
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j] == "1":
#                 helper(grid, i, j)
#                 count += 1
#     return count

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self.dfs(grid, row, col, i, j)
                    count += 1
        return count

    def dfs(self, grid, row, col, x, y):
        if grid[x][y] == '0':
            return
        grid[x][y] = '0'

        if x != 0:
            self.dfs(grid, row, col, x - 1, y)
        if x != row - 1:
            self.dfs(grid, row, col, x + 1, y)
        if y != 0:
            self.dfs(grid, row, col, x, y - 1)
        if y != col - 1:
            self.dfs(grid, row, col, x, y + 1)


print(Solution().numIslands([['1', '0', '1', '0', '1'], [
      '0', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']]))
